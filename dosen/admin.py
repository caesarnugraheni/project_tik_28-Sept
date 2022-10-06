from django.contrib import admin
from dosen.models import dosen, Kelompok

# Register your models here.


# username : admin
# pw : admin123

class DosenAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nip', 'ttl', 'foto', 'email', 'fakultas', 'prodi', 'alamat', 'kelompok_id']
    search_fields = ['nama', 'fakultas', 'prodi']
    list_filter = ('kelompok_id',)
    list_per_page = 5

admin.site.register(dosen, DosenAdmin)
admin.site.register(Kelompok)