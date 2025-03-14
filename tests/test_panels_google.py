from django.test import TestCase
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils

from tests.app.models import MetaPage
from wagtail_meta_preview import meta_settings
from wagtail_meta_preview.utils import GoogleSettings


class TestMetaPreviewGoogleAdminView(TestCase, WagtailTestUtils):
    def setUp(self):
        self.root_page = Page.objects.first()

        self.google_page = self.root_page.add_child(
            instance=MetaPage(
                title="Google Page",
                seo_title="Google Title",
                search_description="Google Description",
                og_title="This is the og title",
                og_description="This is the og description",
            )
        )

    def test_google_default_fallback_titles(self):
        self.google_page.og_title = ""
        self.google_page.save()

        google_settings = GoogleSettings(self.google_page)

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELDS = ""
        self.assertEqual(
            google_settings.get_defaults()["default_title"],
            "",
        )

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELDS = "title,another_title"
        self.assertEqual(
            google_settings.get_defaults()["default_title"],
            self.google_page.title,
        )

        self.google_page.og_title = "New google title"
        self.google_page.save()
        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELDS = (
            "non_existant_field,another_title,og_title"
        )
        self.assertEqual(
            google_settings.get_defaults()["default_title"],
            self.google_page.og_title,
        )

    def test_google_default_fallback_descriptions(self):
        self.google_page.og_description = ""
        self.google_page.save()
        google_settings = GoogleSettings(self.google_page)

        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = ""
        self.assertEqual(
            google_settings.get_defaults()["default_description"],
            "",
        )

        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = (
            "og_description,another_description"
        )
        self.assertEqual(
            google_settings.get_defaults()["default_description"],
            self.google_page.og_description,
        )

        self.google_page.og_description = "New google description"
        self.google_page.save()

        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = (
            "non_existant_field,another_description,og_description"
        )
        self.assertEqual(
            google_settings.get_defaults()["default_description"],
            self.google_page.og_description,
        )

    def test_google_default_without_instance(self):
        google_settings = GoogleSettings()

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELDS = "seo_title,title"
        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = "search_description"

        self.assertEqual(
            google_settings.get_defaults(),
            {
                "title_fallback_fields": "seo_title,title",
                "description_fallback_fields": "search_description",
                "image_fallback_fields": "",
                "default_title": "",
                "default_description": "",
                "default_image": "",
            },
        )

    def test_title_and_description_trunctation(self):
        google_settings = GoogleSettings(self.google_page)

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELDS = "seo_title"
        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = "search_description"

        self.google_page.seo_title = "This title exeeds the threshold recommended for twitter titles and should be capped at max length"
        self.google_page.search_description = "This text is exactly 200 characters long, designed to convey the idea of counting characters. The goal is to show how we can be precise with word choices, making sure to reach the exact character count! Everything outside this is capped."
        self.google_page.save()

        self.assertEqual(len(google_settings.get_title()), 70)
        self.assertEqual(len(google_settings.get_description()), 160)

    def test_that_html_tags_are_stripped(self):
        google_settings = GoogleSettings(self.google_page)

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELDS = "seo_title"
        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = "search_description"

        self.google_page.seo_title = "<strong>Hello world</strong> and <em>earth</em>"
        self.google_page.search_description = "<p>My description</p>"
        self.google_page.save()

        self.assertEqual(google_settings.get_title(), "Hello world and earth")
        self.assertEqual(google_settings.get_description(), "My description")

    def test_that_html_chars_are_decoded(self):
        google_settings = GoogleSettings(self.google_page)

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELDS = "seo_title"
        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = "search_description"

        self.google_page.seo_title = "Here you&#x27;ll find everything you need"
        self.google_page.search_description = (
            "Here you&#x27;ll find everything you need"
        )
        self.google_page.save()

        self.assertEqual(
            google_settings.get_title(), "Here you'll find everything you need"
        )
        self.assertEqual(
            google_settings.get_description(), "Here you'll find everything you need"
        )
