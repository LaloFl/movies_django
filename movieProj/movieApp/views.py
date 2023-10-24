from django.contrib.auth import authenticate, login, logout, models
from django import views, shortcuts
from .forms import FormRegister, FormReview
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        'peliculas': Pelicula.objects.all()
    })

def pelicula_d(request, id):
    search = Pelicula.objects.filter(id=id)
    if search.count() == 0:
        return render(request, '404.html')
    pelicula = search[0]
    reviews = Review.objects.filter(pelicula=pelicula)
    return render(request, 'movie.html', {
        'pelicula': pelicula,
        'reviews': reviews
    })

class Register(views.View):
    def get(self, request):
        form = FormRegister()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = FormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
        return shortcuts.redirect("home")

class ReviewView(views.View):
    def get(self, request, p_id):
        if not request.user.is_authenticated:
            return shortcuts.redirect("login")

        search = Pelicula.objects.filter(id=p_id)
        if search.count() == 0:
            return render(request, '404.html')
        pelicula = search[0]
        user = User.objects.get(id=request.user.id)
        form = FormReview(initial={"pelicula": pelicula, "usuario": user})
        return render(request, "review.html", {"form": form})

    def post(self, request, p_id,):
            search = Pelicula.objects.filter(id=p_id)
            if search.count() == 0:
                return render(request, '404.html')
            pelicula = search[0]
            user = User.objects.get(id=request.user.id)
            form = FormReview(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.pelicula = pelicula
                review.usuario = user
                review.save()
                return shortcuts.redirect(request.META.get('HTTP_REFERER')) 