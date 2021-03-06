# Generated by Django 4.0 on 2022-01-03 03:38

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CV",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cv_file_name", models.CharField(blank=True, max_length=200, null=True)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("contact", models.CharField(blank=True, max_length=200, null=True)),
                ("about", models.CharField(blank=True, max_length=600, null=True)),
                ("mail", models.EmailField(blank=True, max_length=200, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("designation", models.CharField(blank=True, max_length=200, null=True)),
                ("linkedin", models.URLField(blank=True, null=True)),
                ("experience_company", models.CharField(blank=True, max_length=200, null=True)),
                ("experience_location", models.CharField(blank=True, max_length=200, null=True)),
                ("experience_duration", models.CharField(blank=True, max_length=200, null=True)),
                ("experience_job_title", models.CharField(blank=True, max_length=200, null=True)),
                ("experience_description", models.CharField(blank=True, max_length=600, null=True)),
                ("education_college", models.CharField(blank=True, max_length=200, null=True)),
                ("education_location", models.CharField(blank=True, max_length=200, null=True)),
                ("education_degree", models.CharField(blank=True, max_length=200, null=True)),
                ("education_duration", models.CharField(blank=True, max_length=200, null=True)),
                ("education_description", models.CharField(blank=True, max_length=600, null=True)),
                (
                    "skills",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100), null=True, size=10
                    ),
                ),
                (
                    "interests",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100), null=True, size=10
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True, null=True)),
                ("updatedAt", models.DateTimeField(auto_now=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="auth.user"
                    ),
                ),
            ],
            options={
                "ordering": ["-createdAt"],
            },
        ),
    ]
