from rest_framework import serializers

from .models import JobSeekerProfile, Swipe, Match, Message
from employer.serializers import UserSerializer,JobPostingSerializer





class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = JobSeekerProfile
        fields = '__all__'


class SwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    job_seeker = JobSeekerProfileSerializer(read_only=True)
    job_posting = JobPostingSerializer(read_only=True)
    
    class Meta:
        model = Match
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    
    class Meta:
        model = Message
        fields = '__all__'

