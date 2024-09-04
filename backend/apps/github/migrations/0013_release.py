# Generated by Django 5.1 on 2024-08-21 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0012_remove_repository_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="Release",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("tag_name", models.CharField(max_length=100, verbose_name="Tag name")),
                (
                    "description",
                    models.CharField(default="", max_length=500, verbose_name="Description"),
                ),
                ("is_draft", models.BooleanField(default=False, verbose_name="Is draft")),
                (
                    "is_pre_release",
                    models.BooleanField(default=False, verbose_name="Is pre-release"),
                ),
                ("original_created_at", models.DateTimeField(verbose_name="Original created_at")),
                ("published_at", models.DateTimeField(verbose_name="Published at")),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="github.user",
                    ),
                ),
                (
                    "repository",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="github.repository",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Releases",
                "db_table": "github_releases",
            },
        ),
    ]