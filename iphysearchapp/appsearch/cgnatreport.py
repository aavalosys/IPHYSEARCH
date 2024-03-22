from django.shortcuts import render
from django.db import connection
import requests
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
from django.views.decorators.http import require_GET


def Reporte():
    return print("estoy en reporte")

def intdetail(pais):
    try:
        url = f"http://10.10.26.4:5000/api/cgnat_info/"
        data_to_send = [pais]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            data = response.json()
            #datacg = data[1][]
            print (data)
        else:
            datacg = 'X'
        return datacg
    except Exception as e:
        datacg = 'X'
        return datacg
    
def dataprovisional(datacrcgnat):
    #datoscgnats = formatar_datos(datacrcgnat)
    datoscgnats = []
    ips = set()
    for row in datacrcgnat[1:]: #EXTRAE LAS IP DE LA LISTA DE LISTAS 
        ip = row[0]
        ips.add(ip)

    ips_cgnats = list(ips)  #DEVUELVE LAS IPS Y FORMATO PARA GRAFICAR
    print (ips_cgnats)
    return ips_cgnats, datoscgnats

    
def formatar_datos(datos):
    datoscgnats = []
    for row in datos[0:]:
        instancia = row[1]
        usuarios_posibles = row[5]
        usuarios = row[4]
        utilizacion_usuarios = row[6]
        datos_formatados = [instancia, '0', '0', '0', '0', usuarios_posibles, '0', '0', '100', usuarios, '0', '0', '100']
        datoscgnats.append(datos_formatados)
    return datoscgnats



def cgnat(request):  #TITULO, WITH,VACTUAL,VMIN,VMAX
    opcioncgnats = ['GUATEMALA','HONDURAS','EL SALVADOR','NICARAGUA','COSTA RICA']
    ipcgnat = []
    datoscgnats = [] 

    if request.method == 'GET':
        action = request.GET.get('action', None)
        if action == 'graficar':
            ipcgnat, datoscgnats = dataprovisional(intdetail("CR"))
            return render(request, 'paginas/cgnatreport.html',
                    {'dbs': esquemata(),
                        'opcioncgnats':opcioncgnats,
                        'ipcgnat':ipcgnat,
                        'datoscgnats':datoscgnats,
                        })
        elif action == 'reporte':
            Reporte()
            return render(request, 'paginas/cgnatreport.html',
                    {'dbs': esquemata(),
                        'opcioncgnats':opcioncgnats,
                        'ipcgnat':ipcgnat,
                        'datoscgnats':datoscgnats,
                        })
        else:
            print("INGRESANDO POR PRIMERA VEZ SIN CARGAR NADA")    

    return render(request, 'paginas/cgnatreport.html',
            {'dbs': esquemata(),
            'opcioncgnats':opcioncgnats,
            'ipcgnat':ipcgnat,
            'datoscgnats':datoscgnats,
            }) 

        
