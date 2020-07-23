from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from wagtail.images import get_image_model_string
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class TwitterModelMixin(Page):
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

    promote_panels = [
        FieldPanel("twitter_title"),
        FieldPanel("twitter_description"),
        FieldPanel("twitter_image"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels + promote_panels, heading="Promote"),
        ]
    )

    class Meta:
        abstract = True


class FacebookModelMixin(Page):
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

    promote_panels = [
        FieldPanel("og_title"),
        FieldPanel("og_description"),
        FieldPanel("og_image"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels + promote_panels, heading="Promote"),
        ]
    )

    class Meta:
        abstract = True


class SeoModelMixin(TwitterModelMixin, FacebookModelMixin):
    promote_panels = [
        FieldPanel("twitter_title"),
        FieldPanel("twitter_description"),
        FieldPanel("twitter_image"),
        FieldPanel("og_title"),
        FieldPanel("og_description"),
        FieldPanel("og_image"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels + promote_panels, heading="Promote"),
        ]
    )

    class Meta:
        abstract = True
