from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from wagtail.admin.edit_handlers import BaseCompositeEditHandler
from wagtail.admin.edit_handlers import FieldPanel


class SeoTitlePanel(FieldPanel):
    def classes(self):
        classes = super().classes()
        classes.append("meta-preview-title")
        return classes


class SeoDescriptionPanel(FieldPanel):
    def classes(self):
        classes = super().classes()
        classes.append("meta-preview-description")
        return classes


class TwitterPreviewPanel(BaseCompositeEditHandler):
    template = "wagtail_meta_preview/preview_panel.html"

    def render(self):
        defaults = {}

        if self.instance:
            defaults = {
                "title_fallback_fields": settings.TWITTER_PREVIEW_TITLE_FALLBACK_FIELD,
                "description_fallback_fields": settings.DESCRIPTION_PREVIEW_TITLE_FALLBACK_FIELD,
                "default_title": self.instance.twitter_title or self.instance.title,
                "default_description": self.instance.twitter_description,
            }

        context = {"self": self, "is_twitter": True, **defaults}

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "twitter-preview-panel"])
        return classes
