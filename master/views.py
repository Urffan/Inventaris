from django.shortcuts import render
from master.models import * 
# Create your views here.

def index(request):
  barang = Barang.objects.all()
  return render(request,'list.html',{ 'barang':barang } )