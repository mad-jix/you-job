# Generated by Django 5.1.7 on 2025-03-08 06:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_views', models.PositiveIntegerField(default=0)),
                ('total_swipes', models.PositiveIntegerField(default=0)),
                ('matches', models.PositiveIntegerField(default=0)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('website', models.URLField(blank=True)),
                ('location', models.CharField(max_length=100)),
                ('company_size', models.CharField(blank=True, max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=50)),
                ('salary_range', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('required_skills', models.JSONField(default=list)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to='employer.companyprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('spam', 'Spam'), ('inappropriate', 'Inappropriate Content'), ('fake', 'Fake Profile'), ('other', 'Other')], max_length=20)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('reported_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_received', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_filed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
