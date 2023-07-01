from django.db import models

# Create your models here.

class Descripcion(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class item(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.ForeignKey(Descripcion, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

opciones_consultas=[
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencias"],
    [3,"peticiones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
    

  