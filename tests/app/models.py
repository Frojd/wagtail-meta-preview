from wagtail.core.models import Page
from wagtail_seo_preview.mixins import TwitterSeoMixin, FacebookSeoMixin, SeoMixin


class TwitterPage(TwitterSeoMixin, Page):
    pass


class FacebookPage(FacebookSeoMixin, Page):
    pass


class SeoPage(SeoMixin, Page):
    pass
