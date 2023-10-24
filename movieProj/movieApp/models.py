from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imgURL = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Cast(models.Model):
    id = models.AutoField(primary_key=True)
    personaje = models.CharField(max_length=50)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.personaje + " - " + self.actor.nombre + " " + self.actor.apellido
    
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    duracion = models.IntegerField(blank=True)
    generos = models.ManyToManyField(Genero, blank=True)
    creditos = models.ManyToManyField(Actor, blank=True)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, blank=True)
    fechaEstreno = models.DateField(blank=True)
    pais = models.CharField(max_length=50, blank=True)
    posterURL = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    follow = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200)
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.comentario