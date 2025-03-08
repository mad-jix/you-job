from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

# Create your views here.
from .models import Analytics,Report,JobPosting,CompanyProfile
from .serializers import AnalyticsSerializer,ReportSerializer,JobPostingSerializer,CompanyProfileSerializer



class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        company_profile = get_object_or_404(CompanyProfile, user=self.request.user)
        serializer.save(company=company_profile)

    @action(detail=False, methods=['get'])
    def my_jobs(self, request):
        company_profile = get_object_or_404(CompanyProfile, user=request.user)
        jobs = JobPosting.objects.filter(company=company_profile)
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)


class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        # Check if the user is authenticated
        if isinstance(self.request.user, AnonymousUser):
            return Analytics.objects.none()  # Return an empty queryset if the user is not authenticated
        return Analytics.objects.filter(user=self.request.user)
    


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)
