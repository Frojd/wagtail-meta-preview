from django.conf import settings
from . import meta_settings


def get_fields(instance=None):
    twitter_settings = meta_settings.get_twitter_settings(instance)

    title_field = twitter_settings["title_field"]
    description_field = twitter_settings["description_field"]

    title_fallback_fields = twitter_settings["title_fallbacks"]
    description_fallback_fields = twitter_settings["description_fallbacks"]
    image_fallback_fields = twitter_settings["image_fallbacks"]

    title = twitter_settings["title"]
    description = twitter_settings["description"]

    image = twitter_settings["image"]

    return (
        title_field,
        description_field,
        title_fallback_fields,
        description_fallback_fields,
        image_fallback_fields,
        title,
        description,
        image,
    )


def get_twitter_defaults(instance=None):

    (
        title_field,
        description_field,
        title_fallback_fields,
        description_fallback_fields,
        image_fallback_fields,
        title,
        description,
        image,
    ) = get_fields(instance)

    if not title and instance:
        titles = title_fallback_fields.split(",")
        titles = list(filter(lambda x: hasattr(instance, x), titles))
        title_field = titles[0] if titles else "title"
        title = getattr(instance, title_field, "")
    elif not instance:
        title = ""

    if not description and instance:
        descriptions = description_fallback_fields.split(",")
        descriptions = list(filter(lambda x: hasattr(instance, x), descriptions))
        description = getattr(instance, descriptions[0]) if descriptions else ""
    elif not instance:
        description = ""

    return {
        "title_fallback_fields": title_fallback_fields,
        "description_fallback_fields": description_fallback_fields,
        "image_fallback_fields": image_fallback_fields,
        "default_title": title or instance.title if instance else title,
        "default_description": description,
        "default_image": image,
    }
