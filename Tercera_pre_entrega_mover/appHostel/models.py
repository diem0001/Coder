from django.db import models

# Create your models here.
class Cuarto(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    capacidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.numero} - {self.capacidad} personas"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nombre} - {self.edad} - {self.nacionalidad} "

class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.puesto} "
