from django.db import models
# from matplotlib.pyplot import get

# Create your models here.
class factura(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    documento = models.BigIntegerField(default=0)
    telefono = models.BigIntegerField(default=0)
    correo = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    producto = models.CharField(max_length=255)
    costo = models.BigIntegerField(default=0)
        