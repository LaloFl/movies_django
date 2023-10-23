from django.db import models

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
    
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    fechaEstreno = models.DateField()
    enCines = models.BooleanField()
    posterURL = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Cast(models.Model):
    id = models.AutoField(primary_key=True)
    personaje = models.CharField(max_length=50)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.personaje + " - " + self.actor.nombre + " " + self.actor.apellido
    
