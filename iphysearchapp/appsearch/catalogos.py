from django.shortcuts import redirect, render
from django.db import connection
import re
from datetime import datetime
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import * 
from iphysearchapp.connect import *
from appsearch.varias_func import *
from appsearch.busca_ips import * 
from django.contrib.auth.decorators import login_required
 
estados = ['ESTADO','OPEN', 'CLOSED', 'PAUSED']
vendors = ['HUAWEI', 'CISCO', 'INOC','GOOGLE', 'NETFLIX', 'AKAMAI','TELXIUS', 'VERIZON', 'TATA']
paises =  ['GUATEMALA', 'EL SALVADOR', 'HONDURAS', 'NICARAGUA', 'COSTA RICA']
resultado = ['1']

def catalogos(request, selectedoption):
    username = request.session.get('username', None) 
    db = request.GET.get('dbstr')
    idtxtabuscar = request.GET.get('strbuscado')
    fecha_str = ""
    estado = ""
    headtable = []
    listaract = []
    listasr = []

    
    if selectedoption == 'actividades':  
        estado = request.GET.get('idestadossact')
        fecha_str = request.GET.get('idfechabusqueda')
        opcion = 'actividades'
        headtable = headselector(selectedoption)
        listaract = muestraregistrosact(fecha_str, estado,'ACTIVIDAD','')
    elif selectedoption == 'casossr':
        estado = request.GET.get('idestadossr')
        fecha_str = request.GET.get('idfechabusqueda')
        opcion = 'casos SR'
        headtable = headselector(selectedoption)
        listasr = muestraregistrossr(estado,'SR','')
    elif selectedoption == 'buscaregistros':
        opcion = 'registros'
        headtable = headselector(selectedoption)

    if db is not None and idtxtabuscar is not None: 
        if selectedoption == 'actividades':
            listaract = muestraregistrosact(fecha_str, estado,'ACTIVIDAD',idtxtabuscar)
        elif selectedoption == 'casossr':
            listasr = muestraregistrossr(estado,'SR',idtxtabuscar)
        

    return render(request,'paginas/catalogos.html',
                {   'opcion':opcion,
                    'listaract':listaract,
                    'listasr':listasr,  
                    'headtable':headtable,
                    'resultado':resultado,
                    'vendors':vendors,
                    'paises':paises,
                    'estados':estados,    
                    'dbs': esquemata(),
                    'user': username,
                })


def muestraregistrosact(fecha_str, estado, tipo, abuscar): 
    dbrbs = "dblocalip06102024"
    listaract = []
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()

    if estado is None and fecha_str is None:
        query = """
            SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
            FROM (
                SELECT *
                FROM bitacora
                WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
            ) AS filtered_results
            WHERE tipo = %s
            ORDER BY contador ASC
        """
        params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', tipo)
    
    elif estado == 'ESTADO':
        if fecha_str =="":
            query = """
                SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
                FROM (
                    SELECT * 
                    FROM bitacora
                    WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
                ) AS filtered_results
                WHERE tipo = %s
                ORDER BY contador ASC
            """
            params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', tipo)
        else:
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
            fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
            query = """
                SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
                FROM (
                    SELECT * 
                    FROM bitacora
                    WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
                    AND STR_TO_DATE(fecha, '%d/%m/%Y') = STR_TO_DATE(%s, '%d/%m/%Y')
                ) AS filtered_results
                WHERE tipo = %s
                ORDER BY contador ASC
            """
            params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', fecha_formateada, tipo)
    else:
        if fecha_str =="":
            query = """
            SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
            FROM (
                SELECT * 
                FROM bitacora
                WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
                AND estado = %s
            ) AS filtered_results
            WHERE tipo = %s
            ORDER BY contador ASC
            """
            params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', estado, tipo)
        else:
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
            fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
            query = """
                SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
                FROM (
                    SELECT * 
                    FROM bitacora
                    WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
                    AND STR_TO_DATE(fecha, '%d/%m/%Y') = STR_TO_DATE(%s, '%d/%m/%Y')
                ) AS filtered_results
                WHERE tipo = %s
                ORDER BY contador ASC
            """
            params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', fecha_formateada, tipo)
    
    mycursor.execute(query, params)
    listaract = mycursor.fetchall()

    for i in range(len(listaract)):
        listaract[i] += ('1', '2', '3')  # Agregar tres campos vacíos al final

    return listaract

