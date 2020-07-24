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
        classes.append("seo-preview-title")
        return classes


class TwitterPreviewPanel(BaseCompositeEditHandler):
    template = "wagtail_seo_preview/preview_panel.html"

    def classes(self):
        classes = super().classes()
        classes.append("multi-field twitter-preview-panel")
        return classes
