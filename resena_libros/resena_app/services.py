from django.contrib.auth.models import Group, User
from resena_app.models import Contactos, Resenas, Libros, Generos, Autores
from django.contrib.auth.hashers import make_password
from django.core.files import File
from django.db.models import Q
from django.contrib import messages

def create_generos():
    genero = Generos.objects.create(id='000', nombre='Ciencias de las Computación, Información, & Trabajo en General')
    genero = Generos.objects.create(id='100', nombre='Filosofía & Psicología')
    genero = Generos.objects.create(id='200', nombre='Religión')
    genero = Generos.objects.create(id='300', nombre='Ciencias Sociales')
    genero = Generos.objects.create(id='400', nombre='Lenguage')
    genero = Generos.objects.create(id='500', nombre='Ciencias')
    genero = Generos.objects.create(id='600', nombre='Tecnología')
    genero = Generos.objects.create(id='700', nombre='Artes & Recreación')
    genero = Generos.objects.create(id='800', nombre='Literatura')
    genero = Generos.objects.create(id='900', nombre='Historia & Geografía')
    return genero

def create_groups():
    group = Group.objects.create(name='lector')
    group = Group.objects.create(name='administrador')
    return group

def create_user(form):
    user = User.objects.create(username=form['username'].value(), first_name=form['first_name'].value(), last_name=form['last_name'].value(), email=form['email'].value(), password=make_password(form['password1'].value()))
    group = Group.objects.get(name='lector')
    user.groups.add(group)
    return user

def update_user_data(form, user):
    user = User.objects.filter(pk=user.id).update(username=form['username'].value(), first_name=form['first_name'].value(), last_name=form['last_name'].value(), email=form['email'].value())
    return user

def resena_form(id):
    book = Libros.objects.filter(id=id)
    autor = Autores.objects.filter(aut__id=book.values('id')[:1])
    return  book, autor

def resena_data_book(form, rating):
    libro = Libros.objects.get(id=form['libro'].value())
    user = User.objects.get(id=form['usuario'].value())
    resena = Resenas.objects.create(libro= libro, usuario= user, comentario=form['comentario'].value(), calificacion=rating, seguir_autor=form['seguir_autor'].value())
    return resena

def contacto_page(form):
    contact = Contactos.objects.create(nombre=form['nombre'].value(), email=form['email'].value(), mensaje=form['mensaje'].value())
    return contact

def search_page(form):
    if Libros.objects.filter(Q(titulo__istartswith=form['search'].value()) | Q(titulo__icontains=form['search'].value())):
        book = Libros.objects.filter(Q(titulo__istartswith=form['search'].value()) | Q(titulo__icontains=form['search'].value()))
        autor = Autores.objects.filter(aut__id=book.values('id')[:1])
        genero = Generos.objects.filter(gen__id=book.values('id')[:1])
        return  book, autor, genero
            
    elif Autores.objects.filter(Q(nombre__istartswith=form['search'].value()) | Q(nombre__icontains=form['search'].value())):
        autor = Autores.objects.filter(Q(nombre__istartswith=form['search'].value()) | Q(nombre__icontains=form['search'].value()))
        book = Libros.objects.filter(autor=autor.values('id')[:1])
        genero = Generos.objects.filter(gen__id=book.values('id')[:1])
        return  book, autor, genero
            
    elif Generos.objects.filter(Q(nombre__istartswith=form['search'].value()) | Q(nombre__icontains=form['search'].value())):
        genero = Generos.objects.filter(Q(nombre__istartswith=form['search'].value()) | Q(nombre__icontains=form['search'].value()))
        book = Libros.objects.filter(genero=genero.values('id')[:1])
        autor = Autores.objects.filter(aut__id=book.values('id')[:1])
        return  book, autor, genero

def add_autor(form):
    autor = Autores.objects.create(nombre=form['nombre'].value())
    return autor

def add_book(form, f):
    book = Libros.objects.create(titulo=form['titulo'].value(), descripcion=form['descripcion'].value(), anio_publicacion=form['anio_publicacion'].value(), portada_url=form['portada_url'].value())
    autor = Autores.objects.create(nombre=form['autor'].value())
    p = File(open(f"resena_app/media/img/{str(f['imagen'])}", 'rb'))
    book.imagen.save(str(f['imagen']), p)
    book.genero.set(form['genero'].value())
    book.autor.set(autor.id)
    return book
    
def pass_reset_form(form):
    user = User.objects.get(email=form['email'].value())
    return user
    
def pass_reset_confirm(form, user):
    if len(form['password'].value()) >= 8:
        password=make_password(form['password'].value())
        user.set_password(password)
        user.save()
    return user