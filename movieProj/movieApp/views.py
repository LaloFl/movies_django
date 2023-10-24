from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        'peliculas': Pelicula.objects.all()
    })

def pelicula_d(request, id):
    search = Pelicula.objects.filter(id=id)
    print()
    if search.count() == 0:
        return render(request, '404.html')
    pelicula = search[0]
    reviews = Review.objects.filter(pelicula=pelicula)
    return render(request, 'movie.html', {
        'pelicula': pelicula,
        'reviews': reviews
    })
