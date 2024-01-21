from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *

def esquemata():
    cursor = connection.cursor()
    cursor.execute('select count(SCHEMA_NAME) from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'"')
    nodbs = [int(tupla[0]) for tupla in cursor.fetchall()]
    cursor.execute('select SCHEMA_NAME  from information_schema.schemata where SCHEMA_NAME like "'+DBSINICIAL+'" order by SCHEMA_NAME desc limit '+
                   str(nodbs[0])+' offset 2')
    esquemas = [str(tupla[0]) for tupla in cursor.fetchall()]
    print (esquemas)
    return esquemas