def muestraregistrossr(estado, tipo, abuscar): 
    dbrbs = "dblocalip06102024"
    mydb = conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    
    if estado is None:
        query = """
            SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
            FROM (
                SELECT *
                FROM bitacora
                WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
            ) AS filtered_results
            WHERE tipo = %s
            ORDER BY contador ASC
        """
        params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', tipo)
    
    elif estado == 'ESTADO' :
        query = """
            SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
            FROM (
                SELECT * FROM bitacora
                WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
            ) AS filtered_results
            WHERE tipo = %s
            ORDER BY contador ASC
        """
        params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', tipo)
    
    else:
        query = """
            SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
            FROM (
                SELECT * FROM bitacora
                WHERE (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s OR detalle LIKE %s)
                AND estado = %s
            ) AS filtered_results
            WHERE tipo = %s
            ORDER BY contador ASC
        """
        params = ('%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', '%' + abuscar + '%', estado, tipo)
    
    mycursor.execute(query, params)
    listarsr = mycursor.fetchall()

    for i in range(len(listarsr)):
        rmas_tuplas = obtenerRMAS(listarsr[i][0])
        rmas = []

        if rmas_tuplas:
            for tupla in rmas_tuplas:
                rmas.append(tupla)   
        else:
            rmas.append(("Sin RMA",))  
        listarsr[i] += (rmas, '2', '3')

    return listarsr


def agregaractividad(request):
    username = request.session.get('username', None)
    dbrbs = "dblocalip06102024"
    mydb =  conexion_dbown(dbrbs) 
    mycursor = mydb.cursor()
    if request.method == 'POST':
        codigoact = request.POST.get('ididentificador')

        titulo = request.POST.get('idtitulo')
        if len(titulo) > 95:
            titulo = titulo[:95]

        fecha_str = request.POST.get('idfechaact')
        fecha_dt = datetime.strptime(fecha_str, '%Y-%m-%d')  
        fechain = fecha_dt.strftime('%d/%m/%Y')

        hora = request.POST.get('idhoraact')

        descripcion = request.POST.get('iddescripcion')
        if len(descripcion) > 145:
            descripcion = descripcion[:145]

        detalle = request.POST.get('iddetalle')
        if len(detalle) > 195:
            detalle = detalle[:195]

        observacion = ""
        vendor = request.POST.get('idvendoract') 
        estado = "OPEN"
        pais = " "
        tipo = "ACTIVIDAD"  
        fechahoragrabacion = request.POST.get('idfechaactgra')
        usuario = request.POST.get('idusuarioact')

    consulta_sql = """
            INSERT INTO {}.bitacora(codigo, titulo, fecha, hora, descripcion, detalle, observaciones, vendor, estado, pais, tipo, fechahoragrabacion, usuariocrea) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """.format(dbrbs)
    try:
        mycursor.execute(consulta_sql, (codigoact, titulo, fechain, hora, descripcion, detalle, observacion, vendor, estado, pais, tipo, fechahoragrabacion, usuario))
        mydb.commit()
    except ConnectionError as e:
        print(f"Error de conexión: {e}")
        print(f"Mensaje de error detallado: {e.args[0]}") 
    except TimeoutError as e:
        print(f"Error de tiempo de espera: {e}")
    except OSError as e:
        print(f"Error del sistema operativo: {e}")
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
        mydb.rollback()
    finally:
        mycursor.close()
        mydb.close()  

    return render(request,'paginas/catalogos.html',
                {   'opcion':'actividades',  
                    'headtable':headselector('actividades'), 
                    'resultado':resultado,
                    'vendors':vendors,
                    'paises':paises,
                    'estados':estados,     
                    'dbs': esquemata(),
                    'user': username,
                }) 


