
from iphysearchapp.var_env import *
import mysql.connector 
from django.db import connection

def conexion_dbbk(DBBK):
    mydb = mysql.connector.connect(host= HOSTBK, user= USERBK, password=PASSWORDBK, database=DBBK, charset="utf8mb4")
    return  mydb
 
def conexion_dbnet(DB):
    mydb = mysql.connector.connect(host= HOST, user= USER, password=PASSWORD, database=DB, charset="utf8mb4")
    return  mydb

def conexion_dbown(DBOWN):
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

