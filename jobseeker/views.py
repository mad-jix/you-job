from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import JobSeekerProfile,Match,Swipe,Message
from .serializers import JobSeekerProfileSerializer,SwipeSerializer,MatchSerializer,MessageSerializer

class JobSeekerProfileViewSet(viewsets.ModelViewSet):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SwipeViewSet(viewsets.ModelViewSet):
    queryset = Swipe.objects.all()
    serializer_class = SwipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job_seeker = get_object_or_404(JobSeekerProfile, user=self.request.user)
        serializer.save(job_seeker=job_seeker)

        # Check for match if swiped right
        if serializer.validated_data['direction'] == 'right':
            job_posting = serializer.validated_data['job_posting']
            # Create match if employer has also swiped right
            employer_swipe = Swipe.objects.filter(
                job_posting=job_posting,
                direction='right'
            ).exists()
            
            if employer_swipe:
                Match.objects.create(
                    job_seeker=job_seeker,
                    job_posting=job_posting
                )

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'jobseeker_profile'):
            return Match.objects.filter(job_seeker=user.jobseeker_profile)
        elif hasattr(user, 'company_profile'):
            return Match.objects.filter(job_posting__company=user.company_profile)
        return Match.objects.none()

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        match_id = self.kwargs.get('match_pk')
        return Message.objects.filter(match_id=match_id)

    def perform_create(self, serializer):
        match = get_object_or_404(Match, id=self.kwargs.get('match_pk'))
        serializer.save(sender=self.request.user, match=match)

