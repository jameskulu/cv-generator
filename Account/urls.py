from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.LoginFormView.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
    path("email-confirmation/", views.email_confirmation, name="email-confirmation"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
]
