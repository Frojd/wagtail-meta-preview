from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from wagtail.images.models import Rendition
from wagtail.test.utils import WagtailTestUtils

from tests.utils import TempMediaMixin, create_image


class TestGetImageRendition(TempMediaMixin, TestCase, WagtailTestUtils):
    def setUp(self):
        self.image = create_image(size=(1600, 1200), focal_point=(400, 900, 100, 100))
        self.url = reverse("get_image_rendition", args=(self.image.pk,))

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(self.url)

        self.assertRedirects(
            response,
            f"{reverse('wagtailadmin_login')}?next={self.url}",
            fetch_redirect_response=False,
        )

    def test_admin_user_without_image_permission_is_forbidden(self):
        user = get_user_model().objects.create_user(
            username="editor", password="password"
        )
        user.user_permissions.add(
            Permission.objects.get(
                content_type__app_label="wagtailadmin", codename="access_admin"
            )
        )
        self.client.force_login(user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
        self.assertFalse(Rendition.objects.exists())

    def test_returns_rendition_and_focal_point(self):
        self.login()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        rendition = Rendition.objects.get(image=self.image)
        self.assertEqual(rendition.filter_spec, "fill-1200x628")
        self.assertEqual((rendition.width, rendition.height), (1200, 628))
        self.assertEqual(
            response.json(),
            {"src": rendition.url, "focal": {"x": "25.00%", "y": "75.00%"}},
        )
