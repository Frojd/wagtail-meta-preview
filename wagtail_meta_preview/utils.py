import html
from typing import Literal, Union

from django.utils.html import strip_tags
from django.utils.text import Truncator

from . import meta_settings


def get_focal(img):
    # Default focal point values
    background_x = 0.5
    background_y = 0.5

    if img.focal_point_width:
        # Get point relative to image size, make sure it isn't more than 1
        background_x = min(round(img.focal_point_x / img.width, 4), 1)
        background_y = min(round(img.focal_point_y / img.height, 4), 1)

    return {"x": "{:.2%}".format(background_x), "y": "{:.2%}".format(background_y)}


class BaseSettings:
    TITLE_SETTING_NAME_DICT = {
        "GOOGLE": "META_PREVIEW_GOOGLE_TITLE_FIELDS",
        "TWITTER": "META_PREVIEW_TWITTER_TITLE_FIELDS",
        "FACEBOOK": "META_PREVIEW_FACEBOOK_TITLE_FIELDS",
    }
    DESCRIPTION_SETTING_NAME_DICT = {
        "GOOGLE": "META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS",
        "TWITTER": "META_PREVIEW_TWITTER_DESCRIPTION_FIELDS",
        "FACEBOOK": "META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS",
    }
    IMAGE_SETTING_NAME_DICT = {
        "GOOGLE": "",
        "TWITTER": "META_PREVIEW_TWITTER_IMAGE_FIELDS",
        "FACEBOOK": "META_PREVIEW_FACEBOOK_IMAGE_FIELDS",
    }

    DEFAULT_IMAGE_SETTING_NAME_DICT = {
        "GOOGLE": "",
        "TWITTER": "META_PREVIEW_TWITTER_DEFAULT_IMAGE",
        "FACEBOOK": "META_PREVIEW_FACEBOOK_DEFAULT_IMAGE",
    }

    TYPE_GOOGLE = "GOOGLE"
    TYPE_TWITTER = "TWITTER"
    TYPE_FACEBOOK = "FACEBOOK"

    TYPE = Literal["GOOGLE", "TWITTER", "FACEBOOK"]

    type: TYPE
    title_max_chars: int = -1
    description_max_chars: int = -1

    def __init__(self, instance=None):
        self.instance = instance

    def get_title(self) -> str:
        if not self.instance:
            return ""

        title_fields = getattr(
            meta_settings, self.TITLE_SETTING_NAME_DICT[self.type]
        ).split(",")
        existing_title_fields = filter(
            lambda x: hasattr(self.instance, x) and getattr(self.instance, x),
            title_fields,
        )
        try:
            title_field = next(existing_title_fields)
        except StopIteration:
            return ""

        value = getattr(self.instance, title_field) or ""
        value = strip_tags(value)
        value = html.unescape(value)

        if self.title_max_chars == -1:
            return value

        return self._get_truncated_str(value, self.title_max_chars)

    def _get_truncated_str(self, value: str, max_chars) -> str:
        return Truncator(value).chars(max_chars)

    def get_description(self):
        if not self.instance:
            return ""

        description_fields = getattr(
            meta_settings, self.DESCRIPTION_SETTING_NAME_DICT[self.type]
        ).split(",")
        existing_description_fields = filter(
            lambda x: hasattr(self.instance, x) and getattr(self.instance, x),
            description_fields,
        )
        try:
            description_field = next(existing_description_fields)
        except StopIteration:
            return ""

        value = getattr(self.instance, description_field) or ""
        value = strip_tags(value)
        value = html.unescape(value)

        if self.description_max_chars == -1:
            return value

        return self._get_truncated_str(value, self.description_max_chars)

    def get_image(self):
        if not self.instance or self.type == "GOOGLE":
            return ""

        image_fields = getattr(
            meta_settings, self.IMAGE_SETTING_NAME_DICT[self.type]
        ).split(",")
        existing_image_fields = filter(
            lambda x: hasattr(self.instance, x) and getattr(self.instance, x),
            image_fields,
        )
        try:
            image_field = next(existing_image_fields)
            image_instance = getattr(self.instance, image_field, "")
            image_url = (
                image_instance.get_rendition(
                    meta_settings.META_PREVIEW_IMAGE_DEFAULT_SIZE
                ).url
                if image_instance
                else ""
            )
            return image_url
        except StopIteration:
            default_image = getattr(
                meta_settings, self.DEFAULT_IMAGE_SETTING_NAME_DICT[self.type]
            )
            return default_image

    def get_defaults(self):
        title = self.get_title()
        description = self.get_description()
        image = self.get_image()

        return {
            "title_fallback_fields": getattr(
                meta_settings, self.TITLE_SETTING_NAME_DICT[self.type]
            ),
            "description_fallback_fields": getattr(
                meta_settings, self.DESCRIPTION_SETTING_NAME_DICT[self.type]
            ),
            "image_fallback_fields": getattr(
                meta_settings, self.IMAGE_SETTING_NAME_DICT[self.type], ""
            ),
            "default_title": title,
            "default_description": description,
            "default_image": image,
        }


class TwitterSettings(BaseSettings):
    def __init__(
        self,
        instance=None,
        title_max_chars: int = 70,
        description_max_chars: int = 200,
    ):
        self.type = self.TYPE_TWITTER
        self.title_max_chars = title_max_chars
        self.description_max_chars = description_max_chars

        super().__init__(instance)


class FacebookSettings(BaseSettings):
    def __init__(
        self,
        instance=None,
        title_max_chars: int = 90,
        description_max_chars: int = 160,
    ):
        self.type = self.TYPE_FACEBOOK
        self.title_max_chars = title_max_chars
        self.description_max_chars = description_max_chars

        super().__init__(instance)


class GoogleSettings(BaseSettings):
    def __init__(
        self,
        instance=None,
        title_max_chars: int = 70,
        description_max_chars: int = 160,
    ):
        self.type = self.TYPE_GOOGLE
        self.title_max_chars = title_max_chars
        self.description_max_chars = description_max_chars
        super().__init__(instance)
