from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from .mixins import TwitterModelMixin, FacebookModelMixin, MetaModelMixin


class TwitterPage(TwitterModelMixin, Page):
    og_title = models.CharField(blank=True, max_length=100)
    og_description = models.CharField(blank=True, max_length=100)
    another_title = models.CharField(blank=True, max_length=100)
    another_description = models.CharField(blank=True, max_length=100)


class FacebookPage(FacebookModelMixin, Page):
    pass


class MetaPage(MetaModelMixin, Page):
    pass
