from django.contrib import admin
from django.urls import path, include
import movieApp.views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("pelicula/<int:id>", views.pelicula_d, name="pelicula"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("review/<int:p_id>/", views.ReviewView.as_view(), name="NewReview"),

]
