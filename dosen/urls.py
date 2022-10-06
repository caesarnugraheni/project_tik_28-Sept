from django.urls import path
from . import views
from dosen.views import index, tambah_dosen



urlpatterns = [
    path('', views.index),
    path('tambah-dosen/', tambah_dosen)
]
