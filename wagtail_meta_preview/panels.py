from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from wagtail.admin.edit_handlers import BaseCompositeEditHandler
from wagtail.admin.edit_handlers import FieldPanel

from . import meta_settings


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
        title_fallback_fields = meta_settings.META_PREVIEW_TWITTER_TITLE_FALLBACK
        description_fallback_fields = (
            meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK
        )
        title = getattr(self.instance, meta_settings.META_PREVIEW_TWITTER_TITLE_FIELD)
        description = getattr(
            self.instance, meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELD
        )

        if not title and self.instance:
            try:
                titles = title_fallback_fields.split(",")
                titles = filter(lambda x: hasattr(self.instance, x), titles)
                title = next(titles)
            except IndexError:
                pass

        if not description and self.instance:
            try:
                descriptions = title_fallback_fields.split(",")
                descriptions = filter(lambda x: hasattr(self.instance, x), descriptions)
                description = next(descriptions)
            except IndexError:
                pass

        return {
            "title_fallback_fields": title_fallback_fields,
            "description_fallback_fields": description_fallback_fields,
            "default_title": title,
            "default_description": description,
        }

    def render(self):
        defaults = self.get_defaults()

        context = {"self": self, "is_twitter": True, **defaults}

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "twitter-preview-panel"])
        return classes
