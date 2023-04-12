from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

class Empresa(models.Model):
    nombre = models.CharField(max_length=20)
    cuit = models.IntegerField(max_length=11)
    
class Rubro(models.Model):
    categoria = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    
class Zona(models.Model):
    Provincia = models.CharField(max_length=20)
    codigo_postal = models.IntegerField(max_length=11)