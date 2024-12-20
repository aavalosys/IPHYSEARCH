import datetime
import logging
from django.db import OperationalError
from models import Bitacora
from django.db.models import Count
from datetime import datetime
from django.shortcuts import render
from requests import request
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *  #IMPORTA VAR
from iphysearchapp.connect import *  
from appsearch.varias_func import *  #IMPORTAR APIS
from django.contrib.auth.decorators import login_required 
from django.db.models import F, ExpressionWrapper, DurationField
from django.utils import timezone
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

dbrbsmantto = "dblocal_mantto"
tablaname = "backups_ip"

@login_required
def home(request):
    try:
        username = request.user.username
        conexiondb = probar_conexion_db(dbrbsmantto)  
        alertsuccess = 1
        strtext = request.GET.get('strbuscado')
        pivote = request.GET.get('pivotestr')
        dbsbackup = request.GET.get('iddbselectedwel')
        resultadoencontrado = []

        try:
            mydb = conexion_dbbk(dbsbackup) 
            mycursor = mydb.cursor()
        except OperationalError as e:
            respuesta = "Error al conectar a la base de datos."
            errordes = "Recargue la página o contacte al soporte técnico."
            errores = [{
                'db_name': dbsbackup,
                'exception_code': e.__class__.__name__,
                'exception_message': str(e),
                'additional_info': 'Verifique la conexión con la base de datos y la red.'
            }]
            return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores})

        try:
            dbsb = esquematabackups(HOSTBACKUP, USERBACKUP, PASSWORDBACKUP)

        except Exception as e:
            respuesta = "Error al ejecutar la consulta SQL."
            errordes = "Hubo un problema al obtener las fechas de los backups."
            errores = [{
                'db_name': dbsbackup,
                'exception_code': e.__class__.__name__,
                'exception_message': str(e),
                'additional_info': 'Revise la estructura de la tabla y los datos almacenados.'
            }]
            return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores})

        if strtext:
            try:
                strings_buscados = [s.strip() for s in strtext.split('|') if s.strip()]
                if not strings_buscados:
                    return render(request, "paginas/welcome.html", {
                        'resultadoencontrado': [],
                        'alertsuccess': alertsuccess,
                        'conexiondb': conexiondb,
                        'dbsb': dbsb,
                        'user': username
                    })
                conditions = " AND ".join([f"running_config LIKE %s" for _ in strings_buscados])
                query = f"""
                    SELECT device_ip, running_config
                    FROM {dbsbackup}.{tablaname}
                    WHERE {conditions}
                """
                
                params = [f"%{term}%" for term in strings_buscados]
                mycursor.execute(query, params)
                encontrado = mycursor.fetchall()
                resultadoencontrado = []

                for tupla in encontrado:
                    device_ip = tupla[0]
                    running_config = tupla[1]
                    lineas = running_config.split('\n')
                    cumple_todos = all(
                        any(str_buscado.upper() in linea.upper() for linea in lineas)
                        for str_buscado in strings_buscados
                    )

                    if cumple_todos:
                        matches = [
                            (str_buscado, linea)
                            for str_buscado in strings_buscados
                            for linea in lineas
                            if str_buscado.upper() in linea.upper()
                        ]
                        resultadoencontrado.append((device_ip, matches))

                mycursor.close()

                return render(request, "paginas/welcome.html", {
                    'resultadoencontrado': resultadoencontrado,
                    'alertsuccess': alertsuccess,
                    'conexiondb': conexiondb,
                    'dbsb': dbsb,
                    'user': username  
                })

            except Exception as e:
                respuesta = "Error al procesar la búsqueda."
                errordes = "Hubo un problema al realizar la operación solicitada."
                errores = [{
                    'operation': 'Consulta y procesamiento de backups',
                    'exception_code': e.__class__.__name__,
                    'exception_message': str(e),
                    'additional_info': 'Verifique los parámetros de entrada y las condiciones de la consulta.'
                }]
                return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores})


        else:
            # Renderizar la página principal en caso de que no haya búsqueda
            return render(request, 'paginas/welcome.html', {
                'resultadoencontrado': [],
                'listarsr': actualizarbitacorasr(),
                'listaract': actualizarbitacoact(),
                'sumacasosr': sumasr(),
                'sumaact': sumaact(),
                'alertsuccess': alertsuccess,
                'conexiondb': conexiondb,
                'dbsb': dbsb,
                'user': username  
            })
    except Exception as e:
        # Manejo de errores generales
        respuesta = "Error inesperado."
        errordes = "Ocurrió un error inesperado en la aplicación."
        errores = [{
            'exception_code': e.__class__.__name__,
            'exception_message': str(e),
            'additional_info': 'Revise los logs del servidor para más detalles.'
        }]
        return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores})


