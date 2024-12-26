import logging
import os
import requests
from ping3 import ping
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func  import *
from django.contrib.auth.decorators import login_required, user_passes_test
from models import Nodob 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def grupo_requerido(grupos_permitidos, respuesta, errordes, errores):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=grupos_permitidos).exists():
                return view_func(request, *args, **kwargs)
            else:
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
def buscaips(request):
    username = request.user.username  
    res_ping = "Bienvenidos al APP WEB, verificación de elementos de red"
    tipoalerta = "0"
    limpiaINFO()
    if 'buscar_rbs' in request.GET:    #SI ES BOTON IDRBS  
        return buscarbs(request)
    elif 'buscar_ip' in request.GET:   #SI ES BOTON IPCPE
        return buscar_ip(request)
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': [],
                    'listarips':[],
                    'listar_mac': [],
                    'dbs': esquemata_general(), 
                    'tipoalerta':tipoalerta,
                    'res_ping': res_ping,
                    'user': username, 
                    'INFOR': INFOR})

@login_required
@grupo_requerido(
    grupos_permitidos=['usuariosvista', 'intermedio', 'administradores'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def buscarbs(request):      
    username = request.user.username
    limpiaINFO()        
    res_ping = "Este es el resultado de la Busqueda de elementos por ID"
    tipoalerta ="0"
    dbrbs = request.GET.get('idtxtdbrbs')
    textrbs = request.GET.get('idrbs').lstrip()
    listarbs = buscarbsid(dbrbs, textrbs)
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': listarbs,
                   'listaips': [],
                   'listar_mac': [],
                   'dbs': esquemata_general(), 
                   'tipoalerta':tipoalerta,
                   'res_ping': res_ping,
                   'user': username,  
                   'INFOR': INFOR}) 


@login_required
@grupo_requerido(
    grupos_permitidos=['usuariosvista', 'intermedio', 'administradores'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def buscar_ip(request):       #BUSQUEDA DE LA L3
    username = request.user.username
    limpiaINFO()
    res_ping = "Este es el resultado de la IP del elemento y las VPNs donde se observa."
    tipoalerta ="0"        
    dbcpe = request.GET.get('dbcpe')
    textip = request.GET.get('ipcpe').lstrip()
    return render(request, "paginas/buscaips.html", 
                      {'listarbs': buscarbsip(dbcpe, textip),
                       'listaips': buscaipcpe(dbcpe, textip),
                       'listar_mac': [], 
                       'dbs': esquemata_general(),
                       'tipoalerta':tipoalerta,
                       'res_ping': res_ping,
                       'user': username,
                       'INFO':INFOR,})


def buscarbsid(dbrbs, idrbstxt):         
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    pararbs = ('%' + idrbstxt + '%',)
    consulta_sql = "SELECT * FROM {}.nodob WHERE nodoid LIKE %s".format(dbrbs)
    mycursor.execute(consulta_sql, pararbs)    
    listarbsid = mycursor.fetchall()
    return listarbsid


def buscarbsip(dbrbs, rbsip):         
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    pararbs = ('' + rbsip + '',)
    consulta_sql = "SELECT * FROM {}.nodob WHERE ip LIKE %s".format(dbrbs)
    mycursor.execute(consulta_sql, pararbs)    
    listarbsip = mycursor.fetchall()
    mydb.close()
    return listarbsip
     

def buscaipcpe(dbcpe, textip):
    paracpe = ('%' + textip + '',)            #BUSCA L3 DISPOSITIVO
    mydb =  conexion_dbnet(dbcpe)
    mycursor = mydb.cursor()
    query = """ SELECT * FROM ( 
                   SELECT *, 'gt' AS table_name FROM {}.arp_gt
                   UNION ALL
                   SELECT *, 'sv' AS table_name FROM {}.arp_sv
                   UNION ALL
                   SELECT *, 'hn' AS table_name FROM {}.arp_hn
                   UNION ALL
                   SELECT *, 'ni' AS table_name FROM {}.arp_ni 
                   UNION ALL
                   SELECT *, 'cr' AS table_name FROM {}.arp_cr
                ) AS resultado WHERE resultado.ipcpe LIKE %s """.format(dbcpe, dbcpe, dbcpe, dbcpe, dbcpe)
    mycursor.execute(query, paracpe)
    resultados = mycursor.fetchall()
    mydb.close()
    listaips = [(resultado + (dbcpe,)) for resultado in resultados]
    return listaips


def servicioesnormal(mac, vlan, pais, dbcpe):
    mydb =  conexion_dbnet(dbcpe)
    mycursor = mydb.cursor() 
    mycursor.execute("SELECT m.*, i.description FROM "+dbcpe+".mac_address_"+pais+
    " m JOIN "+dbcpe+".int_"+pais+" i ON m.ip = i.ip AND m.interface = i.interface JOIN "+
    "(SELECT COUNT(m.count) as cnt FROM "+dbcpe+".mac_address_"+pais+" m  JOIN "+dbcpe+
    ".int_"+pais+" i ON m.ip = i.ip AND m.interface = i.interface WHERE m.mac = '"+mac+
    "' AND m.vlan = "+vlan+") mycount ON 1=1 WHERE  m.mac = '"+mac+"' AND m.vlan = "+vlan+
    " AND (((count = 0) AND (mycount.cnt = 1)) OR ((count > 0) AND (mycount.cnt > 0))) ORDER BY m.count asc")
    resultados = mycursor.fetchall()
    resultados_es = [(resultado + (elementoesup(resultado[0]), indice,)) for indice, resultado in enumerate(resultados)]
    mydb.close()
    return resultados_es


def servicioespw(mac, subvlan, dbcpe):
    mydb =  conexion_dbnet(dbcpe)
    mycursor = mydb.cursor()
    paracpe = ('%' + mac,)
    mycursor.execute(" ".format(dbcpe), mac)
    resultados = mycursor.fetchall()
    mydb.close()
    listapws = [(ip, mac, vlan, interface, count) 
                for (ip, mac, vlan, interface, count) in resultados 
                if subvlan in str(vlan)]
    return listapws


def elementoesup(ipsw):
    try:
        second_element = 'X'
        success = 0 
        for _ in range(4):
            response = ping(ipsw, timeout=2)  # Tiempo de espera de 2 segundos
            if response is not None:
                success += 1
        if success > 0:
            second_element = 'Up'
        return second_element
    except Exception as e:
        return 'X'


def limpiaINFO():
    INFOR[0][1] = 'PRIMERA COSA'
    INFOR[0][2] = 'SEGUNDA COSA '
    INFOR[1][1] = 'TERCERA COSA'
    return 0


def buscaserviciomacajax(request, ippe, ipcpe, mac, vlan, interface, vrf, pais, dbcpe):  
    listar_mac=[] 
    vlan_f = int(vlan)
    if vlan_f < 4096:
        listar_mac = servicioesnormal(mac, vlan, pais, dbcpe)
    else:
        print("LA VLAN ES MAYOR A 4096")
        #listar_mac = servicioespw(mac, vlan, dbcpe)
    alert = 0
    return JsonResponse({"listar_mac": listar_mac})

 