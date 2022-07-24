import wagtail.admin.urls
import wagtail.urls
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", include(wagtail.admin.urls)),
    path("", include(wagtail.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
