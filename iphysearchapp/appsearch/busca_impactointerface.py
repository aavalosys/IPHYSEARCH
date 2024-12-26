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
    grupos_permitidos=['superuser','adminusers', 'especialistas', 'usuariosvista'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def impactointerfaces(request):
    username = request.user.username 
    db = request.GET.get('dbstr')
    ip = request.GET.get('strbuscado') 
    pais = '-'
    interface='-'
    tabla_mac_vlan='-'
    conteo_vlan_mac='-'

    if db is not None and ip is not None:
        listadointerfaces = buscainterfaces(db, ip)
        pais = obtenerpais(db,ip)
    else:
        ip = '-'
        listadointerfaces = ''
        pais = '-'
        interface='-'
        db = '-'
        tabla_mac_vlan='-'
        conteo_vlan_mac='-'
    return render(request,'paginas/buscaimpactointerface.html',
                {   'db':db,  
                    'ip':ip,
                    'pais':pais,
                    'interface':interface, 
                    'tabla_mac_vlan':tabla_mac_vlan,
                    'conteo_vlan_mac':conteo_vlan_mac,
                    'listadointerfaces':listadointerfaces,   
                    'dbs': esquemata_general(),
                    'user': username,
                })

@login_required
@grupo_requerido(
    grupos_permitidos=['usuariosvista', 'intermedio', 'administradores'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def verimpactointerface(request, ip, no, dbinter, pais):
    username = request.user.username 
    interface='-'
    tabla_mac_vlan='-'
    conteo_vlan_mac='-'
    listadointerfaces = buscainterfaces(dbinter, ip)

    for inter in listadointerfaces:
        if int(inter[0])==int(no):
            interface = inter[2]
            break
        else:
            interface='--'

    ippe = obtenpeL3(dbinter, ip, pais)         #BUSCA LA IP DEL L3

    conteo_vlan_mac, tabla_mac_vlan = contar_vlans_inter(ippe, dbinter, ip, pais, interface)

    return render(request,'paginas/buscaimpactointerface.html',
                {   'db':dbinter,  
                    'ip':ip,
                    'pais':pais,
                    'interface':interface, 
                    'listadointerfaces':listadointerfaces,
                    'tabla_mac_vlan':tabla_mac_vlan,
                    'conteo_vlan_mac':conteo_vlan_mac,   
                    'dbs': esquemata_general(),
                    'user': username,
                })

    
def buscainterfaces(db, idtxtabuscar): 
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ROW_NUMBER() OVER (ORDER BY resultado.ip) AS correlativo, resultado.*, '" + 
                    db + "' AS db FROM ( SELECT * FROM " +
                    db + ".int_gt UNION  SELECT * FROM "+ 
                    db + ".int_sv UNION  SELECT * FROM "+ 
                    db + ".int_hn UNION  SELECT * FROM "+ 
                    db + ".int_ni UNION  SELECT * FROM "+ 
                    db + ".int_cr UNION  SELECT * FROM "+
                    db + ".int_xt ) AS resultado WHERE resultado.ip LIKE '"+
                    idtxtabuscar + "' and description not like '%LIBRE%' and interface not like '%NULL%'")
    resultadointerfaces = mycursor.fetchall()
    mydb.close()
    return resultadointerfaces


  

    


