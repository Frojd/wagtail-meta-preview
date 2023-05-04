from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from wagtail.images import get_image_model

from wagtail_meta_preview.meta_settings import META_PREVIEW_IMAGE_DEFAULT_SIZE
from wagtail_meta_preview.utils import get_focal


@login_required
def get_image_rendition(request, pk):
    img = get_image_model().objects.get(pk=pk)
    if not img.is_editable_by_user(request.user):
        return HttpResponseForbidden()

    focal = get_focal(img)

    data = {
        "src": img.get_rendition(META_PREVIEW_IMAGE_DEFAULT_SIZE).url,
        "focal": focal,
    }

    return JsonResponse(data)
