from django.db import models
from core.models import User



class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    company_size = models.CharField(max_length=50, blank=True)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

class JobPosting(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='job_postings')
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    required_skills = models.JSONField(default=list)


class Report(models.Model):
    REPORT_TYPES = (
        ('spam', 'Spam'),
        ('inappropriate', 'Inappropriate Content'),
        ('fake', 'Fake Profile'),
        ('other', 'Other'),
    )
    
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_filed')
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_received')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

class Analytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_views = models.PositiveIntegerField(default=0)
    total_swipes = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    last_active = models.DateTimeField(auto_now=True)

