from django.db import models

# Create your models here.
class Peminjaman(models.Model):
  status_peminjaman_choices = (
    ('Sudah Kembali', 'Sudah Kembali'),
    ('Belum Kembali', 'Belum Kembali'),
  )
  tanggal_pinjam = models.DateField()
  tanggal_kembali = models.DateField()
  status_peminjaman = models.CharField(max_length=10, choices=status_peminjaman_choices)

  def __str__(self):
    return self.tanggal_pinjam