def sumaact():
    sumacasact = Bitacora.objects.using(DBMANTTOLOCAL).filter(estado="OPEN", tipo="ACTIVIDAD").count()
    return sumacasact

def sumasr():
    sumacasosr = Bitacora.objects.using(DBMANTTOLOCAL).filter(estado="OPEN", tipo="SR").count()
    return sumacasosr

def actualizarbitacoact():
    queryset = Bitacora.objects.using(DBMANTTOLOCAL).filter(estado="OPEN", tipo="ACTIVIDAD")
    current_date = timezone.now().date()

    listaract = list(queryset.values('codigo', 'fecha', 'hora', 'vendor', 'estado', 'pais', 'tipo', 'fechahoragrabacion', 'usuariocrea'))

    for act in listaract:
        fecha_str = act['fecha']
        fecha_obj = datetime.strptime(fecha_str, '%d/%m/%Y').date()
        resta = (current_date - fecha_obj).days
        act['resta'] = resta

        if resta == 0:
            act['dias'] = "HOY"
        elif resta == 1:
            act['dias'] = "AYER"
        elif resta == -1:
            act['dias'] = "MAÑANA"
        elif resta > 1:
            act['dias'] = resta
        else:
            act['dias'] = "PROXIMO"

    listaract = sorted(listaract, key=lambda x: x['resta'], reverse=True)
    listaract = listaract[-10:]
    return listaract


def actualizarbitacorasr():
    queryset = Bitacora.objects.using(DBMANTTOLOCAL).filter(estado="OPEN", tipo="SR")
    current_date = timezone.now().date()
    listarsr = list(queryset.values('codigo', 'fecha', 'hora', 'vendor', 'estado', 'pais', 'tipo', 'fechahoragrabacion', 'usuariocrea'))

    for sr in listarsr:
        fecha_str = sr['fecha']
        fecha_obj = datetime.strptime(fecha_str, '%d/%m/%Y').date()
        sr['dias'] = (current_date - fecha_obj).days

    listarsr = sorted(listarsr, key=lambda x: x['dias'], reverse=True)
    listarsr = listarsr[:10]
    return listarsr

def probar_conexion_db(db_alias):
    try:
        connection = connections[db_alias]
        connection.ensure_connection()
        return 0
    except OperationalError as e:
        return 1


def esquematabackups(servidor, usuario, contraseña):
    conn, cursor = establecer_conexion_mysql(servidor, usuario, contraseña)
    if not conn or not cursor:
        raise Exception("No se pudo establecer la conexión a la base de datos")

    query = "SHOW DATABASES LIKE 'nbk%'"
    cursor.execute(query)
    bases_de_datos_inv = cursor.fetchall()
    bases_de_datos = list(reversed(bases_de_datos_inv))
    cerrar_conexion_mysql(conn, cursor)

    return bases_de_datos

def establecer_conexion_mysql(servidor, usuario, contraseña, base_datos=None):
    try:
        conn = mysql.connector.connect(
            host=servidor,
            user=usuario,
            password=contraseña,
            database=base_datos if base_datos else None
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"Error al establecer la conexión: {e}")
        return None, None
    
def cerrar_conexion_mysql(conn, cursor):
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")



    