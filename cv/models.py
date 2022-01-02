from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class CV(models.Model):
    cv_file_name = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    about = models.CharField(max_length=600, null=True, blank=True)
    mail = models.EmailField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    experience_company = models.CharField(max_length=200, null=True, blank=True)
    experience_location = models.CharField(max_length=200, null=True, blank=True)
    experience_duration = models.CharField(max_length=200, null=True, blank=True)
    experience_job_title = models.CharField(max_length=200, null=True, blank=True)
    experience_description = models.CharField(max_length=600, null=True, blank=True)

    education_college = models.CharField(max_length=200, null=True, blank=True)
    education_location = models.CharField(max_length=200, null=True, blank=True)
    education_degree = models.CharField(max_length=200, null=True, blank=True)
    education_duration = models.CharField(max_length=200, null=True, blank=True)
    education_description = models.CharField(max_length=600, null=True, blank=True)

    skills = ArrayField(models.CharField(max_length=100), size=10, null=True)
    interests = ArrayField(models.CharField(max_length=100), size=10, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ["-createdAt"]
