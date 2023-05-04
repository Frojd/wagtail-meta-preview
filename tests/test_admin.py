from django.test import TestCase, override_settings
from django.urls import reverse
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils

from tests.app.models import FacebookPage, TwitterPage


@override_settings(ALLOWED_HOSTS=["*"])
class TestMetaPreviewAdminView(TestCase, WagtailTestUtils):
    def setUp(self):
        self.root_page = Page.objects.first()

        self.twitter_page = self.root_page.add_child(
            instance=TwitterPage(
                title="Twitter Page",
                twitter_title="Epic Twitter Title",
                twitter_description="Epic Twitter Description",
            )
        )

        self.facebook_page = self.root_page.add_child(
            instance=FacebookPage(
                title="Facebook Page",
                og_title="Epic Facebook Title",
                og_description="Epic Facebook Description",
            )
        )

        self.login()

    def test_add(self):
        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "twitterpage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertEqual(response.status_code, 200)

        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "facebookpage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        edit_page = reverse("wagtailadmin_pages:edit", args=(self.twitter_page.id,))
        response = self.client.get(edit_page)
        self.assertEqual(response.status_code, 200)

        edit_page = reverse("wagtailadmin_pages:edit", args=(self.facebook_page.id,))
        response = self.client.get(edit_page)
        self.assertEqual(response.status_code, 200)

    def test_twitter_panels_markup(self):
        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "twitterpage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertContains(response, "twitter-preview-panel")
        self.assertContains(response, '<div class="meta-preview">')

    def test_twitter_default_values(self):
        edit_page = reverse("wagtailadmin_pages:edit", args=(self.twitter_page.id,))
        response = self.client.get(edit_page)
        self.assertContains(response, 'title">Epic Twitter Title</h2>')
        self.assertContains(response, 'description">Epic Twitter Description</div>')

    def test_facebook_panels_markup(self):
        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "facebookpage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertContains(response, "facebook-preview-panel")
        self.assertContains(response, '<div class="meta-preview meta-preview--single">')

    def test_facebook_default_values(self):
        edit_page = reverse("wagtailadmin_pages:edit", args=(self.facebook_page.id,))
        response = self.client.get(edit_page)
        self.assertContains(response, 'title">Epic Facebook Title</h2>')
        self.assertContains(response, 'description">Epic Facebook Description</div>')

    def test_single_panel_markup(self):
        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "metapage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertContains(response, '<div class="meta-preview meta-preview--single">')
