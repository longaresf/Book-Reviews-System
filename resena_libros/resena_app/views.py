from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import Group, User
from django.contrib import messages
from resena_app.models import Contactos, Resenas, Libros, Generos, Autores
from resena_app.forms import LoginForm, CustomUserCreationForm, LibrosForm, ResenasForm, AutoresForm, GenerosForm, ContactosForm, UserUpdateForm, SearchForm, Password_Reset_Form, Password_Reset_confirm_Form
from resena_app.services import create_user, update_user_data, add_book, resena_data_book, contacto_page, search_page, resena_form, pass_reset_form, pass_reset_confirm
from django.core import signing
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import uuid

# Create your views here.

def home(request):
    book = Libros.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            try:
                book, autor, genero = search_page(form)
                return render(request, "home.html", { 'form':form, 'book': book, 'autor': autor, 'genero': genero })
            except TypeError:
                messages.warning(request, "No se encontró ninguna coincidencia")
        else:
            messages.warning(request, "Algo salió mal, favor intentar nuevamente")
    else:    
        form = SearchForm()
    return render(request, 'home.html', { 'book':book, 'form':form})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.warning(request, "Usuario o contraseña errada")
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form })

def left(request):
    logout(request)
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            create_user(form)
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            login(request,user)
            
            subject = 'Bienvenido a Reseñas de Libros'
            message = f'Hi {user.username}, gracias por registrarte.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )

            messages.success(request, "Registro exitoso. Gracias por registrarte")
            return redirect('/')
        else:
            messages.warning(request, "Falló registro, favor intentar nuevamente")
    else:
        form = CustomUserCreationForm()
    return render(request, "register_user.html", { 'form':form  })

@login_required
def perfil_user(request):
    return render(request, "perfil_user.html")

@login_required
def update_user(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.cleaned_data
            update_user_data(form, user)
            messages.success(request, "Registro mofificado exitosamente.")
        else:
            messages.warning(request, "Hubo un problema, favor intentar nuevamente")
    else:
        form = UserUpdateForm()
    return render(request, "update_user.html", { 'form':form, 'user':user })

@login_required
def register_book(request):
    if request.method == 'POST':
        form = LibrosForm(request.POST, request.FILES)
        f = request.FILES
        if form.is_valid():
            form.cleaned_data
            f.cleaned_data
            add_book(form, f)
            messages.success(request, "Operación exitosa.")
            return redirect('/')
    else:
        form = LibrosForm()
    return render(request, "register_book.html", { 'form': form })

@login_required
def resena_book(request):
    id = request.COOKIES['libro_id']
    libro, autor = resena_form(id)
    
    if request.method == 'POST':
        form = ResenasForm(request.POST)
        rating = request.COOKIES['rating']
        if form.is_valid():
            form.cleaned_data
            resena_data_book(form, rating)
            messages.success(request, "Operación exitosa.")
            #return redirect('/')
    else:
        form = ResenasForm()
    return render(request, "resena_book.html", { 'form': form, 'libro': libro, 'autor': autor })

def contacto(request):
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            contacto_page(form)
            messages.success(request, "Operación exitosa.")
            return redirect('/')
    else:
        form = ContactosForm()
    return render(request, "contacto.html", { 'form': form })

@login_required
def resena_list(request):
    resenas = Resenas.objects.all()
    return render(request, "resena_list.html", { 'resenas': resenas })

def password_reset(request):
    if request.method == 'POST':
        form = Password_Reset_Form(request.POST)
        if form.is_valid():
            form.cleaned_data
            try:
                user = pass_reset_form(form)
                request.session['email'] = user.email
                return redirect('/registration/password_reset_done.html')
            except User.DoesNotExist:
                    messages.warning(request, "Email no existe, favor intentar nuevamente")
    else:
        form = Password_Reset_Form()
    return render(request, "registration/password_reset.html", { 'form': form })
    
def password_reset_done(request):
    email = request.session['email']
    user = User.objects.get(email=email)
    token = signing.dumps({"user": user.id})
    domain = request.get_host()
    uidb64 = uuid.uuid4()

    context = {
    "email": email,
    "user": user,
    "token": token,
    "domain": domain,
    "uidb64": uidb64,
    "year": 2024
    }

    receiver_email = 'francisco.longares@gmail.com'
    template_name = "registration/password_reset_email.html"
    convert_to_html_content =  render_to_string(
    template_name=template_name,
    context=context
)
    plain_message = strip_tags(convert_to_html_content)

    yo_send_it = send_mail(
    subject="Password Reset Email",
    message=plain_message,
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[receiver_email,],   # recipient_list is self explainatory
    html_message=convert_to_html_content,
    fail_silently=True    # Optional
)
    return render(request, "registration/password_reset_done.html", {'context': context} )
    
def password_reset_confirm(request, token):
    if request.method == 'POST':
        form = Password_Reset_confirm_Form(request.POST)
        token_1 = signing.loads(token)
        user = User.objects.get(id=token_1['user'])

        if form.is_valid():
            form.cleaned_data
            pass_reset_confirm(form, user)
            messages.success(request, "Cambio de contraseña con éxito")
            return redirect("/registration/password_reset_complete.html")
        else:
            messages.warning(request, "No se pudo cambiar la contraseña")
    
    else:
        form = Password_Reset_confirm_Form()
    return render(request, "registration/password_reset_confirm.html", { 'form': form })

def password_reset_complete(request):
    return render(request, "registration/password_reset_complete.html")
