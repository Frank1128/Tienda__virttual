from django.shortcuts import render
from inventario.models import Productos

# Create your views here.
def inicio (request):
    productos = Productos.objects.all().order_by('id')
    return render (request,"inicio.html",{'productos':productos})