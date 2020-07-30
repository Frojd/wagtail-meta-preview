from django.conf import settings

META_PREVIEW_TWITTER_TITLE_FALLBACK = "title"
META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK = "search_description"
META_PREVIEW_TWITTER_IMAGE_FALLBACK = ""
META_PREVIEW_TWITTER_TITLE_FIELD = "twitter_title"
META_PREVIEW_TWITTER_DESCRIPTION_FIELD = "twitter_description"
META_PREVIEW_TWITTER_IMAGE_FIELD = "twitter_image"
META_PREVIEW_TWITTER_DEFAULT_IMAGE_FUNCTION = ""

IMAGE_DEFAULT_SIZE = "fill-1200x628"


def get_twitter_settings(instance=None):
    title_field = getattr(
        settings, "META_PREVIEW_TWITTER_TITLE_FIELD", META_PREVIEW_TWITTER_TITLE_FIELD,
    )

    description_field = getattr(
        settings,
        "META_PREVIEW_TWITTER_DESCRIPTION_FIELD",
        META_PREVIEW_TWITTER_DESCRIPTION_FIELD,
    )

    image_field = getattr(
        settings, "META_PREVIEW_TWITTER_IMAGE_FIELD", META_PREVIEW_TWITTER_IMAGE_FIELD,
    )

    title_fallback_fields = getattr(
        settings,
        "META_PREVIEW_TWITTER_TITLE_FALLBACK",
        META_PREVIEW_TWITTER_TITLE_FALLBACK,
    )

    description_fallback_fields = getattr(
        settings,
        "META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK",
        META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK,
    )

    image_fallback_fields = getattr(
        settings,
        "META_PREVIEW_TWITTER_IMAGE_FALLBACK",
        META_PREVIEW_TWITTER_IMAGE_FALLBACK,
    )

    title = getattr(instance, title_field, META_PREVIEW_TWITTER_TITLE_FIELD,)
    description = getattr(
        instance, description_field, META_PREVIEW_TWITTER_DESCRIPTION_FIELD,
    )

    image = ""
    image_instance = getattr(instance, image_field)
    if instance and image_instance:
        image = image_instance.get_rendition(IMAGE_DEFAULT_SIZE).url

    return {
        "title": title,
        "description": description,
        "image": image,
        "title_field": title_field,
        "description_field": description_field,
        "title_fallbacks": title_fallback_fields,
        "description_fallbacks": description_fallback_fields,
        "image_fallbacks": image_fallback_fields,
    }
