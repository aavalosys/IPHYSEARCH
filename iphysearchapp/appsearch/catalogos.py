from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from appsearch.busca_ips import *
from .models import *
 

def catalogos(request, selectedoption):
    db = request.GET.get('dbstr')
    idtxtabuscar = request.GET.get('strbuscado')
    resultado = []
    headtable = []

    if selectedoption == 'actividades':
        opcion = 'actividades'
        headtable = headselector(selectedoption)
    elif selectedoption == 'casossr':
        opcion = 'casos SR'
        headtable = headselector(selectedoption)

    if db is not None and idtxtabuscar is not None:
        if selectedoption == 'actividades':
            listaract = muestraactividades(20)
        elif selectedoption == 'casossr':
            resultado = muestraactividades(10)

    return render(request,'paginas/catalogos.html',
                {   'opcion':opcion,
                    'listaract':muestraactividades(20),  
                    'headtable':headtable,
                    'resultado':resultado,    
                    'dbs': esquemata(),
                })


def muestraactividades(tipo):
    dbrbs = "dbloip130324"
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador FROM"+
                     " bitacorasract WHERE estado = 3 and tipo = "+str(tipo)+" ORDER BY contador DESC limit 15".format(dbrbs))
    listaract=mycursor.fetchall()
    return listaract


def  headselector(selectedoption):
    if selectedoption == 'actividades':
        headtable = ["ACTIVIDAD", "TÍTULO", "FECHA", "HORA", "DESCRIPCIÓN", "DETALLE", "MANTTO"]
    elif selectedoption == 'casossr':
        headtable = ["CASO SR", "TÍTULO", "FECHA", "HORA", "DESCRIPCIÓN", "DETALLE","DÍAS","PAÍS","MANTTO"]
    else:
        headtable = []
    return headtable


def agregaractividad(request):
    dbrbs = "dbloip130324"
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    if request.method == 'POST':
        codigoact = request.POST.get('ididentificador')
        titulo = request.POST.get('idtitulo')
        fecha = request.POST.get('idfechaact')
        hora = request.POST.get('idhoraact')
        descripcion = request.POST.get('iddescripcion')
        detalle = request.POST.get('iddetalle')
        fechahoraactual = request.POST.get('idfechahora')
        estado = "3"
        pais = ""
        tipo = "20"

    consulta_sql = """
            INSERT INTO {}.bitacorasract (codigosractividad, titulo, fecha, hora, descripcion, 
            detallesr, observaciones, estado, pais, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """.format(dbrbs)
    try:
        mycursor.execute(consulta_sql, (codigoact, titulo, fecha, hora, descripcion, detalle, fechahoraactual, estado, pais, tipo))
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
                    'dbs': esquemata(),
                }) 

def agregarcasosr(request):
    if request.method == 'POST':
        codigoact = request.POST.get('ididentificador')
        titulo = request.POST.get('idtitulo')
        fecha = request.POST.get('idfechaact')
        hora = request.POST.get('idhoraact')
        descripcion = request.POST.get('iddescripcion')
        detalle = request.POST.get('iddetalle')
        fechahoraactual = request.POST.get('idfechahora')

    return render(request,'paginas/catalogos.html',
                {   'opcion':'casossr',  
                    'headtable':headselector('casossr'), 
                    'resultado':[],    
                    'dbs': esquemata(),
                }) 