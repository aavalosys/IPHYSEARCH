
import time
from iphysearchapp.var_env import *
from netmiko import ConnectHandler
from django.http import JsonResponse
import mysql.connector 
from django.db import connection
import requests
import subprocess
import platform

def conexion_dbbk(DBBK):  #CONEXION BK 10.10.26.5
    mydb = mysql.connector.connect(host= HOSTBK, user= USERBK, password=PASSWORDBK, database=DBBK, charset="utf8mb4")
    return  mydb
 
def conexion_dbnet(DB):  #CONEXION DATA 10.10.26.4
    mydb = mysql.connector.connect(host= HOST, user= USER, password=PASSWORD, database=DB, charset="utf8mb4")
    return  mydb

def conexion_dbown(DBOWN): #CONEXION LOCAL 10.10.26.7
    mydb = mysql.connector.connect(host= HOSTOWN, user= USEROWN, password=PASSWORDOWN, database=DBOWN, charset="utf8mb4")
    return  mydb


def esquemata():
    cursor = connection.cursor()
    cursor.execute('select count(SCHEMA_NAME) from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'"')
    dbs = [int(tupla[0]) for tupla in cursor.fetchall()] 
    cursor.execute('select SCHEMA_NAME  from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'" order by SCHEMA_NAME desc limit '+
                   str(dbs[0])+' offset 2')
    esquemas = [str(tupla[0]) for tupla in cursor.fetchall()]
    return esquemas

def esquematabackup():
    cursor = connection.cursor()
    cursor.execute('select count(SCHEMA_NAME) from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'"')
    dbs = [int(tupla[0]) for tupla in cursor.fetchall()] 
    cursor.execute('select SCHEMA_NAME  from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'" order by SCHEMA_NAME desc limit '+
                   str(dbs[0])+' offset 2')
    esquemas = [str(tupla[0]) for tupla in cursor.fetchall()]
    return esquemas

def usuariolog():
    usuario = "navalos"
    return usuario

def actualizarbitacorasr(): 
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

def buscapaises():
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *")
    paises=mycursor.fetchall()
    return paises

def vendors():
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *")
    vendors=mycursor.fetchall()
    return vendors

def nombrevlan():
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *")
    vendors=mycursor.fetchall()
    return vendors

def nombrevlan():
    dbrbs = DBNEWLOCAL
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *")
    vlans=mycursor.fetchall()
    return vlans

def pingdesdepevpn(request, ippe, ipcpe, mac, vlan, vrf, pais, dbcpe):
    pehuawei = {
        "device_type": EQUIPOVPNBUSCAR,
        "host": ippe,
        "username": USERVPNBUSCAR,
        "password": PASSVPNBUCAR,  
        }
    res_ping = ''
    command1 = "terminal lenght 0"

    try:
        with ConnectHandler(**pehuawei) as net_connect:
            output1 = net_connect.send_command(command1)
            time.sleep(2)
            command2 = "ping -b -m 20 -c 10 -vpn " + vrf + " " + ipcpe
            output2 = net_connect.send_command(command2)
            print ("Respuesta desde el PE: "+output2)
            res_ping = output2
            tipoalerta = '1'
    except Exception as e:
            res_ping = 'Ocurrio un error:' + str(e)
            tipoalerta = '2'
    return JsonResponse({"res_ping": res_ping})

def elementoesup(ipsw):
    second_element = 'X'
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', '-W', '1', ipsw]
    resultado = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if resultado.returncode == 0:
        second_element = 'up'
        print('resultado ping--- '+second_element)
        return second_element 
    else:
        second_element = 'down'
        print('resultado ping--- '+second_element)
        return second_element
  
    return second_element