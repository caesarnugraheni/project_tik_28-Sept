from django.urls import path
from . import views
from dosen.views import *

urlpatterns = [
    path('', views.index),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
]
