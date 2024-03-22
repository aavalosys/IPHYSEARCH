from django.shortcuts import render
import requests
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *


def buscaips(request):
    res_ping = ""
    tipoalerta = "1"
    if 'buscar_rbs' in request.GET:       #SI ES EN BUSCAR RBS
        return buscarbs(request)
    elif 'buscar_ip' in request.GET:       #SI ES EN BUSCAR
        return busbuscar_ip(request)
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': [],
                    'listarips':[],
                    'res_ping': "",
                    'dbs': esquemata(),
                    'user': usuariolog(),
                    'tipoalerta':tipoalerta,
                    'res_ping': res_ping, 
                    'INFOR': INFOR})


def buscarbs(request):          #BUSCA NEMONICO DISPOSITIVO
    res_ping = ""
    tipoalerta ="0"
    dbrbs = request.GET.get('dbrbs')
    textrbs = request.GET.get('idrbs')
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    pararbs = ('%' + textrbs + '%',)
    mycursor.execute("SELECT * FROM {}.nodob WHERE nodoid LIKE %s".format(dbrbs), pararbs)
    listarbs = mycursor.fetchall()
    mydb.close()
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': listarbs,
                   'listarsr':[],
                   'res_ping': "",
                   'dbs': esquemata(), 
                   'user': usuariolog(),
                   'tipoalerta':tipoalerta,
                   'res_ping': res_ping,
                   'INFOR': INFOR}) 

def busbuscar_ip(request): 
    res_ping = ""
    tipoalerta ="0"        
    dbcpe = request.GET.get('dbcpe')
    textcpe = request.GET.get('ipcpe')
    listarbs = buscarbsfrom(dbcpe, textcpe)
    listaips = buscacaipcpe(dbcpe, textcpe)
    return render(request, "paginas/buscaips.html", 
                      {'listarbs': listarbs,
                       'listaips': listaips, 
                       'dbs': esquemata(),
                       'user': usuariolog(),
                       'tipoalerta':tipoalerta,
                       'res_ping': res_ping,
                       'INFO':INFOR,})

def buscarbsfrom(dbrbs, textcpe):          #BUSCA NEMONICO DISPOSITIVO
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    pararbs = ('%' + textcpe + '',)
    mycursor.execute("SELECT * FROM {}.nodob WHERE ip LIKE %s".format(dbrbs), pararbs)
    listarbs = mycursor.fetchall()
    mydb.close()
    return listarbs
    
def buscacaipcpe(dbcpe, textcpe):            #BUSCA L3 DISPOSITIVO
    mydb =  conexion_dbnet(dbcpe)
    mycursor = mydb.cursor()
    paracpe = ('%' + textcpe,) 
    mycursor.execute(CPETXT.format(dbcpe, dbcpe, dbcpe, dbcpe, dbcpe), paracpe)
    resultados = mycursor.fetchall()
    mydb.close()
    listaips = [(resultado + (dbcpe,)) for resultado in resultados]
    return listaips


def buscaserviciomac (request, ippe, ipcpe, mac, vlan, vrf, pais, dbcpe):
    switch = 0  #DESACTIVA EL DETALLE DE LA ACTIVIDAD
    res_ping = ""
    tipoalerta ="0"
    vlan_f = int(vlan)
    if vlan_f < 4096:
        listar_mac = servicioesnormal(mac, vlan, pais, dbcpe,switch)
    else:
        listar_mac = servicioespw(mac, vlan, dbcpe)
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': buscarbsfrom(dbcpe,ipcpe),
                   'listaips':buscacaipcpe(dbcpe, ipcpe), 
                   'listar_mac': listar_mac,
                   'listarsr':[],
                   'listaotros':[],
                   'sumasr':10,
                   'sumaotros':15,
                   'res_ping': "", 
                   'dbs': esquemata(),
                   'user': usuariolog(),
                   'tipoalerta':tipoalerta,
                   'res_ping': res_ping, 
                   'INFOR': INFOR})

def servicioesnormal(mac, vlan, pais, dbcpe,switch):
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
    mycursor.execute(PATHTXT.format(dbcpe), mac)
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
  
def elementoesping(request, ippe, ipcpe, vrf, pais, dbcpe):
    try:
        url = f"http://10.10.26.4:5000/api/getpingvrf/"
        data_to_send = [dbcpe, ippe, vrf, ipcpe]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            resultado = response.json()
            res_ping = resultado[1]
            if "!!!!!" in res_ping:
                tipoalerta = '0'
            elif "....." in res_ping:
                tipoalerta ='3'
        else:
            res_ping = 'Código de respuesta = ' + response.status_code
            tipoalerta = '1'
    except Exception as e:
        resultado = 'Excepcion en la API /api/getping/ = ' + e

    return render(request, "paginas/buscaips.html", 
                  {'listarbs': buscarbsfrom(dbcpe,ipcpe),
                   'listaips': buscacaipcpe(dbcpe, ipcpe),
                   'dbs': esquemata(),
                   'user': usuariolog(),
                   'tipoalerta':tipoalerta,
                   'INFOR':INFOR,
                   'res_ping': res_ping,})
    

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
        return detalleinter

