from multiprocessing import context
from django.shortcuts import render, redirect
from inventario.models import Productos
from ventas.models import factura

# Create your views here.
def ventas (request,pk):
    producto = Productos.objects.get(id=pk)
    id  = producto.id
    return render (request,"ventas.html", {'producto':producto})

def fectura(request):
    if request.method == "POST":
        nombre = request.POST["txtnombre"]
        apellido = request.POST["txtapellido"]
        documento = request.POST["txtdocumento"]
        telefono = request.POST["txttelefono"]
        correo = request.POST["txtcorreo"]
        direccion = request.POST["txtdireccion"]
        departamento = request.POST["txtdepartamento"]
        ciudad = request.POST["txtciudad"]
        producto = request.POST["txtproducto"]
        costo = request.POST["txtcosto"]

        data = factura(nombre=nombre, apellido=apellido,documento=documento,telefono=telefono,
        correo=correo,direccion=direccion,departamento=departamento,
        ciudad=ciudad,producto=producto,costo=costo)
        data.save()

        return redirect('inicio')
    