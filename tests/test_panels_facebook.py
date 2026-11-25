from django.test import TestCase
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils

from tests.app.models import FacebookPage
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

        with self.settings(META_PREVIEW_FACEBOOK_TITLE_FIELDS=""):
            self.assertEqual(facebook_settings.get_defaults()["default_title"], "")

        with self.settings(META_PREVIEW_FACEBOOK_TITLE_FIELDS="another_title"):
            self.assertEqual(
                facebook_settings.get_defaults()["default_title"],
                self.facebook_page.another_title,
            )

        with self.settings(META_PREVIEW_FACEBOOK_TITLE_FIELDS="title,another_title"):
            self.assertEqual(
                facebook_settings.get_defaults()["default_title"],
                self.facebook_page.title,
            )

        with self.settings(
            META_PREVIEW_FACEBOOK_TITLE_FIELDS="non_existant_field,another_title,og_title"
        ):
            self.assertEqual(
                facebook_settings.get_defaults()["default_title"],
                self.facebook_page.another_title,
            )

            self.facebook_page.og_title = "New facebook title"
            self.facebook_page.save()
            self.assertEqual(
                facebook_settings.get_defaults()["default_title"],
                self.facebook_page.another_title,
            )

    def test_facebook_default_fallback_descriptions(self):
        self.facebook_page.og_description = ""
        self.facebook_page.save()
        facebook_settings = FacebookSettings(self.facebook_page)

        with self.settings(META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS=""):
            self.assertEqual(
                facebook_settings.get_defaults()["default_description"], ""
            )

        with self.settings(
            META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS="og_description,another_description"
        ):
            self.assertEqual(
                facebook_settings.get_defaults()["default_description"],
                self.facebook_page.another_description,
            )

        with self.settings(
            META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS="another_description,og_description"
        ):
            self.assertEqual(
                facebook_settings.get_defaults()["default_description"],
                self.facebook_page.another_description,
            )

        with self.settings(
            META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS=(
                "non_existant_field,another_description,og_description"
            )
        ):
            self.assertEqual(
                facebook_settings.get_defaults()["default_description"],
                self.facebook_page.another_description,
            )

            self.facebook_page.og_description = "New facebook description"
            self.facebook_page.save()
            self.assertEqual(
                facebook_settings.get_defaults()["default_description"],
                self.facebook_page.another_description,
            )

    def test_facebook_default_without_instance(self):
        defaults = FacebookSettings().get_defaults()

        self.assertEqual(defaults["default_title"], "")
        self.assertEqual(defaults["default_description"], "")
        self.assertEqual(defaults["default_image"], "")

    def test_title_and_description_trunctation(self):
        facebook_settings = FacebookSettings(self.facebook_page)

        self.facebook_page.og_title = (
            "This title exeeds the threshold recommended for OG titles and should be "
            "capped at max length"
        )
        self.facebook_page.og_description = (
            "This description is longer then title and represents the og description "
            "field, which should be one to two sentence description of your object, "
            "property are optional but recommended."
        )
        self.facebook_page.save()

        with self.settings(
            META_PREVIEW_FACEBOOK_TITLE_FIELDS="og_title",
            META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS="og_description",
        ):
            self.assertEqual(len(facebook_settings.get_title()), 90)
            self.assertEqual(len(facebook_settings.get_description()), 160)
