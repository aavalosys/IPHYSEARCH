import logging
from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.http import JsonResponse
from appsearch.varias_func import *
import networkx as nx
import json
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def grupo_requerido(grupos_permitidos, respuesta, errordes, errores):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=grupos_permitidos).exists():
                return view_func(request, *args, **kwargs)
            else:
                # Renderiza la página de error con los parámetros proporcionados
                return render(request, 'errorpage.html', {
                    'respuesta': respuesta,
                    'errordes': errordes,
                    'errores': errores
                })
        return _wrapped_view
    return decorator

@login_required
@grupo_requerido(
    grupos_permitidos=['superuser','adminusers', 'especialistas', 'usuariosvista'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def about(request): 
    username = request.user.username 
    return render(request, 'paginas/about.html', {
        'dbs': esquemata_general(),
        'user': username,
        })


   



