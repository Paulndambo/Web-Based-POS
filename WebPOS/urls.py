from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("pos/", include("pos.urls")),
    path("inventory/", include("inventory.urls")),
    path("users/", include("users.urls")),
    path("suppliers/", include("suppliers.urls")),
    path("payments/", include("payments.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
