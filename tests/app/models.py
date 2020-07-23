from wagtail.core.models import Page
from wagtail_seo_preview.mixins import TwitterModelMixin, FacebookModelMixin, SeoModelMixin
from wagtail.admin.edit_handlers import FieldPanel


class TwitterPage(TwitterModelMixin, Page):
    pass


class FacebookPage(FacebookModelMixin, Page):
    pass


class SeoPage(SeoModelMixin, Page):
    pass
