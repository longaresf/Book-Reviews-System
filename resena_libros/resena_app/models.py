from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Contactos(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False) #Unique
    mensaje = models.TextField(null=False, blank=False)
    crea_regist = models.DateField(auto_now_add=True)
    mod_regist = models.DateField(auto_now=True)
    
    def __str__(self):
        return '%s' % (self.nombre)

class Generos(models.Model):
    id = models.CharField(primary_key=True, null=False)
    nombre = models.CharField(max_length=80, null=False, blank=False)
    
    def __str__(self):
        return '%s' % (self.nombre)
    
class Autores(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False, blank=False) #Unique
    
    def __str__(self):
        return '%s' % (self.nombre)
    
class Libros(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    titulo = models.CharField(max_length=80, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    anio_publicacion = models.IntegerField(null=False, blank=False)
    portada_url = models.URLField(max_length=200)
    genero = models.ManyToManyField(Generos, related_name = 'gen')
    autor = models.ManyToManyField(Autores, related_name = 'aut')
    imagen = models.ImageField(upload_to='libros/')
    crea_regist = models.DateField(auto_now_add=True)
    mod_regist = models.DateField(auto_now=True)
    
    def __str__(self):
        return '%s' % (self.titulo)
    
class Resenas(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    libro = models.ForeignKey(Libros, related_name = 'lib', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, related_name = 'usuar', on_delete=models.SET_NULL, null=True)
    calificacion = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(null=False, blank=False)
    seguir_autor = models.BooleanField(default=False)
    fecha_resena = models.DateField(auto_now_add=True)
    mod_resena = models.DateField(auto_now=True)

def __str__(self):
        return '%s' % (self.libro)