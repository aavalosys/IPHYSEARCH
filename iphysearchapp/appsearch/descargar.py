import csv
from datetime import date
from django.http import HttpResponse
from appsearch.cgnatreport import consultarcgnat, convertiraformatocsv
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

def descargararchivo(request, pais):
    fecha = date.today().strftime("%d-%m-%Y")
    cgnatname =""
    if pais == "GUATEMALA":
        print("El país introducido es Guatemala.")
        content = datosdepruebagt
        cgnatname ="cgnat_gt_"
        #datadelapi = consultarcgnat("GT")
        #content = convertiraformatocsv(datadelapi)
    elif pais == "HONDURAS":
        print("El país introducido es Honduras.")
        #content = datospruebahn
        cgnatname ="cgnat_hn_"
        datadelapi = consultarcgnat("HN")
        content = convertiraformatocsv(datadelapi)
    elif pais == "EL SALVADOR":
        print("El país introducido es Nicaragua.")
        #content = datospruebasv
        cgnatname ="cgnat_sv_"
        datadelapi = consultarcgnat("SV")
        content = convertiraformatocsv(datadelapi)
    elif pais == "NICARAGUA":
        print("El país introducido es El Salvador.")
        #content = datospruebani
        cgnatname ="cgnat_ni_"
        datadelapi = consultarcgnat("NI")
        content = convertiraformatocsv(datadelapi)
    elif pais == "COSTA RICA":
        print("El país introducido es Costa Rica.")
        #content = datospruebacr
        cgnatname ="cgnat_cr_"
        datadelapi = consultarcgnat("CR")
        content = convertiraformatocsv(datadelapi)
    else:
        content = ""
        print("NO SE ENVIO UN PAIS CORRECTO")
    nombre_archivo = cgnatname + fecha + ".csv"
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
    return response
