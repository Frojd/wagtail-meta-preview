# Settings

## Field settings

Field settings are used to define which order of importance
the fields which the preview uses has. The fields specified does not have to exists.
It will take the first field that is available on the model amongst the specified field order.
The available settings and their default values:

```python
# Titles
META_PREVIEW_FACEBOOK_TITLE_FIELDS = "og_title,seo_title,title"
META_PREVIEW_TWITTER_TITLE_FIELDS = "twitter_title,og_title,seo_title,title"
META_PREVIEW_GOOGLE_TITLE_FIELDS = "seo_title,title"

# Descriptions
META_PREVIEW_FACEBOOK_DESCRIPTION_FIELDS = "og_description,search_description"
META_PREVIEW_TWITTER_DESCRIPTION_FIELDS = "twitter_description,og_description,search_description"
META_PREVIEW_GOOGLE_DESCRIPTION_FIELDS = "search_description"

# Images
META_PREVIEW_FACEBOOK_IMAGE_FIELDS = "og_image"
META_PREVIEW_TWITTER_IMAGE_FIELDS = "twitter_image,og_image"
```

They are supposed to mimic what you would do if you had html-meta tags that looks like this:

```html
<meta property="og:title" content="{% firstof page.og_title page.seo_title page.title %}" />
```

If you for example only use the og-title and don't want to fallback on other fields
you can adjust your settings like this:

```python
META_PREVIEW_FACEBOOK_TITLE_FIELDS = "og_title"
META_PREVIEW_TWITTER_TITLE_FIELDS = "og_title"
```

## Image size setting

The image size is determined by `META_PREVIEW_IMAGE_DEFAULT_SIZE`
which as a default value of `fill-1200x628`

## Previous docs:
* [Getting started](./1-getting-started.md)
* [Setting up panels](./2-setting-up-panels.md)
