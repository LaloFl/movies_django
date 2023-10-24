from django.contrib import admin
from .models import *

# Register your models here.
for model in [Genero, Estudio, Pelicula, Actor, Cast, Usuario, Review]:
    admin.site.register(model)