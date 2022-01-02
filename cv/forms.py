from django import forms
from django.contrib.auth import authenticate

from .models import CV


class CVCreateForm(forms.ModelForm):
    name = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    contact = forms.CharField(required=True)
    address = forms.CharField(required=True)
    mail = forms.EmailField(required=True)
    linkedin = forms.URLField(required=True)

    class Meta:
        model = CV
        fields = "__all__"
