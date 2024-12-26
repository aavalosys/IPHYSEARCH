import logging
from django.shortcuts import render
from mysql.connector import Error
from django.core.cache import cache
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *
from django.contrib.auth.decorators import login_required, user_passes_test

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
    grupos_permitidos=['superuser','adminusers'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def impactoporpe(request): 
    username = request.user.username 
    db = request.GET.get('dbstr')
    ippe = request.GET.get('strbuscado')
    conteovlans = []
    backuppe = [('','','','','')]
    equipo = [('','','','','','','','','','','','')]
    
    if db is not None and ippe is not None:
        equipo = obteneequipo(db,ippe)
        pais = obtenerpais(db,ippe)
        print
        resultadoarp = buscaarppe(db, ippe, pais)
        vlan_nombre = nombrevlanspe(ippe)
        conteovlans = contar_vlans_pe(resultadoarp, vlan_nombre)
        backuppe = buscabackups("temp_db",ippe)
    else:
        db = '-'
        ippe = '-'
        pais = '-'
        resultadoarp = []
        conteovlans = []
        backuppe = [('','','','','')]
        equipo = [('','','','','','','','','','','','')]
    
    lines = backuppe[0][3].splitlines()
    formatted_text = '\n'.join(lines)
    return render(request,'paginas/buscaimpactoporpe.html',
                {   'db':db,  
                    'ip':equipo[0][0],
                    'nemonico':equipo[0][1],
                    'ubicacion':equipo[0][10],
                    'snmp':equipo[0][7],
                    'pais':conviertepais(pais),
                    'conteovlans':conteovlans,
                    'resultadoarp':resultadoarp,
                    'backuppe':formatted_text,  
                    'dbs': esquemata_general(),
                    'user': username,
                })


