
from iphysearchapp.var_env import *
import mysql.connector 
from django.db import connection

def conexion():
    mydb = mysql.connector.connect(
        host= HOSTBK,
        user= USERBK,
        password=PASSWORDBK,
        database=DBBK
        )
    mycursor = mydb.cursor()
    return  mycursor

def esquemata():
    cursor = connection.cursor()
    cursor.execute('select count(SCHEMA_NAME) from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'"')
    nodbs = [int(tupla[0]) for tupla in cursor.fetchall()]
    print (nodbs)
    cursor.execute('select SCHEMA_NAME  from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'" order by SCHEMA_NAME desc limit '+
                   str(nodbs[0])+' offset 2')
    esquemas = [str(tupla[0]) for tupla in cursor.fetchall()]
    print (esquemas)
    return esquemas

