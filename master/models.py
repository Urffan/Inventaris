from django.db import models

# Create your models here.
class JenisBarang(models.Model):
  label = models.CharField(max_length=80)
  keterangan = models.TextField()
  def __str__(self):
    return self.label


class Barang(models.Model):
  kondisi_choices = (
    ('Bagus', 'Bagus'),
    ('Rusak', 'Rusak'),
  )
  kode = models.CharField(max_length=30)
  nama = models.CharField(max_length=80)
  jenis = models.ForeignKey(JenisBarang, on_delete=models.CASCADE)
  jumlah = models.CharField(max_length=3)
  kondisi = models.CharField(max_length=5, choices=kondisi_choices)
  def __str__(self):
    return self.nama
  

class Peminjam(models.Model):
  jk_choices = (
    ('L', 'Laki-laki'),
    ('P', 'Perempuan'),
  )
  nip = models.CharField(max_length=15)
  nama = models.CharField(max_length=50)
  jk = models.CharField(max_length=1, choices=jk_choices)
  def __str__(self):
    return self.nama
