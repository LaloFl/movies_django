from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review, Pelicula, User  

class FormRegister(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']


class FormReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["usuario", "pelicula", "comentario", "calificacion"]
        def __init__(self, *args, **kwargs):
            super(FormReview, self).__init__(*args, **kwargs)   
            self.fields['usuario'].disabled = True
            self.fields['pelicula'].disabled = True