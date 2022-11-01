from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profil/', include('profil.urls')),
    path('faperta/', include('faperta.urls')),
    path('feb/', include('feb.urls')),
    path('fh/', include('fh.urls')),
    path('fk/', include('fk.urls')),
    path('fkip/', include('fkip.urls')),
    path('dosen/', include('dosen.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('tendik/', include('tendik.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)