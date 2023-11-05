from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    paginas = models.IntegerField()


class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    duracion = models.IntegerField()