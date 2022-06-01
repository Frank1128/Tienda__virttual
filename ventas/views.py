from multiprocessing import context
from django.shortcuts import render, redirect
from inventario.models import Productos
from ventas.models import factura
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import time

# Create your views here.
def Correo (email, nombre, apellido, producto, costo, direccion, ciudad, descripcion):
    fecha = str(time.strftime("%d/%m/%Y"))
    datos = {'email':email,'nombre':nombre,'apellido':apellido,'producto':producto,
             'costo':costo,'direccion':direccion,'fecha':fecha,'ciudad':ciudad,'descripcion':descripcion}
    template = get_template('correo.html')
    contenido = template.render(datos)

    envio = EmailMultiAlternatives(
        'Compra de producto - Style Glasses',
        'Pedido - Style Glasses',
        settings.EMAIL_HOST_USER,
        [email] 
    )
    envio.attach_alternative(contenido, 'text/html')
    try:
        envio.send()
    except:
        print("Error. Correo no enviado.")

def Correo_admin (nombre, apellido, producto, costo, direccion, ciudad, descripcion):
    email = 'salomejaramillopiedrahita@gmail.com'
    fecha = str(time.strftime("%d/%m/%Y"))
    datos = {'email':email,'nombre':nombre,'apellido':apellido,'producto':producto,
             'costo':costo,'direccion':direccion,'fecha':fecha,'ciudad':ciudad,'descripcion':descripcion}
    template = get_template('correo_admin.html')
    contenido = template.render(datos)

    envio = EmailMultiAlternatives(
        'Despachar Producto Al Cliente.',
        'Pediodo - Style Glasses',
        settings.EMAIL_HOST_USER,
        [email] 
    )
    envio.attach_alternative(contenido, 'text/html')
    try:
        envio.send()
    except:
        print("Error. Correo no enviado.")

def ventas (request, pk):
    producto = Productos.objects.get(id=pk)
    id  = producto.id
    return render (request,"ventas.html", {'producto':producto})

def fectura(request, pk):
    producto_f = Productos.objects.get(id=pk)
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
        descripcion = request.POST["txtdescripcion"]

        Correo(correo, nombre, apellido, producto, costo, direccion, ciudad, descripcion)
        Correo_admin(nombre, apellido, producto, costo, direccion, ciudad, descripcion)

        producto_f.cantidad_stock -= 1
        producto_f.save()

        data = factura(nombre=nombre, apellido=apellido, documento=documento, telefono=telefono,
        correo=correo, direccion=direccion, departamento=departamento,
        ciudad=ciudad, producto=producto, costo=costo)
        data.save()

        return redirect('inicio')
    