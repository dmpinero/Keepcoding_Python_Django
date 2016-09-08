from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from users.forms import LoginForm

def login(request):
    """
    Presenta el formulario de login y gestiona el login de un usuario
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    error_message = ""

    login_form = LoginForm()


    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        user = authenticate(username=username, password=password)
        if user is None:
            error_message = "Usuario o contraseña incorrecto"
        else:
            if user.is_active:
                django_login(request, user)  # Cambiar el usuario autenticado en el sistema
                return redirect('/')
            else:
                error_message = "Cuenta de usuario inactiva"

    context = {'error': error_message, 'form': login_form }

    return render(request, 'users/login.html', context)


def logout(request):
    """
    Hace el logout de un usuario y redirige al inicio
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    if request.user.is_authenticated():
        django_logout(request)

    return redirect('/')

