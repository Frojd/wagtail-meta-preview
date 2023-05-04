from io import BytesIO

import PIL.Image
from django.core.files.images import ImageFile
from django.test import TestCase
from wagtail.images.models import Image
from wagtail.test.utils import WagtailTestUtils

from wagtail_meta_preview.utils import get_focal


# Taken from wagtail.images.test.utils
def get_test_image_file(filename="test.png", colour="white", size=(640, 480)):
    f = BytesIO()
    image = PIL.Image.new("RGBA", size, colour)
    image.save(f, "PNG")
    return ImageFile(f, name=filename)


class TestUtils(TestCase, WagtailTestUtils):
    def setUp(self):
        self.image = Image(
            title="Test image",
            file=get_test_image_file(colour="white"),
        )

    def test_focal(self):
        self.assertEqual(get_focal(self.image), {"x": "50.00%", "y": "50.00%"})
