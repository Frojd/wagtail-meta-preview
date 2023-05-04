# Setting up panels

This application provides 8 panels:
- `FacebookPreviewPanel` and `FacebookFieldPreviewPanel`
- `GooglePreviewPanel` and `GoogleFieldPreviewPanel`
- `TwitterPreviewPanel` and `TwitterFieldPreviewPanel`

## Preview panels

Here's how to setup `FacebookFieldPreviewPanel` with some og-fields:

```python
from wagtail.images import get_image_model_string
from wagtail.core.models import Page
from wagtail.admin.panels import FieldPanel

from wagtail_meta_preview.panels import FacebookFieldPreviewPanel


class SomePage(Page):
    og_title = models.CharField()
    og_description = models.TextField()
    og_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Og image"),
    )

    panels = [
        FacebookFieldPreviewPanel([
            FieldPanel("og_title"),
            FieldPanel("og_description"),
            FieldPanel("og_image"),
        ], heading="Facebook")
    ]
```

This sets up a facebook preview panel with the fields left of the preview:

![example-facebook-preview](https://raw.githubusercontent.com/rinti/wagtail-meta-preview/master/docs/img/facebook-preview-example.PNG)

If you'd rather separate the preview from the fields it's possible to use the `FacebookPreviewPanel`:

```python
    panels = [
        MultiFieldPanel([
            FieldPanel("og_title"),
            FieldPanel("og_description"),
            FieldPanel("og_image"),
        ], heading="Facebook"),
        FacebookPreviewPanel(heading="Facebook Preview")
    ]
```

Which will look like this:

![example-facebook-preview](https://raw.githubusercontent.com/rinti/wagtail-meta-preview/master/docs/img/facebook-preview-single-example.PNG)

## How settings will affect the panels

Settings decides which fields will be used when showing titles/descriptions/images. For facebook
title the default settings says to first look in the `og_title`, then in the `seo_title`, then in the `title`:

`META_PREVIEW_FACEBOOK_TITLE_FIELDS = "og_title,seo_title,title"`

So if you have a field that is named e.g. `open_graph_title` you have to change the setting to:

`META_PREVIEW_FACEBOOK_TITLE_FIELDS = "open_graph_title,seo_title,title"`

## Examples

Good examples of both panel types can be seen in the MetaPage in `tests/app/mixins.py` in this repository

## Next steps
* [Settings](./3-settings.md)

## Or go back:
* [Getting started](./1-getting-started.md)
