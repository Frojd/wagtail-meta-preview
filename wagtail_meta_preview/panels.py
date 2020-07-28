from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from wagtail.admin.edit_handlers import BaseCompositeEditHandler
from wagtail.admin.edit_handlers import FieldPanel

from . import meta_settings
from . import utils


class MetaTitlePanel(FieldPanel):
    def classes(self):
        classes = super().classes()
        classes.append("meta-preview-title")
        return classes


class MetaDescriptionPanel(FieldPanel):
    def classes(self):
        classes = super().classes()
        classes.append("meta-preview-description")
        return classes


class TwitterPreviewPanel(BaseCompositeEditHandler):
    template = "wagtail_meta_preview/preview_panel.html"

    def get_defaults(self):
        return utils.get_twitter_defaults(self.instance)

    def render(self):
        defaults = self.get_defaults()

        context = {"self": self, "is_twitter": True, **defaults}

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "twitter-preview-panel"])
        return classes
