# wagtial seo preview

## Panels

### General panels

The panels `SeoTitlePanel` and `SeoDescriptionPanel` are two general panels that can be used
in conjunction with different kinds of `PreviewPanel`. E.g:

```python
from wagtail_seo_preview.panels import SeoTitlePanel, SeoDescriptionPanel, TwitterPreviewPanel


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

It is possible to tweak the fallbacks by overriding the `SEO_PREVIEW_DEFAULTS` setting.

```python
# some_page.py

class SomePage(Page):
    og_title = models.CharField()
    preamble = models.TextField()

# settings.py

SEO_PREVIEW_DEFAULTS = {
    "twitter_fallback_fields": {
        "title": "og_title",
        "description": "preamble"
    }
}
```
