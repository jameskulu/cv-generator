from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list-of-cv/", views.list_of_cv, name="list-of-cv"),
    path("create/", views.create, name="create"),
    path("generate-cv/<int:id>/", views.generate_cv, name="generate-cv"),
    path("edit-cv/<int:id>/", views.edit_cv, name="edit-cv"),
    path("delete-cv/<int:id>/", views.delete_cv, name="delete-cv"),
]
