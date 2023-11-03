from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
import mysql.connector

def home(request):
    strtext = request.GET.get('strbuscado')
    db = request.GET.get('dbstr')
    db = "temp_db"
    piv = request.GET.get('pivstr')
    registros_con_strtext  = []
    mydb =  conexion_dbbk(db)
    mycursor = mydb.cursor()
 
                  
    if strtext and int(piv)==0:               
        mycursor.execute('select * from backups_ip where backup_date like "%2023-06-19%" and running_config like "%'+strtext+'%"') 
        encontrado = mycursor.fetchall()
        mycursor.close
        for resultado in encontrado:
            id_registro = resultado[0]  #ip_device
            running_text = resultado[3]  #running_conf
            lineas = running_text.split('\n')
            lineas_con_strtext = [linea for linea in lineas if strtext in linea]

            if lineas_con_strtext:
                registros_con_strtext.append((id_registro, lineas_con_strtext))
                
        return render(request, "paginas/welcome.html", {"encontrado":registros_con_strtext, 'dbs': esquemata()})
    else:
        return render(request, 'paginas/welcome.html', {'dbs': esquemata()})
   



