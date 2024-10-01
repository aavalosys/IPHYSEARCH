import os
import time
import requests
from django.http import JsonResponse
from django.shortcuts import render
from iphysearchapp.connect import *
from appsearch.busca_ips import *
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from netmiko import ConnectHandler
from django.db import connection


def pingdesdepevpn(request, ippe, ipcpe, vrf):             #HACE PING DESDE EL PE
    pehuawei = {
        "device_type": EQUIPOVPNBUSCAR,
        "host": ippe,
        "username": USERVPNBUSCAR,
        "password": PASSVPNBUCAR,  
        }
    res_ping = ''
    alert = 0
    command1 = "screen-length 0  temporary"
    try:
        with ConnectHandler(**pehuawei) as net_connect:
            net_connect.send_command(command1)
            time.sleep(2)
            command2 = "ping -b -m 20 -c 10 -vpn " + vrf + " " + ipcpe
            output2 = net_connect.send_command(command2, read_timeout=40)
            output2 = output2.replace("PING ", "", 1)
            if '!!!!!' in output2:
                output2 =  "PING EXITOSO : "+"ping -b -m 20 -c 8 -vpn " + vrf + "\n" + output2 + "--- COMPAÑEROS FAVOR VALIDAR RBS, Gracias"
                res_ping = output2
                alert = '1'   
            elif '.....' in output2:
                output2 =  "PING NO EXITOSO : "+command2 + "\n" + output2 +" SE DEBE VALIDAR LA CAPA 2 ..."
                res_ping = output2
                alert = '2'
            else:
                res_ping = 'Ocurrio un error, output invalido:' + command2
                alert = '3'
    except Exception as e:
            res_ping = 'Ocurrio un error al ejecutar ping desde el PE:' + str(e)
            alert = '3'
    return JsonResponse({"res_ping": res_ping, "alert": alert})


def detalleinterface(request, dbcpe, ipsw, interface):  #BUSCA DETALLE DE LA INTERFACE SELECCIONADA
    dispositivo = {
        "device_type": EQUIPOVPNBUSCAR,
        "host": ipsw,
        "username": USERVPNBUSCAR,
        "password": PASSVPNBUCAR,  
        }
    command1 = "screen-length 0  temporary"
    interface_bytes = bytes.fromhex(interface)
    interface = interface_bytes.decode('utf-8')
    try:
        with ConnectHandler(**dispositivo) as net_connect:
            net_connect.send_command(command1)
            time.sleep(2)
            command2 = "display  interface  " + interface +" | i state|Description|Distance|Power|time|rate|CRC"
            detalleInterface = net_connect.send_command(command2, read_timeout=30)
            
    except Exception as e:
            detalleInterface = 'Error al interrogar la interface'
            alert = '3'

    return JsonResponse({"detalleInterface": detalleInterface})


def buscaserviciomacajax(request, ippe, ipcpe, mac, vlan, interface, vrf, pais, dbcpe):  
    tipoalerta ="0" 
    vlan_f = int(vlan)
    if vlan_f < 4096:
        listar_mac = servicioesnormal(mac, vlan, pais, dbcpe)
    else:
        listar_mac = servicioespw(mac, vlan, dbcpe)
    alert = 0
    return JsonResponse({"listar_mac": listar_mac})


def detalleinterfaceAPI(dbcpe, ipsw, swinterface, swtch):   # SE DESACTIVA EL DETALLE DE LAS INTERFACES.
    detalleinter = 'X'
    try:
        if swtch == 1:    
            url = f"http://10.10.26.4:5000/api/getinterface/"
            data_to_send = [dbcpe, ipsw, swinterface]
            response = requests.post(url, json=data_to_send)
            if response.status_code == 200:
                datainterface = response.json()
                detalleinter = datainterface[1].split('\n')
    except Exception as e: 
        detalleinter = 'X'
    return detalleinter 



def actualizarbitacorasr():    #ACTUALIZA EL FRONT END
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador FROM"+
                     " bitacorasract WHERE estado = 3 and tipo = 10 ORDER BY contador DESC".format(dbrbs))
    listarsr=mycursor.fetchall()
    return listarsr


def actualizarbitacoact(): 
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador FROM"+
                     " bitacorasract WHERE estado = 3 and tipo = 20 ORDER BY contador DESC".format(dbrbs))
    listaract=mycursor.fetchall()
    return listaract


def sumasr():
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(codigosractividad) FROM "+
                     "{}.bitacorasract WHERE estado = 3 and tipo = 10".format(dbrbs))
    sumasr=mycursor.fetchall()
    sumacasosr = sumasr[0][0]
    return sumacasosr


def sumaact():
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(codigosractividad) FROM "+
                     "{}.bitacorasract WHERE estado = 3 and tipo = 20".format(dbrbs))
    sumaact=mycursor.fetchall()
    sumaact = sumaact[0][0]
    return sumaact


