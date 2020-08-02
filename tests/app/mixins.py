from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    TabbedInterface,
    ObjectList,
    FieldPanel,
    MultiFieldPanel,
)
from wagtail_meta_preview.panels import (
    TwitterPreviewPanelSingle,
    TwitterPreviewPanel,
    FacebookPreviewPanel,
    FacebookPreviewPanelSingle,
    GooglePreviewPanel,
    GooglePreviewPanelSingle,
)


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
        FieldPanel("og_title"),
        FieldPanel("og_description"),
        ImageChooserPanel("og_image"),
        FieldPanel("another_title"),
        FieldPanel("another_description"),
        TwitterPreviewPanel(
            [
                FieldPanel("twitter_title"),
                FieldPanel("twitter_description"),
                ImageChooserPanel("twitter_image"),
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
        MultiFieldPanel(
            [
                FieldPanel("og_title"),
                FieldPanel("og_description"),
                ImageChooserPanel("og_image"),
            ],
            heading="Facebook",
        ),
        FacebookPreviewPanelSingle(heading="Facebook Preview"),
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
    promote_panels = [
        TwitterPreviewPanelSingle(heading="Twitter Preview"),
        FacebookPreviewPanelSingle(heading="Facebook Preview"),
        GooglePreviewPanelSingle(heading="Google Preview"),
        GooglePreviewPanel(
            [FieldPanel("seo_title"), FieldPanel("search_description"),],
            heading="Google",
        ),
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
            ObjectList(promote_panels, heading="Promote"),
        ]
    )

    class Meta:
        abstract = True