def agregarsr(request):
    dbrbs = "dblocalip06102024"
    username = request.session.get('username', None)
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()

    if request.method == 'POST':
        print("--------------------------------------------------------------------------------------------------------------------------")
        codigoact_input = request.POST.get('ididentificadorsr')
        print(f"codigoact_input: {codigoact_input}")
        codigoact = validate_input(codigoact_input)
        print(f"codigoact: {codigoact}")

        titulo_input = request.POST.get('idtitulosr')
        print(f"titulo_input: {titulo_input}")
        titulo = validate_input(titulo_input, max_length=95)
        print(f"titulo: {titulo}")

        fecha = request.POST.get('fechasr')
        fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')  
        fechain = fecha_dt.strftime('%d/%m/%Y')
        print(fechain)
        hora = request.POST.get('horasr')
        print(hora)
        descripcion = validate_input(request.POST.get('iddescripcionsr'), max_length=145, default_value='sin_descripcion')
        print(descripcion)
        detalle = validate_input(request.POST.get('iddetallesr'), max_length=195, default_value='sin_detalle')
        print(detalle)
        observacion = ""
        vendor = request.POST.get('idvendorsr') 
        print(vendor)
        estado = "OPEN"
        paispagina = request.POST.get('idpaissr')
        print(paispagina)
        pais = conviertepais(paispagina)
        print(pais)
        tipo = "SR" 
        fechahoragrabacion = request.POST.get('idfechahorasr')
        print(fechahoragrabacion)
        usuario = request.POST.get('idusuariosr')
        print(usuario)
        print("----------------------------------------------------------------------------------------------------------------------------")
    consulta_sql = """
            INSERT INTO {}.bitacora(codigo, titulo, fecha, hora, descripcion, detalle, observaciones, vendor, estado, pais, tipo, fechahoragrabacion, usuariocrea) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """.format(dbrbs)
    try:
        mycursor.execute(consulta_sql, (codigoact, titulo, fechain, hora, descripcion, detalle, observacion, vendor, estado, pais, tipo, fechahoragrabacion, usuario))
        mydb.commit()
        return redirect('catalogos')
    except ConnectionError as e:
        print(f"Error de conexión: {e}")
        print(f"Mensaje de error detallado: {e.args[0]}") 
    except TimeoutError as e:
        print(f"Error de tiempo de espera: {e}")
    except OSError as e:
        print(f"Error del sistema operativo: {e}")
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
        mydb.rollback()
    finally:
        mycursor.close()
        mydb.close()  

    return render(request,'paginas/catalogos.html',
                {   'opcion':'actividades',  
                    'headtable':headselector('actividades'), 
                    'resultado':resultado,
                    'vendors':vendors,
                    'paises':paises,
                    'estados':estados,     
                    'dbs': esquemata(),
                    'user': username, 
                }) 


def actualizaractividad(request, registroact, fechaactmodal, actualizacion, usuarioact, estadoact, vendoract): 
    dbrbs = "dblocalip06102024"
    mydb = conexion_dbown(dbrbs)
    mycursor = mydb.cursor() 
    fechahex = bytes.fromhex(fechaactmodal) 
    fechaactualizacion = fechahex.decode('utf-8')

    if request.method == 'POST':
        fechafin = ""
        horafin = ""
        fechahoragrabacion = fechaactualizacion
        rma = "" 
        ttrma = ""
        if len(actualizacion) > 195:
            actualizacion = actualizacion[:195]
        detalle = ""
        observacion = ""
        usuariomodifica = usuarioact 
        estadomodifica = estadoact
        vendormodifica = vendoract
        paismodifica = ""
        bitacora_registrosractividad = registroact

    consulta_sql = """
        INSERT INTO {}.registrobitacora(fechafin, horafin, fechahoragrabacion, rma, ttrma, actualizacion, detalle, observacion, usuariomodifica, estadomodifica, vendormodifica, paismodifica, bitacora_registrosractividad) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """.format(dbrbs)
    
    consulta_sql_update = """
            UPDATE {}.bitacora 
            SET estado = %s, vendor = %s 
            WHERE registrosractividad = %s
        """.format(dbrbs)

    try:
        mycursor.execute(consulta_sql, (fechafin, horafin, fechahoragrabacion, rma, ttrma, actualizacion, detalle, observacion, usuariomodifica, estadomodifica, vendormodifica, paismodifica, bitacora_registrosractividad))
        mydb.commit()
        mycursor.execute(consulta_sql_update, (estadoact, vendoract, registroact))
        mydb.commit()

    except ConnectionError as e:
        print(f"Error de conexión: {e}")
        print(f"Mensaje de error detallado: {e.args[0]}") 
    except TimeoutError as e:
        print(f"Error de tiempo de espera: {e}")
    except OSError as e:
        print(f"Error del sistema operativo: {e}")
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
        mydb.rollback() 
    finally:
        mycursor.close()
        mydb.close() 

    return JsonResponse({'success': False, 'message': 'Método no permitido.'})


