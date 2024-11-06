from tkinter import messagebox
from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *
from django.views.decorators.http import require_GET
from appsearch.varias_func import *
import requests
from django.shortcuts import render, redirect
from django.contrib import messages


def loginmain(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        url_api_token = 'http://10.10.26.5:80/api/token/'
        data = {'username': username, 'password': password}

        try:
            response = requests.post(url_api_token, json=data, timeout=5)
            if 200 <= response.status_code < 300:
                #request.session['username'] = username
                return redirect('welcome') 
            elif 400 <= response.status_code < 500:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
            else:
                messages.warning(request, "Respuesta inesperada del servidor.")
        except requests.Timeout:
            messages.error(request, "No se pudo conectar al servidor. Tiempo de espera agotado.")
        except requests.RequestException as req_err:
            messages.error(request, f"Error al conectarse al servidor: {req_err}")

    return render(request, 'login.html', {
        'dbs': esquemata(),
    })
