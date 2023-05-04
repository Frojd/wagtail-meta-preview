# Generated by Django 3.0.8 on 2020-08-02 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0022_uploadedimage"),
        ("wagtailcore", "0045_assign_unlock_grouppagepermission"),
    ]

    operations = [
        migrations.CreateModel(
            name="TwitterPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "twitter_title",
                    models.CharField(
                        blank=True,
                        max_length=70,
                        null=True,
                        verbose_name="Twitter title",
                    ),
                ),
                (
                    "twitter_description",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Twitter description",
                    ),
                ),
                ("og_title", models.CharField(blank=True, max_length=100)),
                ("og_description", models.CharField(blank=True, max_length=100)),
                ("another_title", models.CharField(blank=True, max_length=100)),
                ("another_description", models.CharField(blank=True, max_length=100)),
                (
                    "og_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                        verbose_name="Og image",
                    ),
                ),
                (
                    "twitter_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                        verbose_name="Twitter image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MetaPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "twitter_title",
                    models.CharField(
                        blank=True,
                        max_length=70,
                        null=True,
                        verbose_name="Twitter title",
                    ),
                ),
                (
                    "twitter_description",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Twitter description",
                    ),
                ),
                (
                    "og_title",
                    models.CharField(
                        blank=True,
                        max_length=95,
                        null=True,
                        verbose_name="Facebook title",
                    ),
                ),
                (
                    "og_description",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Facebook description",
                    ),
                ),
                (
                    "og_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                        verbose_name="Facebook image",
                    ),
                ),
                (
                    "twitter_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                        verbose_name="Twitter image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="FacebookPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "og_title",
                    models.CharField(
                        blank=True,
                        max_length=95,
                        null=True,
                        verbose_name="Facebook title",
                    ),
                ),
                (
                    "og_description",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Facebook description",
                    ),
                ),
                ("another_title", models.CharField(blank=True, max_length=100)),
                ("another_description", models.CharField(blank=True, max_length=100)),
                (
                    "og_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                        verbose_name="Facebook image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
