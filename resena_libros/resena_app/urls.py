"""
URL configuration for resena_libros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from resena_app.views import home, login_page, left, register_user, perfil_user, update_user, register_book, resena_book, contacto, resena_list, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name ='home'),
    path('accounts/login/', login_page, name ='login_page'),
    path('accounts/logout/', left, name= 'left'),
    path('register_user/', register_user, name= 'register_user'),
    path('perfil_user/', perfil_user, name= 'perfil_user'),
    path('update_user/', update_user, name= 'update_user'),
    path('register_book/', register_book, name= 'register_book'),
    path('resena_book/', resena_book, name= 'resena_book'),
    path('resena_list/', resena_list, name= 'resena_list'),
    path('contacto/', contacto, name= 'contacto'),
    # Reset Password URLS
    path('registration/password_reset/', password_reset, name= 'password_reset'),
    path('registration/password_reset_done.html/', password_reset_done, name= 'password_reset_done'),
    path('registration/password_reset_confirm.html/<uidb64>/<token>/', password_reset_confirm, name= 'password_reset_confirm'),
    path('registration/password_reset_complete.html', password_reset_complete, name= 'password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
