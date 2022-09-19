from django.db import models

# Create your models here.
class feb(models.Model):
    fakultas=models.CharField(max_length=50)
    prodi=models.CharField(max_length=100)

    def __str__(self):
        return self.fakultas