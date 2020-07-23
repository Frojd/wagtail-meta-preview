from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from wagtail.images import get_image_model_string


class TwitterModelMixin:
    twitter_title = models.CharField(
        max_length=70, blank=True, null=True, verbose_name=_("Twitter title"),
    )

    twitter_description = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Twitter description"),
    )

    twitter_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Twitter image"),
    )


class FacebookModelMixin:
    og_title = models.CharField(
        max_length=95, blank=True, null=True, verbose_name=_("Facebook title"),
    )

    og_description = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=_("Facebook description"),
    )

    og_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Facebook image"),
    )


class TwitterSeoMixin(TwitterModelMixin):
    pass


class FacebookSeoMixin(FacebookModelMixin):
    pass


class SeoMixin(TwitterSeoMixin, FacebookSeoMixin):
    pass
