import datetime
from datetime import datetime
from django.shortcuts import render
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *


def home(request):
    alertsuccess = 1
    alertdanger = 0
    alertwarning = 0
    alertinfo = 0
    strtext = request.GET.get('strbuscado')
    piv = request.GET.get('pivstr')
    db = "temp_db"
    tablaname = "backups_ip"
    resultadoencontrado  = []
    mydb =  conexion_dbbk(db)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT backup_date FROM '+db+'.'+tablaname+' group by backup_date order by backup_date desc;')
    fechas_formateadas = mycursor.fetchall()
    dbsb = [fecha[0].strftime('%d/%m/%y') for fecha in fechas_formateadas if fecha[0]]

    if strtext and int(piv)==0:
        dbs = request.GET.get('iddbselectedwel')
        fecha_formato_sql = datetime.strptime(dbs, '%d/%m/%y').strftime('%Y-%m-%d')
        strings_buscados = strtext.split()
        clausulas_like = ["UPPER(running_config) LIKE UPPER(%s)"] * len(strings_buscados)
        clausulas_like.append("backup_date LIKE %s")
        print(clausulas_like)
        where_clause = " AND ".join(clausulas_like)
        print(where_clause)
        query = f"SELECT device_ip, running_config FROM {db}.{tablaname} WHERE {where_clause}"
        print(query)
        like_patterns = tuple(f"%{string}%" for string in strings_buscados)
        like_patterns += (fecha_formato_sql,)  # No necesitas los comodines % aquí
        print(like_patterns)
        mycursor.execute(query, like_patterns)
        encontrado = mycursor.fetchall()
        #encontrado = []


        for tupla in encontrado:
            device_ip = tupla[0]
            running_config = tupla[1]
            lineas = running_config.split('\n')
            for str_buscado in strings_buscados:
                    for linea in lineas:
                        if str_buscado.upper() in linea.upper():
                            resultadoencontrado.append((device_ip, str_buscado, linea))
                    
        mycursor.close

        return render(request, "paginas/welcome.html", {
            'resultadoencontrado':resultadoencontrado,
            'alertsuccess':alertsuccess,
            'alertdanger':alertdanger,
            'alertwarning':alertwarning,
            'alertinfo':alertinfo, 
            'dbsb': dbsb,
            'user': usuariolog()
            })
    
    else:
        return render(request, 'paginas/welcome.html', {
            'resultadoencontrado':[],
            'listarsr': actualizarbitacorasr(),
            'listaract':actualizarbitacoact(),
            'sumacasosr':sumasr(),
            'sumaact':sumaact(),
            'alertsuccess':alertsuccess,
            'alertdanger':alertdanger,
            'alertwarning':alertwarning,
            'alertinfo':alertinfo,   
            'dbsb': dbsb,
            'user': usuariolog()
            })
   



