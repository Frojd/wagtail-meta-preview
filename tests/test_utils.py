from django.test import TestCase
from wagtail.images.models import Rendition
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils

from tests.app.models import FacebookPage, MetaPage, TwitterPage
from tests.utils import TempMediaMixin, create_image
from wagtail_meta_preview.utils import (
    FacebookSettings,
    GoogleSettings,
    TwitterSettings,
    get_focal,
)


class TestGetFocal(TempMediaMixin, TestCase, WagtailTestUtils):
    def test_without_focal_point_is_centered(self):
        image = create_image()
        self.assertEqual(get_focal(image), {"x": "50.00%", "y": "50.00%"})

    def test_focal_point_relative_to_image_size(self):
        image = create_image(size=(640, 480), focal_point=(160, 360, 100, 100))
        self.assertEqual(get_focal(image), {"x": "25.00%", "y": "75.00%"})

    def test_focal_point_outside_image_is_capped(self):
        image = create_image(size=(640, 480), focal_point=(800, 600, 100, 100))
        self.assertEqual(get_focal(image), {"x": "100.00%", "y": "100.00%"})


class TestGetImage(TempMediaMixin, TestCase, WagtailTestUtils):
    def setUp(self):
        self.root_page = Page.objects.first()
        self.first_image = create_image(title="First")
        self.second_image = create_image(title="Second")

    def get_rendition(self, image):
        return Rendition.objects.get(image=image, filter_spec="fill-1200x628")

    def test_returns_rendition_of_first_set_image_field(self):
        page = self.root_page.add_child(
            instance=TwitterPage(
                title="Twitter",
                twitter_image=self.first_image,
                og_image=self.second_image,
            )
        )

        url = TwitterSettings(page).get_image()

        rendition = self.get_rendition(self.first_image)
        self.assertEqual(url, rendition.url)
        self.assertEqual((rendition.width, rendition.height), (1200, 628))
        self.assertFalse(
            Rendition.objects.filter(image=self.second_image).exists(),
        )

    def test_skips_empty_image_field(self):
        page = self.root_page.add_child(
            instance=TwitterPage(title="Twitter", og_image=self.second_image)
        )

        url = TwitterSettings(page).get_image()

        self.assertEqual(url, self.get_rendition(self.second_image).url)

    def test_respects_image_size_setting(self):
        page = self.root_page.add_child(
            instance=FacebookPage(title="Facebook", og_image=self.first_image)
        )

        with self.settings(META_PREVIEW_IMAGE_DEFAULT_SIZE="fill-100x50"):
            url = FacebookSettings(page).get_image()

        rendition = Rendition.objects.get(image=self.first_image)
        self.assertEqual(url, rendition.url)
        self.assertEqual((rendition.width, rendition.height), (100, 50))

    def test_falls_back_to_default_image_per_type(self):
        page = self.root_page.add_child(instance=MetaPage(title="Meta"))

        with self.settings(
            META_PREVIEW_TWITTER_DEFAULT_IMAGE="/static/twitter.png",
            META_PREVIEW_FACEBOOK_DEFAULT_IMAGE="/static/facebook.png",
        ):
            self.assertEqual(TwitterSettings(page).get_image(), "/static/twitter.png")
            self.assertEqual(FacebookSettings(page).get_image(), "/static/facebook.png")

    def test_google_has_no_image(self):
        page = self.root_page.add_child(
            instance=MetaPage(title="Meta", og_image=self.first_image)
        )

        self.assertEqual(GoogleSettings(page).get_image(), "")
        self.assertFalse(Rendition.objects.exists())
