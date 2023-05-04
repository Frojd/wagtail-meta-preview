from django.test import TestCase
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils

from tests.app.models import TwitterPage
from wagtail_meta_preview import meta_settings
from wagtail_meta_preview.utils import TwitterSettings


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

    def test_twitter_default_fallback_titles(self):
        self.twitter_page.twitter_title = ""
        self.twitter_page.save()
        twitter_settings = TwitterSettings(self.twitter_page)

        meta_settings.META_PREVIEW_TWITTER_TITLE_FIELDS = ""
        self.assertEqual(
            twitter_settings.get_defaults()["default_title"],
            "",
        )

        meta_settings.META_PREVIEW_TWITTER_TITLE_FIELDS = "og_title,another_title"
        self.assertEqual(
            twitter_settings.get_defaults()["default_title"],
            self.twitter_page.og_title,
        )

        meta_settings.META_PREVIEW_TWITTER_TITLE_FIELDS = "another_title,og_title"
        self.assertEqual(
            twitter_settings.get_defaults()["default_title"],
            self.twitter_page.another_title,
        )

        meta_settings.META_PREVIEW_TWITTER_TITLE_FIELDS = (
            "non_existant_field,another_title,og_title"
        )
        self.assertEqual(
            twitter_settings.get_defaults()["default_title"],
            self.twitter_page.another_title,
        )

        self.twitter_page.twitter_title = "New twitter title"
        self.twitter_page.save()
        meta_settings.META_PREVIEW_TWITTER_TITLE_FIELDS = (
            "non_existant_field,another_title,og_title"
        )
        self.assertEqual(
            twitter_settings.get_defaults()["default_title"],
            self.twitter_page.another_title,
        )

    def test_twitter_default_fallback_descriptions(self):
        self.twitter_page.twitter_description = ""
        self.twitter_page.save()
        twitter_settings = TwitterSettings(self.twitter_page)

        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = ""
        self.assertEqual(
            twitter_settings.get_defaults()["default_description"],
            "",
        )

        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = (
            "og_description,another_description"
        )
        self.assertEqual(
            twitter_settings.get_defaults()["default_description"],
            self.twitter_page.og_description,
        )

        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = (
            "another_description,og_description"
        )
        self.assertEqual(
            twitter_settings.get_defaults()["default_description"],
            self.twitter_page.another_description,
        )

        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = (
            "non_existant_field,another_description,og_description"
        )
        self.assertEqual(
            twitter_settings.get_defaults()["default_description"],
            self.twitter_page.another_description,
        )

        self.twitter_page.twitter_description = "New twitter description"
        self.twitter_page.save()

        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = (
            "non_existant_field,another_description,og_description"
        )
        self.assertEqual(
            twitter_settings.get_defaults()["default_description"],
            self.twitter_page.another_description,
        )

    def test_twitter_default_without_instance(self):
        twitter_settings = TwitterSettings()

        meta_settings.META_PREVIEW_TWITTER_TITLE_FIELDS = "title"
        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = "search_description"
        meta_settings.META_PREVIEW_TWITTER_IMAGE_FIELDS = ""

        self.assertEqual(
            twitter_settings.get_defaults(),
            {
                "title_fallback_fields": "title",
                "description_fallback_fields": "search_description",
                "image_fallback_fields": "",
                "default_title": "",
                "default_description": "",
                "default_image": "",
            },
        )
