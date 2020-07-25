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
        return mark_safe(
            render_to_string(self.template, {"self": self, "is_twitter": True})
        )

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "seo-preview-panel", "twitter-preview-panel"])
        return classes
