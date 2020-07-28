from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from .mixins import TwitterModelMixin, FacebookModelMixin, MetaModelMixin


class TwitterPage(TwitterModelMixin, Page):
    pass


class FacebookPage(FacebookModelMixin, Page):
    pass


class MetaPage(MetaModelMixin, Page):
    pass
