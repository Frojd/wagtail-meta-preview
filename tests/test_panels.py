from django.test import TestCase, override_settings
from django.urls import reverse

from wagtail.tests.utils import WagtailTestUtils
from wagtail.core.models import Page

from tests.app.models import TwitterPage
from wagtail_meta_preview.utils import get_twitter_defaults


class TestMetaPreviewTwitterAdminView(TestCase, WagtailTestUtils):
    def setUp(self):
        self.root_page = Page.objects.first()

        self.twitter_page = self.root_page.add_child(
            instance=TwitterPage(
                title="Twitter Page",
                twitter_title="Epic Twitter Title",
                twitter_description="Epic Twitter Description",
                another_title="This is another title",
                another_description="This is another description",
                og_title="This is the og title",
                og_description="This is the og description",
            )
        )

    def test_twitter_fallback_titles(self):
        self.twitter_page.twitter_title = ""
        self.twitter_page.save()

        with override_settings(META_PREVIEW_TWITTER_TITLE_FALLBACK=""):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_title"],
                self.twitter_page.title,
            )

        with override_settings(
            META_PREVIEW_TWITTER_TITLE_FALLBACK="og_title,another_title"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_title"],
                self.twitter_page.og_title,
            )

        with override_settings(
            META_PREVIEW_TWITTER_TITLE_FALLBACK="another_title,og_title"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_title"],
                self.twitter_page.another_title,
            )

        with override_settings(
            META_PREVIEW_TWITTER_TITLE_FALLBACK="non_existant_field,another_title,og_title"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_title"],
                self.twitter_page.another_title,
            )

        self.twitter_page.twitter_title = "New twitter title"
        self.twitter_page.save()
        with override_settings(
            META_PREVIEW_TWITTER_TITLE_FALLBACK="non_existant_field,another_title,og_title"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_title"],
                self.twitter_page.twitter_title,
            )
