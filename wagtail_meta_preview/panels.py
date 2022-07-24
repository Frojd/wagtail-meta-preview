from wagtail.admin.panels import Panel, PanelGroup

from . import utils


class TwitterPreviewPanel(Panel):
    class BoundPanel(Panel.BoundPanel):
        template_name = "wagtail_meta_preview/preview_panel.html"

        def get_context_data(self, parent_context=None):
            twitter_settings = utils.FacebookSettings(self.instance)

            context = super().get_context_data(parent_context)

            context = {
                **context,
                "is_twitter": True,
                "is_single": True,
                **twitter_settings.get_defaults(),
            }

            return context

    def classes(self):
        classes = super().classes()
        classes.extend(["meta-preview-panel", "twitter-preview-panel"])
        return classes


class TwitterFieldPreviewPanel(PanelGroup):
    class BoundPanel(PanelGroup.BoundPanel):
        template_name = "wagtail_meta_preview/preview_panel.html"

        def get_context_data(self, parent_context=None):
            google_settings = utils.TwitterSettings(self.instance)

            context = super().get_context_data(parent_context)

            context = {
                **context,
                "is_twitter": True,
                **google_settings.get_defaults(),
            }

            return context

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "twitter-preview-panel"])
        return classes


class FacebookFieldPreviewPanel(PanelGroup):
    class BoundPanel(PanelGroup.BoundPanel):
        template_name = "wagtail_meta_preview/preview_panel.html"

        def get_context_data(self, parent_context=None):
            facebook_settings = utils.FacebookSettings(self.instance)

            context = super().get_context_data(parent_context)

            context = {
                **context,
                "is_facebook": True,
                **facebook_settings.get_defaults(),
            }

            return context

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "facebook-preview-panel"])
        return classes


class FacebookPreviewPanel(Panel):
    class BoundPanel(Panel.BoundPanel):
        template_name = "wagtail_meta_preview/preview_panel.html"

        def get_context_data(self, parent_context=None):
            facebook_settings = utils.FacebookSettings(self.instance)

            context = super().get_context_data(parent_context)

            context = {
                **context,
                "is_facebook": True,
                "is_single": True,
                **facebook_settings.get_defaults(),
            }

            return context

    def classes(self):
        classes = super().classes()
        classes.extend(["meta-preview-panel", "facebook-preview-panel"])
        return classes


class GoogleFieldPreviewPanel(PanelGroup):
    class BoundPanel(PanelGroup.BoundPanel):
        template_name = "wagtail_meta_preview/preview_panel.html"

        def get_context_data(self, parent_context=None):
            google_settings = utils.GoogleSettings(self.instance)

            context = super().get_context_data(parent_context)

            context = {
                **context,
                "is_google": True,
                **google_settings.get_defaults(),
            }

            return context

    def classes(self):
        classes = super().classes()
        classes.extend(["multi-field", "meta-preview-panel", "google-preview-panel"])
        return classes


class GooglePreviewPanel(Panel):
    class BoundPanel(Panel.BoundPanel):
        template_name = "wagtail_meta_preview/preview_panel.html"

        def get_context_data(self, parent_context=None):
            google_settings = utils.GoogleSettings(self.instance)

            context = super().get_context_data(parent_context)

            context = {
                **context,
                "is_google": True,
                "is_single": True,
                **google_settings.get_defaults(),
            }

            return context

    def classes(self):
        classes = super().classes()
        classes.extend(["meta-preview-panel", "google-preview-panel"])
        return classes
