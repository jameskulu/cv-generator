from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("Account.urls")),
    path("", include("cv.urls")),
    path("api/cv/", include("cv.api.urls")),
]
