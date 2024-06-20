from django import forms
from django.forms import ModelForm, ClearableFileInput, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from resena_app.models import Contactos, Resenas, Libros, Generos, Autores
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column

CALIFICACION = ((1, 'No lo recomiendo'),
           (2, 'Es regular'),
           (3, 'Es bueno'),
           (4, 'Lo recomiendo'),
            (5, 'Me gustó mucho'))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
         label = 'Usuario',
     )
    password = forms.CharField(max_length=30,
        widget=forms.PasswordInput,
         label = 'Password',
     )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class AutoresForm(forms.ModelForm):
    nombre = forms.CharField(
         label = 'Autor',
     )
    class Meta:
        model = Autores
        fields = ('nombre',)

class LibrosForm(forms.ModelForm):
    titulo = forms.CharField(
        label='Título'
     )
    descripcion = forms.CharField(
        label='Descripción'
     )
    anio_publicacion = forms.CharField(
        label='Año Publicación'
     )
    portada_url = forms.CharField(
        label='Portada Url'
     )
    genero = forms.ModelChoiceField(
        queryset=Generos.objects.all(),
     )
    autor = forms.CharField(
     )
    
    class Meta:
        model = Libros
        fields = ('titulo', 'descripcion', 'anio_publicacion', 'portada_url', 'genero', 'autor', 'imagen')

class ResenasForm(forms.ModelForm):

    class Meta:
        model = Resenas
        fields = ('libro', 'usuario', 'calificacion', 'comentario', 'seguir_autor')

class GenerosForm(forms.ModelForm):

    class Meta:
        model = Generos
        fields = ('nombre',)
        
class ContactosForm(forms.ModelForm):
    
    class Meta:
        model = Contactos
        fields = ('nombre', 'email', 'mensaje') 
        
class UserUpdateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
    
class SearchForm(forms.Form):

    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Busqueda por título, autor o género'}), max_length=100, label='')
    
class Password_Reset_Form(forms.Form):
    email = forms.EmailField(max_length=50,
         label = 'Favor ingrese su email',)
    
class Password_Reset_confirm_Form(forms.Form):
    password = forms.CharField(max_length=30,
        widget=forms.PasswordInput,
         label = 'Nueva contraseña:',
     )
