from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('usuario_realms.urls')),
    path('', include('crono_realms.urls')),
    path('', include('biblioteca_realms.urls')),
    path('', include('list_realms.urls')),
    path('', include('cronograma_realms.urls')),

]


# MEDIA (imagens dos avatares)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)