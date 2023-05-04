from django.urls import path
from django.utils.html import format_html
from wagtail import hooks
from wagtail.admin.staticfiles import versioned_static

from .views import get_image_rendition


@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add /static/css/custom.css to the admin."""
    return format_html(
        '<link rel="stylesheet" href="{}">',
        versioned_static("wagtail_meta_preview/wagtail-meta-preview.css"),
    )


@hooks.register("insert_global_admin_js", order=100)
def global_admin_js():
    """Add /static/css/custom.js to the admin."""
    return format_html(
        '<script src="{}"></script>',
        versioned_static("wagtail_meta_preview/wagtail-meta-preview.js"),
    )


@hooks.register("register_admin_urls")
def urlconf_time():
    return [
        path(
            "get-img-rendition/<int:pk>/",
            get_image_rendition,
            name="get_image_rendition",
        ),
    ]
