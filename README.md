# wagtial meta preview

## Todo

- Change fallback settings to TWITTER_TITLE_META_FIELD_FALLBACKS

## Panels

### General panels

The panels `MetaTitlePanel` and `MetaDescriptionPanel` are two general panels that can be used
in conjunction with different kinds of `PreviewPanel`. E.g:

```python
from wagtail_meta_preview.panels import MetaTitlePanel, MetaDescriptionPanel, TwitterPreviewPanel


panels = [
    TwitterPreviewPanel([
        MetaTitlePanel("twitter_title"),
        MetaDescriptionPanel("twitter_description"),
    ])
]
```

The PreviewPanels behave just like a `MultiFieldPanel`
The default fallback for the MetaTitlePanel is the current instance's (if it has been created)
title field.
There is no default fallback for the MetaDescriptionPanel.

It is possible to tweak the fallbacks by overriding the `META_PREVIEW_X_Y_FALLBACK` setting.

```python
# some_page.py

class SomePage(Page):
    og_title = models.CharField()
    preamble = models.TextField()
    twitter_title = models.CharField()
    twitter_description = models.CharField()

    panels = [
        TwitterPreviewPanel([
            MetaTitlePanel("twitter_title"),
            MetaDescriptionPanel("twitter_description"),
        ])
    ]

# settings.py

META_PREVIEW_TWITTER_TITLE_FALLBACK = "og_title,title"
META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK = "preamble"
```

If the `twitter_title` is empty here the preview will show the value of `og_title` and if that field
is empty, the value of `title` will be shown.

### Preview Panels

There are currently three preview panels, `TwitterPreviewPanel`, `FacebookPreviewPanel` and `GooglePreviewPanel`.

They are all used in the same way:
```python
# Example with the Twitter Panel
from wagtail_meta_preview.panels import MetaTitlePanel, MetaDescriptionPanel, TwitterPreviewPanel


class SomePage(page):
    a_title = models.CharField()
    a_description = models.TextField()

    panels = [
        TwitterPreviewPanel([
            MetaTitlePanel("a_title"),
            MetaDescriptionPanel("a_description"),
        ])
    ]

```

### Settings

Sometimes if the fields are empty, you still want them to be populated. E.g. Twitter will still
use the page's `<title>` field if there is no `og:title` or `og:twitter` present. If you have rules setup for this. Maybe something like this:

```html
<meta rel="twitter:title" value="{% firstof page.twitter_title page.og_title page.title %}"
```

We still want the preview panel to be able to handle the same logic.

Therefore we have (with defaults):

```python
# Twitter specific
META_PREVIEW_TWITTER_TITLE_FALLBACK = "title"
META_PREVIEW_TWITTER_DESCRIPTION_FALLBACK = ""
META_PREVIEW_TWITTER_TITLE_FIELD = "twitter_title"
META_PREVIEW_TWITTER_DESCRIPTION_FIELD = "twitter_description"
```
