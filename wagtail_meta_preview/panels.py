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


class SinglePanel(EditHandler):
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


class TwitterPreviewPanelSingle(SinglePanel):
    def render(self):
        context = {"self": self, "is_twitter": True, "is_single": True}

        twitter_settings = utils.TwitterSettings(self.instance)
        context.update(twitter_settings.get_defaults())

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["meta-preview-panel", "twitter-preview-panel"])
        return classes


class TwitterPreviewPanel(BaseCompositeEditHandler):
    template = "wagtail_meta_preview/preview_panel.html"

    def render(self):
        twitter_settings = utils.TwitterSettings(self.instance)

        context = {"self": self, "is_twitter": True, **twitter_settings.get_defaults()}

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "twitter-preview-panel"])
        return classes


class FacebookPreviewPanel(BaseCompositeEditHandler):
    template = "wagtail_meta_preview/preview_panel.html"

    def get_defaults(self):
        return utils.get_facebook_defaults(self.instance)

    def render(self):
        facebook_settings = utils.FacebookSettings(self.instance)

        context = {
            "self": self,
            "is_facebook": True,
            **facebook_settings.get_defaults(),
        }

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "facebook-preview-panel"])
        return classes


class FacebookPreviewPanelSingle(SinglePanel):
    def render(self):
        context = {"self": self, "is_facebook": True, "is_single": True}

        facebook_settings = utils.FacebookSettings(self.instance)
        context.update(facebook_settings.get_defaults())

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["meta-preview-panel", "facebook-preview-panel"])
        return classes


class GooglePreviewPanel(BaseCompositeEditHandler):
    template = "wagtail_meta_preview/preview_panel.html"

    def render(self):
        google_settings = utils.GoogleSettings(self.instance)

        context = {
            "self": self,
            "is_google": True,
            **google_settings.get_defaults(),
        }

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "google-preview-panel"])
        return classes


class GooglePreviewPanelSingle(SinglePanel):
    def render(self):
        context = {"self": self, "is_google": True, "is_single": True}

        google_settings = utils.GoogleSettings(self.instance)
        context.update(google_settings.get_defaults())

        return mark_safe(render_to_string(self.template, context))

    def classes(self):
        classes = super().classes()
        classes.extend(["meta-preview-panel", "google-preview-panel"])
        return classes
