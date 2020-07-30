from django.conf import settings
from . import meta_settings


def get_twitter_defaults(instance=None):
    twitter_field = getattr(
        settings,
        "META_PREVIEW_TWITTER_TITLE_FIELD",
        meta_settings.META_PREVIEW_TWITTER_TITLE_FIELD,
    )
    description_field = getattr(
        settings,
        "META_PREVIEW_TWITTER_DESCRIPTION_FIELD",
        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELD,
    )

    title_fallback_fields = getattr(
        settings,
        "META_PREVIEW_TWITTER_TITLE_FALLBACK",
        meta_settings.META_PREVIEW_TWITTER_TITLE_FALLBACK,
    )
    description_fallback_fields = getattr(
        settings,
        "META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK",
        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK,
    )
    title = getattr(
        instance, twitter_field, meta_settings.META_PREVIEW_TWITTER_TITLE_FIELD,
    )
    description = getattr(
        instance,
        description_field,
        meta_settings.META_PREVIEW_TWITTER_DESCRIPTION_FIELD,
    )

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
        "default_title": title or instance.title if instance else title,
        "default_description": description,
    }
