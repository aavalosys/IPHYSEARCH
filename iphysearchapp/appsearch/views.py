from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

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



