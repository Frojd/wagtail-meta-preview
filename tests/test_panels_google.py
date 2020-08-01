from django.test import TestCase

from wagtail.tests.utils import WagtailTestUtils
from wagtail.core.models import Page

from tests.app.models import MetaPage
from wagtail_meta_preview.utils import GoogleSettings
from wagtail_meta_preview import meta_settings


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

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FALLBACK = ""
        meta_settings.META_PREVIEW_GOOGLE_TITLE_FIELD = ""
        self.assertEqual(
            google_settings.get_defaults()["default_title"], self.google_page.title,
        )

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FALLBACK = "title,another_title"
        self.assertEqual(
            google_settings.get_defaults()["default_title"], self.google_page.title,
        )

        self.google_page.og_title = "New google title"
        self.google_page.save()
        meta_settings.META_PREVIEW_GOOGLE_TITLE_FALLBACK = (
            "non_existant_field,another_title,og_title"
        )
        self.assertEqual(
            google_settings.get_defaults()["default_title"], self.google_page.og_title,
        )

    def test_google_default_fallback_descriptions(self):
        self.google_page.og_description = ""
        self.google_page.save()
        google_settings = GoogleSettings(self.google_page)

        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FALLBACK = ""
        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FIELD = ""
        self.assertEqual(
            google_settings.get_defaults()["default_description"], "",
        )

        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FALLBACK = (
            "og_description,another_description"
        )
        self.assertEqual(
            google_settings.get_defaults()["default_description"],
            self.google_page.og_description,
        )

        self.google_page.og_description = "New google description"
        self.google_page.save()

        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FALLBACK = (
            "non_existant_field,another_description,og_description"
        )
        self.assertEqual(
            google_settings.get_defaults()["default_description"],
            self.google_page.og_description,
        )

    def test_google_default_without_instance(self):
        google_settings = GoogleSettings()

        meta_settings.META_PREVIEW_GOOGLE_TITLE_FALLBACK = "title"
        meta_settings.META_PREVIEW_GOOGLE_DESCRIPTION_FALLBACK = "search_description"
        meta_settings.META_PREVIEW_GOOGLE_IMAGE_FALLBACK = ""

        self.assertEqual(
            google_settings.get_defaults(),
            {
                "title_fallback_fields": "title",
                "description_fallback_fields": "search_description",
                "image_fallback_fields": "",
                "default_title": "",
                "default_description": "",
                "default_image": "",
            },
        )
