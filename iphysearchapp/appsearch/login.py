from django.contrib.auth import authenticate, login
from django.db import DatabaseError
from django.shortcuts import render, redirect
from iphysearchapp.var_env import *  #IMPORTA VAR
from django.contrib.auth import logout  
from django.http import HttpResponse

def login_view(request):
    errores = []
    errordes = ""
    respuesta = ""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print("Usuario autenticado correctamente")
                return redirect('welcome')
            else:
                respuesta = "Error en la autenticación"
                errordes = "Credenciales no válidas, inténtelo nuevamente...."
                return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores})

        except DatabaseError as e:
            respuesta = "Error en la conexión a la Base de Datos."
            errordes = "Recargue la página"
            errores.append({
                'db_name': 'dblocal_default',  # Reemplaza con el nombre de tu base de datos
                'exception_code': e.__class__.__name__,
                'exception_message': str(e),
                'additional_info': 'Verifique  su VPN ó que la DB '+HOSTOWN+' este alcanzable...'
            })
            return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores})

    return render(request, 'login.html')


def logout_view(request):
    try:
        logout(request)
        return redirect('login')

    except DatabaseError as e:
        respuesta = "Error en la conexión a la Base de Datos."
        errordes = "Recargue la página .. Si el problema persiste, contacte al soporte..."
        errores = [{
            'db_name': 'dblocal_default',  
            'exception_code': e.__class__.__name__,
            'exception_message': str(e),
            'additional_info': 'Verifique  su VPN ó que la DB '+HOSTOWN+' este alcanzable...'
        }]
        return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores})
