from django.contrib import admin
from master.models import *

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
  list_display = ['kode','nama','jenis','jumlah','kondisi']
  list_per_page = 25
  list_filter = []
  search_fields = ['kode','nama','jenis']
admin.site.register(Barang,BarangAdmin)



admin.site.register(JenisBarang)
admin.site.register(Peminjam)
