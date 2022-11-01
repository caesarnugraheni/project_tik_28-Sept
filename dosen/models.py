from unittest.util import _MAX_LENGTH
from django.db import models

class Kelompok(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class dosen(models.Model):
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=70)
    ttl = models.CharField(max_length=70)
    foto = models.ImageField(upload_to='media/', null=True)
    email = models.CharField(max_length=70)
    fakultas = models.CharField(max_length=70)
    prodi = models.CharField(max_length=70)
    alamat = models.CharField(max_length=70)
    kelompok_id = models.ForeignKey(Kelompok, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.nama

