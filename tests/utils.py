import shutil
import tempfile
from io import BytesIO

import PIL.Image
from django.core.files.images import ImageFile
from django.test import override_settings
from wagtail.images.models import Image


# Taken from wagtail.images.test.utils
def get_test_image_file(filename="test.png", colour="white", size=(640, 480)):
    f = BytesIO()
    image = PIL.Image.new("RGBA", size, colour)
    image.save(f, "PNG")
    return ImageFile(f, name=filename)


def create_image(title="Test image", size=(1600, 1200), focal_point=None):
    image = Image(title=title, file=get_test_image_file(size=size))
    if focal_point:
        x, y, width, height = focal_point
        image.focal_point_x = x
        image.focal_point_y = y
        image.focal_point_width = width
        image.focal_point_height = height
    image.save()
    return image


class TempMediaMixin:
    @classmethod
    def setUpClass(cls):
        media_root = tempfile.mkdtemp()
        cls.addClassCleanup(shutil.rmtree, media_root, ignore_errors=True)
        cls.enterClassContext(
            override_settings(
                MEDIA_ROOT=media_root,
                CACHES={
                    "default": {
                        "BACKEND": "django.core.cache.backends.dummy.DummyCache"
                    }
                },
            )
        )
        super().setUpClass()
