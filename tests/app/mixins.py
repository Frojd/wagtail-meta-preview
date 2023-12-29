from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.images import get_image_model_string
from wagtail.models import Page

from wagtail_meta_preview.panels import (
    FacebookFieldPreviewPanel,
    FacebookPreviewPanel,
    GoogleFieldPreviewPanel,
    GooglePreviewPanel,
    TwitterFieldPreviewPanel,
    TwitterPreviewPanel,
)


class TwitterModelMixin(Page):
    twitter_title = models.CharField(
        max_length=70,
        blank=True,
        null=True,
        verbose_name=_("Twitter title"),
    )

    twitter_description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_("Twitter description"),
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
        FieldPanel("og_title"),
        FieldPanel("og_description"),
        FieldPanel("og_image"),
        FieldPanel("another_title"),
        FieldPanel("another_description"),
        TwitterFieldPreviewPanel(
            [
                FieldPanel("twitter_title"),
                FieldPanel("twitter_description"),
                FieldPanel("twitter_image"),
            ],
            heading="Twitter",
        ),
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
        max_length=95,
        blank=True,
        null=True,
        verbose_name=_("Facebook title"),
    )

    og_description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name=_("Facebook description"),
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
        MultiFieldPanel(
            [
                FieldPanel("og_title"),
                FieldPanel("og_description"),
                FieldPanel("og_image"),
            ],
            heading="Facebook",
        ),
        FacebookPreviewPanel(heading="Facebook Preview"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels + promote_panels, heading="Promote"),
        ]
    )

    class Meta:
        abstract = True


class MetaModelMixin(TwitterModelMixin, FacebookModelMixin):
    promote_panels_fields = [
        FacebookFieldPreviewPanel(
            [
                FieldPanel("og_title"),
                FieldPanel("og_description"),
                FieldPanel("og_image"),
            ],
            heading="Facebook",
        ),
        TwitterFieldPreviewPanel(
            [
                FieldPanel("twitter_title"),
                FieldPanel("twitter_description"),
                FieldPanel("twitter_image"),
            ],
            heading="Twitter",
        ),
        GoogleFieldPreviewPanel(
            [
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
            ],
            heading="Google",
        ),
    ]

    promote_panels = [
        FacebookPreviewPanel(heading="Facebook Preview"),
        TwitterPreviewPanel(heading="Twitter Preview"),
        GooglePreviewPanel(heading="Google Preview"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(promote_panels_fields, heading="Previews with fields"),
            ObjectList(
                Page.promote_panels + promote_panels, heading="Previews without fields"
            ),
        ]
    )

    class Meta:
        abstract = True
