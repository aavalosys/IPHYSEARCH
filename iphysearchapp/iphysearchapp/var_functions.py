
from iphysearchapp.var_env import *
import mysql.connector 
from django.db import connection

def conexion_dbbk(DBBK):
    mydb = mysql.connector.connect(host= HOSTBK, user= USERBK, password=PASSWORDBK, database=DBBK)
    return  mydb

def conexion_dbnet(DB):
    mydb = mysql.connector.connect(host= HOST, user= USER, password=PASSWORD, database=DB)
    return  mydb

def conexion_dbown(DB):
    mydb = mysql.connector.connect(host= HOSTOWN, user= USEROWN, password=PASSWORDOWN, database=DBOWN)
    return  mydb

def esquemata():
    cursor = connection.cursor()
    cursor.execute('select count(SCHEMA_NAME) from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'"')
    dbs = [int(tupla[0]) for tupla in cursor.fetchall()] #cuantas dbs encontro en schema_name
    cursor.execute('select SCHEMA_NAME  from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'" order by SCHEMA_NAME desc limit '+
                   str(dbs[0])+' offset 2')
    esquemas = [str(tupla[0]) for tupla in cursor.fetchall()]
    return esquemas

