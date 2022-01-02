from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CV

admin.site.unregister(Group)


class CVAdmin(admin.ModelAdmin):
    model = CV
    list_per_page = 5

    search_fields = ("cv_file_name", "user__username")
    list_display = ("cv_file_name", "user")
    list_filter = ("createdAt", "user")


admin.site.register(CV, CVAdmin)
