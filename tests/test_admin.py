from django.test import TestCase, override_settings
from django.urls import reverse

from wagtail.tests.utils import WagtailTestUtils
from wagtail.core.models import Page

from tests.app.models import TwitterPage


@override_settings(ALLOWED_HOSTS=["*"])
class TestSeoPreviewTwitterAdminView(TestCase, WagtailTestUtils):
    def setUp(self):
        self.root_page = Page.objects.first()

        self.twitter_page = self.root_page.add_child(
            instance=TwitterPage(title="Twitter Page")
        )

        self.login()

    def test_add(self):
        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "twitterpage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        edit_page = reverse("wagtailadmin_pages:edit", args=(self.twitter_page.id,))
        response = self.client.get(edit_page)
        self.assertEqual(response.status_code, 200)

    def test_twitter_panels_markup(self):
        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "twitterpage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertContains(response, "twitter-preview-panel")
        self.assertContains(response, '<fieldset class="seo-preview">')
