from iphysearchapp.var_env import *
from django.db import connection
import time
import mysql.connector 

def conexion_dbbk(DBBK):    #CONEXION BK 10.10.26.5 
    mydb = mysql.connector.connect(host= HOSTBK, user= USERBK, password=PASSWORDBK, database=DBBK, charset="utf8mb4")
    return  mydb
 
def conexion_dbnet(DB):     #CONEXION DATA 10.10.26.4
    mydb = mysql.connector.connect(host= HOST, user= USER, password=PASSWORD, database=DB, charset="utf8mb4")
    return  mydb

def conexion_dbown(DBOWN):  #CONEXION LOCAL 10.10.26.7
    mydb = mysql.connector.connect(host= HOSTOWN, user= USEROWN, password=PASSWORDOWN, database=DBOWN, charset="utf8mb4")
    return  mydb

def esquemata():            #LLENA EL SELECTLIST DE TODAS LAS PAGINAS
    cursor = connection.cursor()
    cursor.execute('select count(SCHEMA_NAME) from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'"')
    dbs = [int(tupla[0]) for tupla in cursor.fetchall()] 
    cursor.execute('select SCHEMA_NAME  from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+
                   '" order by SCHEMA_NAME desc limit '+
                   str(dbs[0])+' offset 3')
    esquemas = [str(tupla[0]) for tupla in cursor.fetchall()]
    return esquemas

def esquematabackup():      #LLENA EL SELECTLIST DE HOME
    cursor = connection.cursor()
    cursor.execute('select count(SCHEMA_NAME) from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'"')
    dbs = [int(tupla[0]) for tupla in cursor.fetchall()] 
    cursor.execute('select SCHEMA_NAME  from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+
                   '" order by SCHEMA_NAME desc limit '+
                   str(dbs[0])+' offset 2')
    esquemas = [str(tupla[0]) for tupla in cursor.fetchall()]
    return esquemas

def usuariolog():               #VERIFICA USUARIO
    usuario = "navalos"
    return usuario