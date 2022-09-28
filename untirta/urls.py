from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profil/', include('profil.urls')),
    path('faperta/', include('faperta.urls')),
    path('feb/', include('feb.urls')),
    path('fh/', include('fh.urls')),
    path('fk/', include('fk.urls')),
    path('fkip/', include('fkip.urls')),
]
