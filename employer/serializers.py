from rest_framework import serializers

from .models import CompanyProfile, JobPosting,Report, Analytics

from core.serializers import UserSerializer






class CompanyProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = CompanyProfile
        fields = '__all__'

class JobPostingSerializer(serializers.ModelSerializer):
    company = CompanyProfileSerializer(read_only=True)
    
    class Meta:
        model = JobPosting
        fields = '__all__'



class ReportSerializer(serializers.ModelSerializer):
    reporter = UserSerializer(read_only=True)
    reported_user = UserSerializer(read_only=True)
    
    class Meta:
        model = Report
        fields = '__all__'

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = '__all__' 