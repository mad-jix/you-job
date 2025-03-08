from django.db import models

from core.models import User
from employer.models import JobPosting


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jobseeker_profile')
    job_title = models.CharField(max_length=100)
    skills = models.JSONField(default=list)
    experience_years = models.PositiveIntegerField(default=0)
    video_resume = models.FileField(upload_to='video_resumes/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)




class Swipe(models.Model):
    SWIPE_CHOICES = (
        ('left', 'Left'),
        ('right', 'Right'),
    )
    
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    direction = models.CharField(max_length=5, choices=SWIPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job_seeker', 'job_posting')

class Match(models.Model):
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    matched_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('job_seeker', 'job_posting')


class Message(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)