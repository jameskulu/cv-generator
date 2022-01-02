from django import forms
from django.contrib.auth import authenticate
from django.contrib.postgres.forms import SimpleArrayField

from .models import CV


class CVCreateForm(forms.ModelForm):
    cv_file_name = forms.CharField(required=True)
    name = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    contact = forms.CharField(required=True)
    address = forms.CharField(required=True)
    mail = forms.EmailField(required=True)
    linkedin = forms.URLField(required=True)
    skills = SimpleArrayField(forms.CharField(max_length=100), required=False)
    interests = SimpleArrayField(forms.CharField(max_length=100), required=False)

    class Meta:
        model = CV
        fields = "__all__"
