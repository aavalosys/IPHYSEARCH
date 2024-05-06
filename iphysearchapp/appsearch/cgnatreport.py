import datetime
from io import BytesIO
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import connection 
import requests
from appsearch import descargar
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
from django.views.decorators.http import require_GET

def cgnat(request):
    tipoalerta = '1'
    opcioncgnats = ['GUATEMALA','HONDURAS','EL SALVADOR','NICARAGUA','COSTA RICA']
    paisselect = request.GET.get('optionsRadios')
    if request.method == 'GET':
        action = request.GET.get('graficar')
        if action == 'graficar':
            if paisselect == 'GUATEMALA':
                datosapi =  consultarcgnat('GT')
                datos_c = convertiraformatocsv(datosapi)
                datosproc = datosalista(datos_c)      # CONVIERTE EN UNA LISTA DE LISTAS
                datoscgnats = datoslogicos(datosproc) # EXTRAE LOS PRIMEROS 11 VALORES
                ipcgnat = extraeipcgnat(datosproc)    # EXTRAE LAS IPS DE LOS CGNATS
            elif paisselect == 'HONDURAS':
                datosapi =  consultarcgnat('HN')
                datos_c = convertiraformatocsv(datosapi)
                datosproc = datosalista(datos_c) 
                datoscgnats = datoslogicos(datosproc) 
                ipcgnat = extraeipcgnat(datosproc)
            elif paisselect == 'EL SALVADOR':
                datosapi =  consultarcgnat('SV')
                datos_c = convertiraformatocsv(datosapi)
                datosproc = datosalista(datos_c) 
                datoscgnats = datoslogicos(datosproc) 
                ipcgnat = extraeipcgnat(datosproc)
            elif paisselect == 'NICARAGUA':
                datosapi =  consultarcgnat('NI')
                datos_c = convertiraformatocsv(datosapi)
                datosproc = datosalista(datos_c) 
                datoscgnats = datoslogicos(datosproc) 
                ipcgnat = extraeipcgnat(datosproc)
            elif paisselect == 'COSTA RICA':
                datosapi =  consultarcgnat('CR')
                datos_c = convertiraformatocsv(datosapi)
                datosproc = datosalista(datos_c) 
                datoscgnats = datoslogicos(datosproc)
                ipcgnat = extraeipcgnat(datosproc)
            else:
                ipcgnat =[]
                datoscgnats =[]
            return render(request, 'paginas/cgnatreport.html',
                    {'dbs': esquemata(),
                    'user': usuariolog(),
                    'ipcgnat':ipcgnat,
                    'tipoalerta':tipoalerta,
                    'opcioncgnats':opcioncgnats,   
                    'datoscgnats':datoscgnats,
                    'inforcgnat1':'Bienvenido al ',
                    'inforcgnat2':'',
                        })
        else:
            print("")    

    return render(request, 'paginas/cgnatreport.html',
            {'dbs': esquemata(),
            'user': usuariolog(),
            'ipcgnat':[],
            'opcioncgnats':opcioncgnats,
            'tipoalerta':tipoalerta,
            'datoscgnats':[],
            'inforcgnat1':'Bienvenido al ',
            'inforcgnat2':'',
            }) 


def consultarcgnat(pais):
    try:
        url = f"http://10.10.26.4:5000/api/cgnat_info/"
        data_to_send = [pais]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            data = response.json()
            print (data)
        else:
            data = []
    except Exception as e:
        data = []
    return data
    

def extraeipcgnat(datoscgnat):
    ipscgnat = set()
    for sublista in datoscgnat[1:]:
          ipscgnat.add(sublista[1])
    ipscgnat = list(ipscgnat)
    return ipscgnat


def datosalista (datos):
    datossintab = datos.strip().replace('\t', '')
    lineas = datossintab.splitlines()
    lista_datos = []
    for linea in lineas[0:]:
        datos_linea = linea.split(';')
        datos_linea = [elemento.strip() for elemento in datos_linea]
        nueva_lista = []
        for elemento in datos_linea:
            try:
                nueva_lista.append(int(elemento))
            except ValueError:
                try:
                    nueva_lista.append(float(elemento))
                except ValueError:
                    nueva_lista.append(elemento)
        lista_datos.append(nueva_lista)
    return lista_datos


def datoslogicos(datosproc):
    lista_logica = [sublista[:11] for sublista in datosproc[1:] if len(sublista) > 11]
    return lista_logica

def convertiraformatocsv(data):
    variable_csv =""
    for row in data:
        row = map(str, row)
        fila_csv = ';'.join(row)
        variable_csv += fila_csv + '\n'
    return variable_csv
    
