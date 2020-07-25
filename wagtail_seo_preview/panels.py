from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from wagtail.admin.edit_handlers import BaseCompositeEditHandler
from wagtail.admin.edit_handlers import FieldPanel


class SeoTitlePanel(FieldPanel):
    def classes(self):
        classes = super().classes()
        classes.append("seo-preview-title")
        return classes


class SeoDescriptionPanel(FieldPanel):
    def classes(self):
        classes = super().classes()
        classes.append("seo-preview-description")
        return classes


class TwitterPreviewPanel(BaseCompositeEditHandler):
    template = "wagtail_seo_preview/preview_panel.html"

    def render(self):
        if self.instance:
            defaults = {
                "default_title": self.instance.twitter_title or self.instance.title,
                "default_description": self.instance.twitter_description,
            }

        context = {"self": self, "is_twitter": True, **defaults}

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "seo-preview-panel", "twitter-preview-panel"])
        return classes
