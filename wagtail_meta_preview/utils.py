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
    def __init__(self, instance=None):
        self.instance = instance

    def get_title(self):
        title_field = getattr(meta_settings, f"META_PREVIEW_{self.type}_TITLE_FIELD")
        title = getattr(self.instance, title_field, "")

        if not title and self.instance:
            titles = getattr(
                meta_settings, f"META_PREVIEW_{self.type}_TITLE_FALLBACK"
            ).split(",")
            titles = list(filter(lambda x: hasattr(self.instance, x), titles))
            title_field = titles[0] if titles else "title"
            title = getattr(self.instance, title_field, "")

        return title or (self.instance.title if self.instance else "")

    def get_description(self):
        description_field = getattr(
            meta_settings, f"META_PREVIEW_{self.type}_DESCRIPTION_FIELD"
        )
        description = getattr(self.instance, description_field, "")

        if not description and self.instance:
            descriptions = getattr(
                meta_settings, f"META_PREVIEW_{self.type}_DESCRIPTION_FALLBACK"
            ).split(",")
            descriptions = list(
                filter(lambda x: hasattr(self.instance, x), descriptions)
            )
            description = (
                getattr(self.instance, descriptions[0]) if descriptions else ""
            )

        return description

    def get_image(self):
        image = ""

        if self.instance:
            image_instance = getattr(
                self.instance,
                getattr(meta_settings, f"META_PREVIEW_{self.type}_IMAGE_FIELD"),
            )
            image = (
                image_instance.get_rendition(meta_settings.IMAGE_DEFAULT_SIZE).url
                if image_instance
                else ""
            )

        return image

    def get_defaults(self):
        title = self.get_title()
        description = self.get_description()
        image = self.get_image()

        return {
            "title_fallback_fields": getattr(
                meta_settings, f"META_PREVIEW_{self.type}_TITLE_FALLBACK"
            ),
            "description_fallback_fields": getattr(
                meta_settings, f"META_PREVIEW_{self.type}_DESCRIPTION_FALLBACK"
            ),
            "image_fallback_fields": getattr(
                meta_settings, f"META_PREVIEW_{self.type}_IMAGE_FALLBACK"
            ),
            "default_title": title,
            "default_description": description,
            "default_image": image,
        }


class TwitterSettings(BaseSettings):
    def __init__(self, instance=None):
        self.type = "TWITTER"
        super().__init__(instance)


class FacebookSettings(BaseSettings):
    def __init__(self, instance=None):
        self.type = "FACEBOOK"
        super().__init__(instance)