def actualizarsrs(request, registrosr, fechahoragrabacion, rma, ttrma, fecharmasr, actualizacion, usuariosr, estadosr, vendorsr, paissr):
    dbrbs = "dblocalip06102024"
    mydb =  conexion_dbown(dbrbs)
    mycursor = mydb.cursor()
    fechahex = bytes.fromhex(fecharmasr) 
    fechaactualizacion = fechahex.decode('utf-8')


    if request.method == 'POST':
        fechafin = ""
        horafin = ""
        fechahoragrabacion = bytes.fromhex(fechahoragrabacion).decode('utf-8')
        rma = rma 
        ttrma = ttrma
        if len(actualizacion) > 195:
            actualizacion = actualizacion[:195]
        detalle = ""
        observacion = fechaactualizacion
        usuariomodifica = usuariosr
        estadomodifica = estadosr
        vendormodifica = vendorsr
        paismodifica = paissr
        bitacora_registrosractividad = registrosr

    consulta_sql = """
            INSERT INTO {}.registrobitacora(fechafin, horafin, fechahoragrabacion, rma, ttrma, actualizacion, detalle, observacion, usuariomodifica, estadomodifica, vendormodifica, paismodifica, bitacora_registrosractividad) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """.format(dbrbs)
    
    consulta_sql_update = """
            UPDATE {}.bitacora 
            SET estado = %s, vendor = %s 
            WHERE registrosractividad = %s
        """.format(dbrbs)
    try:
        print("---------------------------------- variable rma a punto de ser insertada en la db")
        print(rma)
        mycursor.execute(consulta_sql, (fechafin, horafin, fechahoragrabacion, rma, ttrma, actualizacion, detalle, observacion, usuariomodifica, estadomodifica, vendormodifica, paismodifica, bitacora_registrosractividad))
        mydb.commit()
        mycursor.execute(consulta_sql_update, (estadosr, vendorsr, paissr))
        mydb.commit()  
    except ConnectionError as e:
        print(f"Error de conexión: {e}")
        print(f"Mensaje de error detallado: {e.args[0]}") 
    except TimeoutError as e:
        print(f"Error de tiempo de espera: {e}")
    except OSError as e:
        print(f"Error del sistema operativo: {e}")
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
        mydb.rollback()
    finally:
        mycursor.close()
        mydb.close() 

    return JsonResponse( {'success': False, 'message': 'Método no permitido.'})



def  headselector(selectedoption):
    if selectedoption == 'actividades':
        headtable = ["ACTIVIDAD", "TÍTULO", "FECHA ACTIVIDAD", "HORA", "DESCRIPCIÓN", "VENDOR", "ESTADO","OPCIÓN"]
    elif selectedoption == 'casossr':
        headtable = ["DÍAS","CASO SR", "TÍTULO", "APERTURA", "HORA", "DESCRIPCIÓN", "RMA", "DETALLE", "VENDOR","ESTADO","PAÍS","OPCIÓN"]
    else:
        headtable = []
    return headtable



def traelistasselectsmodal(request): #CARGAR SELECTED MODALES 
    return JsonResponse(
        {
        'estados': estados,
        'vendors': vendors,
        'paises': paises,
        })


def actualizacionactividades(request, registroactividad):
    dbrbs = "dblocalip06102024"
    mydb = conexion_dbown(dbrbs)
    mycursor = mydb.cursor() 
    
    query = """
        SELECT idregistro, fechahoragrabacion, actualizacion, usuariomodifica 
        FROM registrobitacora 
        WHERE bitacora_registrosractividad = %s
        ORDER BY idregistro ASC
    """
    params = (registroactividad,) 
    mycursor.execute(query, params)
    listaactualizacionactividad = mycursor.fetchall()

    resultado = [
        {
            'idregistro': row[0],
            'fechahoragrabacion': row[1],
            'actualizacion': row[2],
            'usuariomodifica': row[3]
        }
        for row in listaactualizacionactividad
    ]

    return JsonResponse({'listaactualizacionactividad': resultado})



def conviertepais(pais):
    paises = {
        "GUATEMALA": "GT",
        "HONDURAS": "HN",
        "NICARAGUA": "NI",
        "EL SALVADOR": "SV",
        "COSTA RICA": "CR"
    }
    return paises.get(pais, "País desconocido")


def validate_input(input_string, max_length=None, default_value=None):
    if input_string is None:
        return default_value

    cleaned_string = re.sub(r'[^\w\.\s]', '_', input_string)

    if not cleaned_string:
        return default_value

    if max_length and len(cleaned_string) > max_length:
        return cleaned_string[:max_length]

    return cleaned_string