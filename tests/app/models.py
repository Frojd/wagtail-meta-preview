from django.utils.functional import cached_property

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.images import get_image_model_string
from wagtail.models import Page

from .mixins import FacebookModelMixin, MetaModelMixin, TwitterModelMixin
from wagtail_meta_preview.utils import FacebookSettings


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
    another_title = models.CharField(blank=True, max_length=100)
    another_description = models.CharField(blank=True, max_length=100)

    @cached_property
    def facebook_setting(self) -> FacebookSettings:
        return FacebookSettings(self)

    @cached_property
    def seo_og_title(self):
        return self.facebook_setting.get_title()

    @cached_property
    def seo_og_description(self):
        return self.facebook_setting.get_description()


class MetaPage(MetaModelMixin, Page):
    pass
