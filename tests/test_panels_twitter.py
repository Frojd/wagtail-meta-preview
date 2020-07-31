from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse

from wagtail.tests.utils import WagtailTestUtils
from wagtail.core.models import Page

from tests.app.models import TwitterPage
from wagtail_meta_preview.utils import get_twitter_defaults
from wagtail_meta_preview import meta_settings


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

    def test_twitter_default_fallback_descriptions(self):
        self.twitter_page.twitter_description = ""
        self.twitter_page.save()

        with override_settings(META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK=""):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_description"], "",
            )

        with override_settings(
            META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK="og_description,another_description"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_description"],
                self.twitter_page.og_description,
            )

        with override_settings(
            META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK="another_description,og_description"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_description"],
                self.twitter_page.another_description,
            )

        with override_settings(
            META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK="non_existant_field,another_description,og_description"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_description"],
                self.twitter_page.another_description,
            )

        self.twitter_page.twitter_description = "New twitter description"
        self.twitter_page.save()
        with override_settings(
            META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK="non_existant_field,another_description,og_description"
        ):
            self.assertEqual(
                get_twitter_defaults(self.twitter_page)["default_description"],
                self.twitter_page.twitter_description,
            )

    def test_twitter_default_without_instance(self):
        title_fallback_fields = getattr(
            settings,
            "META_PREVIEW_TWITTER_TITLE_FALLBACK",
            meta_settings.META_PREVIEW_TWITTER_TITLE_FALLBACK,
        )
        description_fallback_fields = getattr(
            settings,
            "META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK",
            meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK,
        )
        image_fallback_fields = getattr(
            settings,
            "META_PREVIEW_TWITTER_IMAGE_FALLBACK",
            meta_settings.META_PREVIEW_TWITTER_IMAGE_FALLBACK,
        )

        self.assertEqual(
            get_twitter_defaults(),
            {
                "title_fallback_fields": title_fallback_fields,
                "description_fallback_fields": description_fallback_fields,
                "image_fallback_fields": image_fallback_fields,
                "default_title": "",
                "default_description": "",
                "default_image": "",
            },
        )
