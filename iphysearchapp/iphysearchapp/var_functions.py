
from iphysearchapp.var_env import *
import mysql.connector 
from django.db import connection

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

def actualizarbitacorasr(): 
    dbrbs = "dbloip130324"
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador FROM"+
                     " bitacorasract WHERE estado = 3 and tipo = 10 ORDER BY contador DESC".format(dbrbs))
    listarsr=mycursor.fetchall()
    return listarsr

def actualizarbitacoact(): 
    dbrbs = "dbloip130324"
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador FROM"+
                     " bitacorasract WHERE estado = 3 and tipo = 20 ORDER BY contador DESC".format(dbrbs))
    listaract=mycursor.fetchall()
    return listaract

def sumasr():
    dbrbs = "dbloip130324"
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(codigosractividad) FROM "+
                     "{}.bitacorasract WHERE estado = 3 and tipo = 10".format(dbrbs))
    sumasr=mycursor.fetchall()
    sumacasosr = sumasr[0][0]
    return sumacasosr

def sumaact():
    dbrbs = "dbloip130324"
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(codigosractividad) FROM "+
                     "{}.bitacorasract WHERE estado = 3 and tipo = 20".format(dbrbs))
    sumaact=mycursor.fetchall()
    sumaact = sumaact[0][0]
    return sumaact