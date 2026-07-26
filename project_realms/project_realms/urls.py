from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('usuario_realms.urls')),
    path('', include('crono_realms.urls')),
    path('', include('biblioteca_realms.urls')),
    path('', include('list_realms.urls')),
    path('', include('cronograma_realms.urls')),

    path(
        'media/<path:path>',
        serve,
        {
            'document_root': settings.MEDIA_ROOT
        }
    ),
]