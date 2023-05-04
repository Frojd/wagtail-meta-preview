from django.test import TestCase
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils

from tests.app.models import FacebookPage
from wagtail_meta_preview import meta_settings
from wagtail_meta_preview.utils import FacebookSettings


class TestMetaPreviewFacebookAdminView(TestCase, WagtailTestUtils):
    def setUp(self):
        self.root_page = Page.objects.first()

        self.facebook_page = self.root_page.add_child(
            instance=FacebookPage(
                title="Facebook Page",
                another_title="This is another title",
                another_description="This is another description",
                og_title="This is the og title",
                og_description="This is the og description",
            )
        )

    def test_facebook_default_fallback_titles(self):
        self.facebook_page.og_title = ""
        self.facebook_page.save()

        facebook_settings = FacebookSettings(self.facebook_page)

        meta_settings.META_PREVIEW_FACEBOOK_TITLE_FIELDS = ""
        self.assertEqual(
            facebook_settings.get_defaults()["default_title"],
            "",
        )

        meta_settings.META_PREVIEW_FACEBOOK_TITLE_FIELDS = "another_title"
        self.assertEqual(
            facebook_settings.get_defaults()["default_title"],
            self.facebook_page.another_title,
        )

        meta_settings.META_PREVIEW_FACEBOOK_TITLE_FIELDS = "title,another_title"
        self.assertEqual(
            facebook_settings.get_defaults()["default_title"],
            self.facebook_page.title,
        )

        meta_settings.META_PREVIEW_FACEBOOK_TITLE_FIELDS = (
            "non_existant_field,another_title,og_title"
        )
        self.assertEqual(
            facebook_settings.get_defaults()["default_title"],
            self.facebook_page.another_title,
        )

        self.facebook_page.og_title = "New facebook title"
        self.facebook_page.save()
        meta_settings.META_PREVIEW_FACEBOOK_TITLE_FIELDS = (
            "non_existant_field,another_title,og_title"
        )
        self.assertEqual(
            facebook_settings.get_defaults()["default_title"],
            self.facebook_page.another_title,
        )

    def test_facebook_default_fallback_descriptions(self):
        self.facebook_page.og_description = ""
        self.facebook_page.save()
        facebook_settings = FacebookSettings(self.facebook_page)

        meta_settings.META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = ""
        self.assertEqual(
            facebook_settings.get_defaults()["default_description"],
            "",
        )

        meta_settings.META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = (
            "og_description,another_description"
        )
        self.assertEqual(
            facebook_settings.get_defaults()["default_description"],
            self.facebook_page.another_description,
        )

        meta_settings.META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = (
            "another_description,og_description"
        )
        self.assertEqual(
            facebook_settings.get_defaults()["default_description"],
            self.facebook_page.another_description,
        )

        meta_settings.META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = (
            "non_existant_field,another_description,og_description"
        )
        self.assertEqual(
            facebook_settings.get_defaults()["default_description"],
            self.facebook_page.another_description,
        )

        self.facebook_page.og_description = "New facebook description"
        self.facebook_page.save()

        meta_settings.META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = (
            "non_existant_field,another_description,og_description"
        )
        self.assertEqual(
            facebook_settings.get_defaults()["default_description"],
            self.facebook_page.another_description,
        )

    def test_facebook_default_without_instance(self):
        facebook_settings = FacebookSettings()

        meta_settings.META_PREVIEW_FACEBOOK_TITLE_FIELDS = "og_title,seo_title,title"
        meta_settings.META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = (
            "og_description,search_description"
        )
        meta_settings.META_PREVIEW_FACEBOOK_IMAGE_FIELDS = "og_image"

        self.assertEqual(
            facebook_settings.get_defaults(),
            {
                "title_fallback_fields": "og_title,seo_title,title",
                "description_fallback_fields": "og_description,search_description",
                "image_fallback_fields": "og_image",
                "default_title": "",
                "default_description": "",
                "default_image": "",
            },
        )
