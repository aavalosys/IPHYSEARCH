import csv
from datetime import date
from django.http import HttpResponse
from appsearch.cgnatreport import consultarcgnat, convertiraformatocsv
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *

def descargararchivo(request, pais):
    fecha = date.today().strftime("%d-%m-%Y")
    cgnatname =""
    if pais == "GUATEMALA":
        cgnatname ="cgnat_gt_"
        datadelapi = consultarcgnat("GT")
        content = convertiraformatocsv(datadelapi)
    elif pais == "HONDURAS":
        cgnatname ="cgnat_hn_"
        datadelapi = consultarcgnat("HN")
        content = convertiraformatocsv(datadelapi)
    elif pais == "EL SALVADOR":
        cgnatname ="cgnat_sv_"
        datadelapi = consultarcgnat("SV")
        content = convertiraformatocsv(datadelapi)
    elif pais == "NICARAGUA":
        cgnatname ="cgnat_ni_"
        datadelapi = consultarcgnat("NI")
        content = convertiraformatocsv(datadelapi)
    elif pais == "COSTA RICA":
        cgnatname ="cgnat_cr_"
        datadelapi = consultarcgnat("CR")
        content = convertiraformatocsv(datadelapi)
    else:
        content = ""
        print("Sin País")
    nombre_archivo = cgnatname + fecha + ".csv"
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
    return response