def obtenerpais(db,ip):                     #BUSCA EL PAIS DEL EQUIPO
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT pais FROM "+db+".equipos where ip like '%"+ip+"';")
    pais = mycursor.fetchall()
    print(ip)
    print ("------------------------------------------>")
    print(pais)
    print ("------------------------------------------>")
    print(db)
    pais = pais[0][0].lower()
    mydb.close()
    return pais

def conviertepais(pais):
    paises = {
        "gt": "Guatemala",
        "hn": "Honduras",
        "ni": "Nicaragua",
        "sv": "El Salvador",
        "cr": "Costa Rica"
    }
    return paises.get(pais.lower(), "País desconocido")

def nombrevlanspe(ippe):
    mydbvlan = conexion_dbown(DBNEWLOCAL) #BUSCA LAS VLAN EN EL PE L3
    mycursorvl = mydbvlan.cursor()
    mycursorvl.execute("SELECT vlan, nombrevlan  FROM  dbloip130324.vlans where ippevlan ='"+ippe+"'")
    vlan_nombre =  mycursorvl.fetchall()
    print (vlan_nombre)
    mydbvlan.close()
    return vlan_nombre

def obtenpeL3(dbinter, ip, pais):
    mydbpe =  conexion_dbnet(dbinter)  #BUSCA LA IP DEL L3
    mycursorpe = mydbpe.cursor()
    query = "SELECT ip FROM "+dbinter+".arp_"+pais+" WHERE ipcpe = '"+ip+"' AND vrf NOT LIKE '%LOBAL%' LIMIT 1 "
    mycursorpe.execute(query)
    ippe = mycursorpe.fetchall()
    if ippe:    
        ippe = ippe[0][0]
    mydbpe.close()
    return ippe

def obtenermacinterface(dbinter, ip, pais, interface):
    mydb =  conexion_dbnet(dbinter)      #TRAE LAS MAC APRENDIDAS
    mycursor = mydb.cursor()
    mycursor.execute("SELECT vlan, mac FROM "+dbinter+".mac_address_"+pais+" where ip ='"+ip+"' and interface like '%"+interface+"%'")
    totalmacinter = mycursor.fetchall()
    mydb.close()
    return totalmacinter


def buscaarppe(db, ip, pais): 
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM "+db+".arp_"+pais+" where ip = '"+ip+"';")
    resultadoarp = mycursor.fetchall()
    mydb.close()
    return resultadoarp


def contar_vlans_inter(ippe, dbinter, ip, pais, interface):

    vlan_nombre =  nombrevlanspe(ippe)                 #TRAE TODAS LAS VLAN DEL PE
    totalvlans = obtenermacinterface(dbinter, ip, pais, interface)  #TRAE LAS MAC APRENDIDAS

    vlan_nombre_dict = {vlan: nombrevlan for vlan, nombrevlan in vlan_nombre}
    tabla_mac_vlan = []

    for vlan, mac in totalvlans:
        nombrevlan = vlan_nombre_dict.get(vlan, 'Unknown')
        tabla_mac_vlan.append([mac, vlan, nombrevlan])

    vlan_count = {}
    for mac, vlan, nombrevlan in tabla_mac_vlan:
        if vlan in vlan_count:
            vlan_count[vlan][2] += 1
        else:
            vlan_count[vlan] = [vlan, nombrevlan, 1]

    conteo_vlan_mac = list(vlan_count.values())

    return conteo_vlan_mac, tabla_mac_vlan

def contar_vlans_pe(resultadoarp, vlan_nombre):
    vlan_count = {}
    for entry in resultadoarp:
        vlan = entry[3]
        if vlan in vlan_count:
            vlan_count[vlan] += 1
        else:
            vlan_count[vlan] = 1
    results = []

    for vlan, count in vlan_count.items():
        name = 'GLOBAL' if vlan == '0' else next((item[1] for item in vlan_nombre if item[0] == vlan), "Unknown")
        results.append([vlan, name, count])

    results.sort(key=lambda x: x[2], reverse=True)	
    
    return results

def obteneequipo(db,ip):                     #BUSCA EL PAIS DEL EQUIPO
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM "+db+".equipos where ip like '"+ip+"';")
    equipo = mycursor.fetchall()
    mydb.close()
    return equipo

def buscabackups(db,ip):                     #BUSCA EL PAIS DEL EQUIPO
    db = "temp_db"
    tablaname = "backups_ip"
    backupequipo  = []
    mydb =  conexion_dbbk(db)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM '+db+'.'+tablaname+' where  device_ip like "'+ ip + '";')
    backupequipo = mycursor.fetchall()
    mydb.close()
    return backupequipo