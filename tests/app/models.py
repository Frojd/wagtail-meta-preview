from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images import get_image_model_string
from .mixins import TwitterModelMixin, FacebookModelMixin, MetaModelMixin


class TwitterPage(TwitterModelMixin, Page):
    og_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Og image"),
    )
    og_title = models.CharField(blank=True, max_length=100)
    og_description = models.CharField(blank=True, max_length=100)
    another_title = models.CharField(blank=True, max_length=100)
    another_description = models.CharField(blank=True, max_length=100)


class FacebookPage(FacebookModelMixin, Page):
    pass


class MetaPage(MetaModelMixin, Page):
    pass
