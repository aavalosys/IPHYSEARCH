from django.shortcuts import render
from django.db import connection
from datetime import datetime
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *
from appsearch.busca_ips import * 
 

def catalogos(request, selectedoption):
    db = request.GET.get('dbstr')
    idtxtabuscar = request.GET.get('strbuscado')
    resultado = []
    headtable = []
    listaract = []
    listasr = []
    vendors = ['CISCO', 'HUAWEI', 'GOOGLE', 'NETFLIX', 'AKAMAI']
    paises = ['GUATEMALA', 'EL SALVADOR', 'HONDURAS', 'NICARAGUA', 'COSTA RICA']

    if selectedoption == 'actividades':           #AL BUSCAR
        opcion = 'actividades'
        headtable = headselector(selectedoption)
        listaract = muestraregistros(20,'')
    elif selectedoption == 'casossr':
        opcion = 'casos SR'
        headtable = headselector(selectedoption)
        listasr = muestraregistros(10,'')
    elif selectedoption == 'buscaregistros':
        opcion = 'registros'
        headtable = headselector(selectedoption)
        listasr = buscaregistros()


    if db is not None and idtxtabuscar is not None: #AL INGRESAR A LA OPCION
        if selectedoption == 'actividades':
            listaract = muestraregistros(20,idtxtabuscar)
        elif selectedoption == 'casossr':
            listasr = muestraregistros(10,idtxtabuscar)
        

    return render(request,'paginas/catalogos.html',
                {   'opcion':opcion,
                    'listaract':listaract,
                    'listasr':listasr,  
                    'headtable':headtable,
                    'resultado':resultado,
                    'vendors':vendors,
                    'paises':paises,    
                    'dbs': esquemata(),
                    'user': usuariolog(),
                })


def muestraregistros(tipo,abuscar):
    dbrbs = "dbloip130324"
    print(tipo)
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador FROM "+
             "(SELECT * FROM bitacorasract WHERE codigosractividad LIKE '%"+abuscar+
             "%' OR titulo LIKE '%"+abuscar+"%' OR descripcion LIKE '%"+abuscar+
             "%' OR detallesr LIKE '%"+abuscar+"%') AS filtered_results WHERE tipo = " +str(tipo)+
             " ORDER BY contador DESC LIMIT 15")
    listaract=mycursor.fetchall()
    return listaract


def  headselector(selectedoption):
    if selectedoption == 'actividades':
        headtable = ["ACTIVIDAD", "TÍTULO", "FECHA", "HORA", "DESCRIPCIÓN", "DETALLE", "INGRESADA","ESTADO","OPCIÓN"]
    elif selectedoption == 'casossr':
        headtable = ["CASO SR", "TÍTULO", "FECHA", "HORA", "DESCRIPCIÓN", "DETALLE","VENDOR","ESTADO","PAÍS","OPCIÓN"]
    else:
        headtable = []
    return headtable




def agregaractividad(request):
    dbrbs = "dbloip130324"
    vendors = ['CISCO', 'HUAWEI', 'GOOGLE', 'NETFLIX', 'AKAMAI']
    paises = ['GUATEMALA', 'EL SALVADOR', 'HONDURAS', 'NICARAGUA', 'COSTA RICA']
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    if request.method == 'POST':
        codigoact = request.POST.get('ididentificador')
        titulo = request.POST.get('idtitulo')
        fecha_str = request.POST.get('idfechaact')
        fecha_dt = datetime.strptime(fecha_str, '%Y-%m-%d')  
        fechain = fecha_dt.strftime('%d/%m/%Y')
        hora = request.POST.get('idhoraact')
        descripcion = request.POST.get('iddescripcion')
        detalle = request.POST.get('iddetalle')
        observfechahoraactual = request.POST.get('idfechahora')
        estado = "ABIERTA"
        pais = ""
        tipo = "20"

    consulta_sql = """
            INSERT INTO {}.bitacorasract (codigosractividad, titulo, fecha, hora, descripcion, 
            detallesr, observaciones, estado, pais, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """.format(dbrbs)
    try:
        mycursor.execute(consulta_sql, (codigoact, titulo, fechain, hora, descripcion, detalle, observfechahoraactual, estado, pais, tipo))
        mydb.commit()
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
        mydb.rollback()

    mycursor.close()  
    mydb.close()  

    return render(request,'paginas/catalogos.html',
                {   'opcion':'actividades',  
                    'headtable':headselector('actividades'), 
                    'resultado':[],
                    'vendors':vendors,
                    'paises':paises,     
                    'dbs': esquemata(),
                    'user': usuariolog(),
                }) 





def agregarsr(request):
    dbrbs = "dbloip130324"
    vendors = ['CISCO', 'HUAWEI', 'GOOGLE', 'NETFLIX', 'AKAMAI']
    paises = ['GUATEMALA', 'EL SALVADOR', 'HONDURAS', 'NICARAGUA', 'COSTA RICA']
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()

    if request.method == 'POST':
        codigoact = request.POST.get('ididentificadorsr')
        titulo = request.POST.get('idtitulosr')
        fecha = request.POST.get('fechasr')
        fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')  
        fechain = fecha_dt.strftime('%d/%m/%Y')
        hora = request.POST.get('horasr')
        descripcion = request.POST.get('iddescripcionsr')
        detalle = request.POST.get('iddetallesr')
        observendor = request.POST.get('vendors')
        estado = "ABIERTO"
        pais = request.POST.get('paises')
        tipo = "10"  #CASO PROVEEDOR

    consulta_sql = """
            INSERT INTO {}.bitacorasract (codigosractividad, titulo, fecha, hora, descripcion, 
            detallesr, observaciones, estado, pais, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """.format(dbrbs)
    try:
        mycursor.execute(consulta_sql, (codigoact, titulo, fechain, hora, descripcion, detalle, observendor, estado, pais, tipo))
        mydb.commit()
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
        mydb.rollback()

    mycursor.close()  
    mydb.close()  

    return render(request,'paginas/catalogos.html',
                {   'opcion':'actividades',  
                    'headtable':headselector('actividades'), 
                    'resultado':[],
                    'vendors':vendors,
                    'paises':paises,     
                    'dbs': esquemata(),
                    'user': usuariolog(),
                }) 



def buscaregistros():

    return 0 