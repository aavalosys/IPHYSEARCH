from django.shortcuts import render
from django.db import connection
from sistema.databases import DATABASES
from sistema.var_env import *
import mysql.connector 
from .models import *

def conexion():
    mydb = mysql.connector.connect(
        host= HOSTBK,
        user= USERBK,
        password=PASSWORDBK,
        database=DBBK
        )
    mycursor = mydb.cursor()
    return  mycursor

def home(request):
    mycursor = conexion()
    strtext = request.GET.get('strbuscado')
    db = request.GET.get('dbstr')
    piv = request.GET.get('pivstr')
    
    if strtext and int(piv)==0:               
        mycursor.execute('select device_ip, running_config from backups_ip where device_ip like  "%10.78.7.196%" limit 1')
        encontrado = mycursor.fetchall()
        mycursor.close
        return render(request, "paginas/home.html", {"encontrado":encontrado, 'dbs': esquemata()})
    else:
        return render(request, 'paginas/home.html', {'dbs': esquemata()})


def buscaips(request):
    mycursor = conexion()
    idrbs = request.GET.get('idrbs')
    dbrbs = request.GET.get('dbrbs')
    pivrbs = request.GET.get('pivrbs')
    
    ip = request.GET.get('ip')
    db = request.GET.get('db')
    piv = request.GET.get('piv')

    if idrbs and pivrbs=='0':               
        mycursor.execute('SELECT * FROM '+ dbrbs+'.nodob WHERE nodoid like "%"'+idrbs+'%"')
        qrbss = mycursor.fetchall()
        return render(request, "paginas/buscaips.html", {"qrbss":qrbss, 'dbs': esquemata()})
    elif ip and piv=='1':
        return render(request, "paginas/buscaips.html", {'dbs': esquemata()})
    
    return render(request, "paginas/buscaips.html", {'dbs': esquemata()})
    
    

    
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


def listadoinodos(request):
    return render(request, "paginas/buscaips.html", {'dbs': esquemata()})


def monitoreotcns(request):
    return render(request,'paginas/monitoreotcns.html')

def buscadorvarios(request):
    return render(request,'paginas/buscadorvarios.html')

def pruebas(request):
     return render(request,'paginas/pruebas.html', {'dbs': esquemata()})


# Datos de conexión a la base de datos
db_config = {
    'host': '10.10.26.5',
    'user': 'nelson.avalos',
    'password': 'Navalos20230720#',
    'database': 'temp_db',
}

