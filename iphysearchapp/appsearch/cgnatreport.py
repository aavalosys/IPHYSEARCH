import datetime
from io import BytesIO
import io
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection 
import requests
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
from django.views.decorators.http import require_GET

def cgnat(request):
    listac = []
    opcioncgnats = ['GUATEMALA','HONDURAS','EL SALVADOR','NICARAGUA','COSTA RICA']
    paisselect = request.GET.get('optionsRadios')
    print (paisselect) 
    if request.method == 'GET':
        action = request.GET.get('action', None)
        if action == 'graficar':
            if paisselect == 'GUATEMALA':
                print("GT")
                datos_c =  consultarcgnat('GT')
                #datos_c =  datosdeprueba
                datosproc = datosalista(datos_c)
                datoscgnats = datoslogicos(datosproc)
                ipcgnat = extraeipcgnat(datosproc)
            elif paisselect == 'HONDURAS':
                print("HN")
                #datoschn = datosc = consultarcgnat('HN')
            elif paisselect == 'EL SALVADOR':
                print("SV")
                #datoscsv = datosc = consultarcgnat('SV')
            elif paisselect == 'NI':
                print("EN NI")
                #datoscni = datosc = consultarcgnat('NI')
            elif paisselect == 'COSTA RICA':
                datos_c =  consultarcgnat('CR')
                for row in datos_c:
                    row = map(str, row)
                    listac.append(';'.join(row))
                listac = [item + '\n' for item in listac]
                print (listac)
                #datos_d =  listac
                #datosproc = datosalista(datos_d)
                #datoscgnats = datoslogicos(datosproc)
                #ipcgnat = extraeipcgnat(datosproc)
                #datosccr = datosc = consultarcgnat('CR')

            return render(request, 'paginas/cgnatreport.html',
                    {'dbs': esquemata(),
                    'user': usuariolog(),
                    'ipcgnat':[],
                    'opcioncgnats':opcioncgnats,
                    'datoscgnats':[],
                        })
        elif action == 'reporte':
            response =reporte(request, str(paisselect))
            return render(request, 'paginas/cgnatreport.html',
                    {'dbs': esquemata(),
                    'user': usuariolog(),
                    'ipcgnat':[],
                    'opcioncgnats':opcioncgnats,
                    'datoscgnats':[],
                    'response': response, 
                    })
        else:
            print("---------> INGRESO INICIAL  <----------")    

    return render(request, 'paginas/cgnatreport.html',
            {'dbs': esquemata(),
            'user': usuariolog(),
            'ipcgnat':[],
            'opcioncgnats':opcioncgnats,
            'datoscgnats':[],
            }) 


def consultarcgnat(pais):
    try:
        url = f"http://10.10.26.4:5000/api/cgnat_info/"
        data_to_send = [pais]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            data = response.json()
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

from io import BytesIO
from django.http import HttpResponse

from io import BytesIO
from django.http import HttpResponse

def reporte(request, pais):  # Pass 'pais' as an argument
    url = "http://10.10.26.4:5000/api/cgnat_info/"
    data_to_send = ["CR"]  # Use the provided country code

    response = requests.post(url, json=data_to_send)

    if response.status_code == 200:
        data = response.json()
        fecha_actual = datetime.date.today()  # Use datetime.date.today()
        string_fecha_actual = fecha_actual.strftime("%Y-%m-%d")
        contenido_csv = ''

        for row in data:
            row = map(str, row)
            contenido_csv += ';'.join(row) + '\n'

        output = io.BytesIO(contenido_csv.encode('utf-8'))  # Ensure UTF-8 encoding
        download_response = HttpResponse(output, content_type='application/octet-stream')
        download_response['Content-Disposition'] = f'attachment; filename="{string_fecha_actual}_{pais}_cgnat_data.csv"'

        # **Alternate approach (using the request object):**

        # download_url = request.build_absolute_uri(download_response.url)  # Uncomment for this approach
        context = {
            # 'download_url': download_response.url,  # Comment out for this approach
            'download_url': request.build_absolute_uri(download_response.url),  # Uncomment for this approach
            'filename': f"{string_fecha_actual}_{pais}_cgnat_data.csv",
        }

        return render(request, 'paginas/cgnatreport.html', context)
    else:
        return HttpResponse(f"Error al obtener datos: {response.status_code}")

