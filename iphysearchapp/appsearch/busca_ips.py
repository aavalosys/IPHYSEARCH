from django.shortcuts import render
import requests
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *


def buscaips(request):
    res_ping = "Bienvenidos al APP WEB, verificación de elementos de red"
    tipoalerta = "0"
    limpiaINFO()
    if 'buscar_rbs' in request.GET:      
        return buscarbs(request)
    elif 'buscar_ip' in request.GET:      
        return buscar_ip(request)
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': [],
                    'listarips':[],
                    'listar_mac': [],
                    'dbs': esquemata(),
                    'user': usuariolog(),
                    'tipoalerta':tipoalerta,
                    'res_ping': res_ping, 
                    'INFOR': INFOR})

def buscarbs(request):
    limpiaINFO()        
    res_ping = "Este es el resultado de la Busqueda de elementos por ID"
    tipoalerta ="0"
    dbrbs = request.GET.get('dbrbs')
    textrbs = request.GET.get('idrbs')
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': buscarbsid(dbrbs, textrbs),
                   'listaips': [],
                   'listar_mac': [],
                   'dbs': esquemata(), 
                   'user': usuariolog(),
                   'tipoalerta':tipoalerta,
                   'res_ping': res_ping,
                   'INFOR': INFOR}) 

def buscar_ip(request):
    limpiaINFO()
    res_ping = "Este es el resultado de la IP del elemento y las VPNs donde se observa."
    tipoalerta ="0"        
    dbcpe = request.GET.get('dbcpe')
    textip = request.GET.get('ipcpe')
    return render(request, "paginas/buscaips.html", 
                      {'listarbs': buscarbsip(dbcpe, textip),
                       'listaips': buscaipcpe(dbcpe, textip),
                       'listar_mac': [], 
                       'dbs': esquemata(),
                       'user': usuariolog(),
                       'tipoalerta':tipoalerta,
                       'res_ping': res_ping,
                       'INFO':INFOR,})

def buscaserviciomac (request, ippe, ipcpe, mac, vlan, vrf, pais, dbcpe):
    limpiaINFO()
    switch = 0  #DESACTIVA EL DETALLE DE LAS INTERFACES
    res_ping = "Este es el resultado del trayecto L2 por donde se observa la MAC del elemento"
    tipoalerta ="0"
    vlan_f = int(vlan)
    if vlan_f < 4096:
        listar_mac = servicioesnormal(mac, vlan, pais, dbcpe, switch)
    else:
        listar_mac = servicioespw(mac, vlan, dbcpe)
    
    INFOR[0][1] = vrf
    INFOR[0][2] = ipcpe
    INFOR[1][1] = mac

    return render(request, "paginas/buscaips.html", 
                  {'listarbs': buscarbsip(dbcpe,ipcpe),
                   'listaips':buscaipcpe(dbcpe, ipcpe), 
                   'listar_mac': listar_mac,
                   'dbs': esquemata(),
                   'user': usuariolog(),
                   'tipoalerta':tipoalerta,
                   'res_ping': res_ping, 
                   'INFOR': INFOR})

def elementoesping(request, ippe, ipcpe, mac, vlan, vrf, pais, dbcpe):
    limpiaINFO()
    try:
        url = f"http://10.10.26.4:5000/api/getpingvrf/"
        data_to_send = [dbcpe, ippe, vrf, ipcpe]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            resultado = response.json()
            res_ping = resultado[1]
            if "!!!!!" in res_ping:
                tipoalerta = '1'
            elif "....." in res_ping:
                tipoalerta ='3'
            else:
                tipoalerta= '2'
        else:
            res_ping ='ERR0R '+str(response.status_code) + ' PROBLEMA EN LA API.'
            tipoalerta = '2'

    except Exception as e:
        res_ping = 'Excepcion en la API = ' + e
        tipoalerta = '0'

    INFOR[0][1] = vrf
    INFOR[0][2] = ipcpe
    INFOR[1][1] = mac
    
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': buscarbsip(dbcpe,ipcpe),
                   'listaips': buscaipcpe(dbcpe, ipcpe),
                   'listar_mac': servicioesnormal(mac, vlan, pais, dbcpe, 0),
                   'dbs': esquemata(),
                   'user': usuariolog(),
                   'tipoalerta':tipoalerta,
                   'res_ping': res_ping,
                   'INFOR':INFOR,})



def buscarbsid(dbrbs, textrbs):         
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    pararbs = ('%' + textrbs + '%',)
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
    paracpe = ('%' + textip + '%',)            #BUSCA L3 DISPOSITIVO
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

def servicioesnormal(mac, vlan, pais, dbcpe, switch):
    mydb =  conexion_dbnet(dbcpe)
    mycursor = mydb.cursor()
    tiposerv = 0
    if tiposerv > 0:
        print ("EN SERVICIO 0")
    elif tiposerv == 1:
        print ("EN SERVICIO 1") 
    elif tiposerv == 0:  
        mycursor.execute("SELECT m.*, i.description FROM "+dbcpe+".mac_address_"+pais+
        " m JOIN "+dbcpe+".int_"+pais+" i ON m.ip = i.ip AND m.interface = i.interface JOIN "+
        "(SELECT COUNT(m.count) as cnt FROM "+dbcpe+".mac_address_"+pais+" m  JOIN "+dbcpe+
        ".int_"+pais+" i ON m.ip = i.ip AND m.interface = i.interface WHERE m.mac = '"+mac+
        "' AND m.vlan = "+vlan+") mycount ON 1=1 WHERE  m.mac = '"+mac+"' AND m.vlan = "+vlan+
        " AND (((count = 0) AND (mycount.cnt = 1)) OR ((count > 0) AND (mycount.cnt > 0))) ORDER BY m.count asc")
        resultados = mycursor.fetchall()
        resultados_es = [(resultado + (elementoesup(resultado[0]), detalleinterface(dbcpe, resultado[0], resultado[3],switch ),indice,)) for indice, resultado in enumerate(resultados)]
        print(resultados_es)
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
    second_element = 'X'
    mydb =  conexion_dbnet(DBESUP)
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT status FROM uptime WHERE uptime.ip LIKE %s", ('%' + ipsw,))
        url = f"http://10.10.26.4:5000/api/ping/"
        response = requests.post(url, json=ipsw)
        if response.status_code == 200:
            second_element = response.json()[1]
    except Exception as e:
        second_element = 'X'
    return second_element
    

def detalleinterface(dbcpe, ipsw, swinterface,swtch):
    detalleinter = 'X'
    try:
        if swtch == 1:   # SE DESACTIVA EL DETALLE DE LAS INTERFACES. 
            url = f"http://10.10.26.4:5000/api/getinterface/"
            data_to_send = [dbcpe, ipsw, swinterface]
            response = requests.post(url, json=data_to_send)
            if response.status_code == 200:
                datainterface = response.json()
                detalleinter = datainterface[1].split('\n')
    except Exception as e: 
        detalleinter = 'X'
    return detalleinter

def limpiaINFO():
    INFOR[0][1] = ''
    INFOR[0][2] = ''
    INFOR[1][1] = ''
    return


