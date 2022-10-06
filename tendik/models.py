from django.db import models

# Create your models here.

class Kelompok(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class tendik(models.Model):
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='C:/projecttik/untirta/dosen/static/dosen/images')
    email = models.CharField(max_length=200)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=150)
    kelompok_id = models.ForeignKey(Kelompok, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.nama        