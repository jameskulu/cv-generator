from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list-of-cv/", views.list_of_cv, name="list-of-cv"),
    path("generate-cv/<int:id>/", views.generate_cv, name="generate-cv"),
]
