from django.test import TestCase, override_settings
from django.urls import reverse
from wagtail.images.models import Rendition
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils
from wagtail.users.models import UserProfile

from tests.app.models import FacebookPage, MetaPage, TwitterPage
from tests.utils import TempMediaMixin, create_image


@override_settings(ALLOWED_HOSTS=["*"])
class TestMetaPreviewAdminView(TempMediaMixin, TestCase, WagtailTestUtils):
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

        self.user = self.login()

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

    def test_previews_follow_admin_language(self):
        profile = UserProfile.get_for_user(self.user)
        profile.preferred_language = "sv"
        profile.save()

        add_page = reverse(
            "wagtailadmin_pages:add", args=("app", "metapage", self.root_page.id)
        )
        response = self.client.get(add_page)
        self.assertContains(response, "Förhandsvisning för Facebook")
        self.assertContains(response, "Förhandsvisning för Twitter")
        self.assertContains(response, "Förhandsvisning för Google")
        self.assertContains(
            response,
            '<div class="meta-facebook-author-name">Facebook-användare</div>',
        )
        self.assertContains(response, "1 tim")
        self.assertContains(response, "Från site.com")
        self.assertContains(response, "Webbplatsens namn")
        self.assertContains(response, "Twitter-användare")
        self.assertContains(response, "Kolla in den här grymma artikeln!")

    def test_google_default_values(self):
        meta_page = self.root_page.add_child(
            instance=MetaPage(
                title="Meta Page",
                seo_title="Epic Google Title",
                search_description="Epic Google Description",
                og_title="Epic Facebook Title",
                og_description="Epic Facebook Description",
                twitter_title="Epic Twitter Title",
                twitter_description="Epic Twitter Description",
            )
        )
        edit_page = reverse("wagtailadmin_pages:edit", args=(meta_page.id,))
        response = self.client.get(edit_page)
        self.assertContains(response, "google-preview-panel")
        self.assertContains(response, 'title">Epic Google Title</h2>', count=2)
        self.assertContains(
            response, 'description">Epic Google Description</div>', count=2
        )

    def test_default_image_in_preview(self):
        image = create_image()
        self.twitter_page.og_image = image
        self.twitter_page.save()

        edit_page = reverse("wagtailadmin_pages:edit", args=(self.twitter_page.id,))
        response = self.client.get(edit_page)

        rendition = Rendition.objects.get(image=image, filter_spec="fill-1200x628")
        self.assertContains(response, f"background-image: url('{rendition.url}')")
