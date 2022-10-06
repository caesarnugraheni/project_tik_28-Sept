from django.contrib import admin
from mahasiswa.models import mahasiswa, Kelompok

# Register your models here.

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nim', 'ttl', 'foto', 'email', 'fakultas', 'prodi', 'kelompok_id']
    search_fields = ['nama', 'fakultas', 'prodi']
    list_filter = ('kelompok_id',)
    list_per_page = 5

admin.site.register(mahasiswa, MahasiswaAdmin)
admin.site.register(Kelompok)