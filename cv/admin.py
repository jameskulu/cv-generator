from django.contrib import admin

from .models import CV


class CVAdmin(admin.ModelAdmin):
    model = CV
    list_per_page = 5

    search_fields = ("cv_file_name", "user__username")
    list_display = ("cv_file_name", "user")
    list_filter = ("createdAt", "user")


admin.site.register(CV, CVAdmin)
