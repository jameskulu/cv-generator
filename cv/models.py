from django.contrib.auth.models import User
from django.db import models


class CV(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    mail = models.EmailField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ["-createdAt"]
