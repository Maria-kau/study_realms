"""
URL configuration for project_realms project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Admin Django
    path('admin/', admin.site.urls),

    # Apps
    path('', include('usuario_realms.urls')),
    path('', include('crono_realms.urls')),
    path('', include('biblioteca_realms.urls')),
    path('', include('list_realms.urls')),
    path('', include('cronograma_realms.urls')),

]


# Arquivos de mídia (avatares, imagens dos usuários)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)