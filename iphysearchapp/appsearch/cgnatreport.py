from django.shortcuts import render
from django.db import connection
import requests
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
from django.views.decorators.http import require_GET
import mysql.connector

def cgnat(request):  #TITULO, WITH,VACTUAL,VMIN,VMAX
    opcioncgnats = ['GUATEMALA','HONDURAS','EL SALVADOR','NICARAGUA','COSTA RICA']
    ipcgnat = []
    datoscgnats = []
    
    if request.method == 'GET':
        action = request.GET.get('action', None)
        if action == 'graficar':
                        #TITULO,WITH,VACTUAL,VMIN,VMAX,WITH,VACTUAL,VMIN,VMAX,WITH,VACTUAL,VMIN,VMAX
            ipcgnat = ['10.179.28.2','10.179.28.1','10.179.28.4','10.179.28.5','10.179.28.7']
            datoscgnats = [['CGNAT HFC','10','0','0','100','50','0','0','100','40','0','0','100'], 
                          ['CGNAT BRAS','7','25','0','100','9','20','0','100','15','5','0','100'], 
                          ['CGNAT GPON','3','40','0','100','11','20','0','100','15','5','0','100']]
            return render(request, 'paginas/cgnatreport.html',
                    {'dbs': esquemata(),
                        'opcioncgnats':opcioncgnats,
                        'ipcgnat':ipcgnat,
                        'datoscgnats':datoscgnats,
                        })
        
        elif action == 'reporte':
            print()
        
    else:
        return render(request, 'paginas/cgnatreport.html',
            {'dbs': esquemata(),
            'opcioncgnats':opcioncgnats,
            'ipcgnat':ipcgnat,
            'datoscgnats':datoscgnats,
            }) 

        

def intdetail():
    try:
        url = f"http://10.10.26.4:5000/api/cgnat_info/"
        data_to_send = ["GT"]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            data = response.json()
            datacg = data[1]
        else:
            datacg = 'X'
        return datacg
    except Exception as e:
        datacg = 'X'
        return datacg



