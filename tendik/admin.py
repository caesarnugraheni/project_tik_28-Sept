from django.contrib import admin
from tendik.models import tendik, Kelompok

# Register your models here.

class TendikAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nip', 'ttl', 'foto', 'email', 'unit', 'alamat', 'kelompok_id']
    search_fields = ['nama', 'fakultas', 'prodi']
    list_filter = ('kelompok_id',)
    list_per_page = 5

admin.site.register(tendik, TendikAdmin)
admin.site.register(Kelompok)