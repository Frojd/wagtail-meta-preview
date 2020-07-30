from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from wagtail_meta_preview.meta_settings import IMAGE_DEFAULT_SIZE
from wagtail.images import get_image_model


@login_required
def get_image_rendition(request, pk):
    img = get_image_model().objects.get(pk=pk)
    return HttpResponse(img.get_rendition(IMAGE_DEFAULT_SIZE).url)
