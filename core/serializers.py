from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


from jobseeker.models import JobSeekerProfile
from employer.models import CompanyProfile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'user_type', 'profile_picture', 'is_email_verified')
        read_only_fields = ('is_email_verified',)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)

class JobSeekerRegistrationSerializer(RegisterSerializer):
    job_title = serializers.CharField(required=True)
    skills = serializers.ListField(child=serializers.CharField(), required=True)
    experience_years = serializers.IntegerField(required=True, min_value=0)
    bio = serializers.CharField(required=False)

    class Meta(RegisterSerializer.Meta):
        fields = RegisterSerializer.Meta.fields + ('job_title', 'skills', 'experience_years', 'bio')

    def create(self, validated_data):
        profile_data = {
            'job_title': validated_data.pop('job_title'),
            'skills': validated_data.pop('skills'),
            'experience_years': validated_data.pop('experience_years'),
            'bio': validated_data.pop('bio', '')
        }
        user = super().create(validated_data)
        JobSeekerProfile.objects.create(user=user, **profile_data)
        return user

class CompanyRegistrationSerializer(RegisterSerializer):
    company_name = serializers.CharField(required=True)
    industry = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    website = serializers.URLField(required=False)
    location = serializers.CharField(required=True)
    company_size = serializers.CharField(required=False)

    class Meta(RegisterSerializer.Meta):
        fields = RegisterSerializer.Meta.fields + (
            'company_name', 'industry', 'description', 
            'website', 'location', 'company_size'
        )

    def create(self, validated_data):
        profile_data = {
            'company_name': validated_data.pop('company_name'),
            'industry': validated_data.pop('industry'),
            'description': validated_data.pop('description'),
            'website': validated_data.pop('website', ''),
            'location': validated_data.pop('location'),
            'company_size': validated_data.pop('company_size', '')
        }
        user = super().create(validated_data)
        CompanyProfile.objects.create(user=user, **profile_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    