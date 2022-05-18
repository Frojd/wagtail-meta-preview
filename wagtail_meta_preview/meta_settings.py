from django.conf import settings

META_PREVIEW_IMAGE_DEFAULT_SIZE = getattr(
    settings, "META_PREVIEW_IMAGE_DEFAULT_SIZE", "fill-1200x628"
)

META_PREVIEW_TWITTER_TITLE_FIELDS = getattr(
    settings,
    "META_PREVIEW_TWITTER_TITLE_FIELDS",
    "twitter_title,og_title,seo_title,title",
)
META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = getattr(
    settings,
    "META_PREVIEW_TWITTER_DESCRIPTION_FIELDS",
    "twitter_description,og_description,search_description",
)
META_PREVIEW_TWITTER_IMAGE_FIELDS = getattr(
    settings,
    "META_PREVIEW_TWITTER_IMAGE_FIELDS",
    "twitter_image,og_image",
)


META_PREVIEW_FACEBOOK_TITLE_FIELDS = getattr(
    settings,
    "META_PREVIEW_FACEBOOK_TITLE_FIELDS",
    "og_title,seo_title,title",
)
META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = getattr(
    settings,
    "META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS",
    "og_description,search_description",
)
META_PREVIEW_FACEBOOK_IMAGE_FIELDS = getattr(
    settings,
    "META_PREVIEW_FACEBOOK_IMAGE_FIELDS",
    "og_image",
)


META_PREVIEW_GOOGLE_TITLE_FIELDS = getattr(
    settings,
    "META_PREVIEW_GOOGLE_TITLE_FIELDS",
    "seo_title,title",
)
META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = getattr(
    settings,
    "META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS",
    "search_description",
)
