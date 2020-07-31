from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from wagtail.admin.edit_handlers import BaseCompositeEditHandler, EditHandler
from wagtail.admin.edit_handlers import FieldPanel

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


class TwitterPreviewPanelSingle(EditHandler):
    def __init__(
        self,
        template="wagtail_meta_preview/preview_panel.html",
        heading="",
        classname="",
    ):
        super().__init__(heading=heading, classname=classname)
        self.template = template

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        del kwargs["help_text"]
        kwargs.update(template=self.template,)
        return kwargs

    def render(self):
        context = {"self": self, "is_twitter": True, "is_single": True}

        context.update(utils.get_twitter_defaults(self.instance))

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["meta-preview-panel", "twitter-preview-panel"])
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
