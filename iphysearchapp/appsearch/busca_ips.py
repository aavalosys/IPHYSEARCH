from django.shortcuts import render
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
                      {'listaips': buscacaipcpe(dbcpe, textcpe), 
                       'dbs': esquemata(),
                       'infor': INFOR})
    return render(request, "paginas/buscaips.html", 
                  {'dbs': esquemata(), 
                   'infor': INFOR})

def buscarbs(request):      #BUSCA NEMONICO DISPOSITIVO
    dbrbs = request.GET.get('dbrbs')
    textrbs = request.GET.get('idrbs')
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    pararbs = ('%' + textrbs + '%',)
    mycursor.execute(RBSTXT.format(dbrbs), pararbs)
    listarbs = mycursor.fetchall()
    mydb.close()
    return render(request, "paginas/buscaips.html", 
                  {'listarbs': listarbs, 
                   'dbs': esquemata(), 
                   'infor': "entro a rbs"})
    
def buscacaipcpe(dbcpe, textcpe):       #BUSCA L3 DISPOSITIVO
    mydb =  conexion_dbnet(dbcpe)
    mycursor = mydb.cursor()
    paracpe = ('%' + textcpe,)
    mycursor.execute(CPETXT.format(dbcpe, dbcpe, dbcpe, dbcpe, dbcpe), paracpe)
    resultados = mycursor.fetchall()
    mydb.close()
    listaips = [(resultado + (dbcpe,)) for resultado in resultados]
    return listaips

def buscaserviciomac (request, ipcpe, mac, vlan, pais, dbcpe):
    vlan_f = int(vlan)
    if vlan_f < 4096:
        listar_mac = servicioesnormal(mac, vlan, pais, dbcpe)
    else:
        listar_mac = servicioespw(mac, vlan, dbcpe)
    return render(request, "paginas/buscaips.html", 
                  {'listaips':buscacaipcpe(dbcpe, ipcpe), 
                   'listar_mac': listar_mac, 'dbs': esquemata(), 
                   'infor': INFOR})

def servicioesnormal(mac, vlan, pais, dbcpe):
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
        ".int_"+pais+" i ON m.ip = i.ip AND m.interface = i.interface WHERE m.mac LIKE '%"+mac+
        "%' AND m.vlan = "+vlan+") mycount ON 1=1 WHERE  m.mac LIKE '%"+mac+"%' AND m.vlan = "+vlan+
        " AND (((count = 0) AND (mycount.cnt = 1)) OR ((count > 0) AND (mycount.cnt > 0))) ORDER BY m.count asc")


        resultados = mycursor.fetchall()
        resultados_es = [(resultado + (elementoesup(resultado[0]),)) for resultado in resultados]
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
        deviceisup = mycursor.fetchall()[0]
    except Exception as e:
        deviceisup = "X"
    return deviceisup[0].strip("('')")

