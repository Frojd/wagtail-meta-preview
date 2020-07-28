# wagtial meta preview

## Todo

- Change fallback settings to TWITTER_META_FIELD_FALLBACKS

## Panels

### General panels

The panels `SeoTitlePanel` and `SeoDescriptionPanel` are two general panels that can be used
in conjunction with different kinds of `PreviewPanel`. E.g:

```python
from wagtail_meta_preview.panels import SeoTitlePanel, SeoDescriptionPanel, TwitterPreviewPanel


panels = [
    TwitterPreviewPanel([
        SeoTitlePanel("twitter_title"),
        SeoDescriptionPanel("twitter_description"),
    ])
]
```

The PreviewPanels behave just like a `MultiFieldPanel`
The default fallback for the SeoTitlePanel is the current instance's (if it has been created)
title field.
There is no default fallback for the SeoDescriptionPanel.

It is possible to tweak the fallbacks by overriding the `X_PREVIEW_X_FALLBACK` setting.

```python
# some_page.py

class SomePage(Page):
    og_title = models.CharField()
    preamble = models.TextField()

# settings.py

TWITTER_PREVIEW_TITLE_FALLBACK_FIELD = "og_title,title"
TWITTER_PREVIEW_DESCRIPTION_FALLBACK = "preamble"

# utils.py

def get_twitter_title(instance):
    return instance.og_title or instance.title

def get_twitter_description(instance):
    return instance.description
```

### Preview Panels

There are currently three preview panels, `TwitterPreviewPanel`, `FacebookPreviewPanel` and `GooglePreviewPanel`.

They are all used in the same way:
```python
# Example with the Twitter Panel
from wagtail_meta_preview.panels import SeoTitlePanel, SeoDescriptionPanel, TwitterPreviewPanel


class SomePage(page):
    a_title = models.CharField()
    a_description = models.TextField()

    panels = [
        TwitterPreviewPanel([
            SeoTitlePanel("a_title"),
            SeoDescriptionPanel("a_description"),
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

Therefore we have:

- `TWITTER_PREVIEW_TITLE_FALLBACK_FIELD`
- `TWITTER_PREVIEW_DESCRIPTION_FALLBACK_FIELD`
- `FACEBOOK_PREVIEW_TITLE_FALLBACK_FIELD`
- `FACEBOOK_PREVIEW_DESCRIPTION_FALLBACK_FIELD`
- `META_PREVIEW_TITLE_FALLBACK_FIELD`
- `META_PREVIEW_DESCRIPTION_FALLBACK_FIELD`
