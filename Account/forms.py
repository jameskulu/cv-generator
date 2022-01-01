from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    # first_name = forms.CharField(max_length=200, help_text="Required")
    # last_name = forms.CharField(max_length=200, help_text="Required")
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError("Email address must be unique.")
        return email


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("username", "password")

#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")

#         if username and password:
#             username_qs = User.objects.filter(username=username)
#             if not username_qs.exists():
#                 raise forms.ValidationError("Invalid Credentials")
#             else:
#                 is_active_qs = User.objects.filter(username=username, is_active=True)
#                 if not is_active_qs.exists():
#                     # raise forms.ValidationError("Account is not active, you need to activate your account before login. An account activation link has been sent to your mailbox.")
#                     raise forms.ValidationError(
#                         f"Account is not verified, your need to verify your account before login."
#                     )
#                 else:
#                     user = authenticate(username=username, password=password)
#                     if not user:
#                         raise forms.ValidationError("Invalid Credentials")

#         return super(LoginForm, self).clean(*args, **kwargs)
