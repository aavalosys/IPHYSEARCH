from django.shortcuts import render
import requests
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

def buscaips(request):
    
    if 'buscar_rbs' in request.GET:     #SI ES EN BUSCAR RBS
        return buscarbs(request)
    elif 'buscar_ip' in request.GET:        #SI ES EN BUSCAR
        dbcpe = request.GET.get('dbcpe')
        textcpe = request.GET.get('ipcpe')
        return render(request, "paginas/buscaips.html", 
                      {'listarbs': buscarbsfrom(dbcpe, textcpe),
                       'listaips': buscacaipcpe(dbcpe, textcpe), 
                       'dbs': esquemata(),
                       'infor': INFOR})
    return render(request, "paginas/buscaips.html", 
                  {'dbs': esquemata(), 
                   'infor': INFOR})

def buscarbs(request):          #BUSCA NEMONICO DISPOSITIVO
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
                   'dbs': esquemata(), 
                   'infor': "entro a rbs"}) 

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
    vlan_f = int(vlan)
    if vlan_f < 4096:
        listar_mac = servicioesnormal(mac, vlan, pais, dbcpe)
    else:
        listar_mac = servicioespw(mac, vlan, dbcpe)
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': buscarbsfrom(dbcpe,ipcpe),
                   'listaips':buscacaipcpe(dbcpe, ipcpe), 
                   'listar_mac': listar_mac, 
                   'dbs': esquemata(), 
                   'infor': INFOR})

def servicioesnormal(mac, vlan, pais, dbcpe):
    mydb =  conexion_dbnet(dbcpe)
    mycursor = mydb.cursor()
    tiposerv = 0
    if tiposerv > 0:
        print ("EN SERVICIO 0")
    elif tiposerv == 1:
        print ("<<<<<<<<<<<<<<<<<< BUSCANDO UN SERVICIO CONVENCIONAL >>>>>>>>>>>>>>>>>>>>>>>")
    elif tiposerv == 0:  
        mycursor.execute("SELECT m.*, i.description FROM "+dbcpe+".mac_address_"+pais+
        " m JOIN "+dbcpe+".int_"+pais+" i ON m.ip = i.ip AND m.interface = i.interface JOIN "+
        "(SELECT COUNT(m.count) as cnt FROM "+dbcpe+".mac_address_"+pais+" m  JOIN "+dbcpe+
        ".int_"+pais+" i ON m.ip = i.ip AND m.interface = i.interface WHERE m.mac = '"+mac+
        "' AND m.vlan = "+vlan+") mycount ON 1=1 WHERE  m.mac = '"+mac+"' AND m.vlan = "+vlan+
        " AND (((count = 0) AND (mycount.cnt = 1)) OR ((count > 0) AND (mycount.cnt > 0))) ORDER BY m.count asc")
        resultados = mycursor.fetchall()
        resultados_es = [(resultado + (elementoesup(resultado[0]), intdetail(dbcpe, resultado[0], resultado[3] ),indice,)) for indice, resultado in enumerate(resultados)]
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
    mydb =  conexion_dbnet(DBESUP)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(DEVISUP, ('%' + ipsw,))
        url = f"http://10.10.26.4:5000/api/ping/"
        response = requests.post(url, json=ipsw)
        if response.status_code == 200:
            second_element = response.json()[1]
            return second_element
        else:
            second_element = 'X'
            return second_element
    except Exception as e:
        second_element = 'X'
        return second_element
  
def elementoesping(request, ippe, ipcpe, mac, vlan, vrf, pais, dbcpe):
    try:
        url = f"http://10.10.26.4:5000/api/getpingvrf/"
        data_to_send = [dbcpe, ippe, vrf, ipcpe]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            resultado = response.json()
            res_ping = resultado[1]
            print(res_ping)
            res_ping = res_ping.replace("PING", " ")
            res_ping = 'ping -b -m 50 -c 5 -vpn-instance ' + vrf + ' ' + res_ping
        else:
            res_ping = 'Ooops ocurrio un error.... Código de respuesta no es 200'
    except Exception as e:
        resultado = 'Ooops ocurrio un error.... Excepcion en la API /api/getpingvrf/'
        return resultado

    return render(request, "paginas/buscaips.html", 
                  {'listarbs': buscarbsfrom(dbcpe,ipcpe),
                   'listaips': buscacaipcpe(dbcpe, ipcpe), 
                   'dbs': esquemata(),
                   'res_ping': res_ping,
                   'infor': INFOR})
    
def intdetail(dbcpe, ipsw, swinterface):
    try:
        url = f"http://10.10.26.4:5000/api/getinterface/"
        data_to_send = [dbcpe, ipsw, swinterface]
        response = requests.post(url, json=data_to_send)

        if response.status_code == 200:
            datainterface = response.json()
            detalleinter = datainterface[1].split('\n')
        else:
            detalleinter = 'X'
        return detalleinter
    except Exception as e:
        detalleinter = 'X'
        return detalleinter

