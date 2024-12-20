import re
import logging
from django.shortcuts import redirect, render
from django.db import connection
from datetime import datetime
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import * 
from iphysearchapp.connect import *
from appsearch.varias_func import *
from appsearch.busca_ips import * 
from models import Registrobitacora
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.utils import OperationalError
from django.db import connections
from django.shortcuts import redirect, render
from django.urls import reverse 
from models import *
from django.contrib.auth.decorators import login_required 


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

dbrbs = "dblocal_default"
username = "sin_usuario_logg"
HEADTABLESR = ["NO.","DÍAS","CASO SR", "TÍTULO", "APERTURA", "DESCRIPCION", "DETALLE-RMA", "VENDOR","ESTADO","PAÍS","OPCIÓN"]

@login_required
def casossr(request, pagina):
    username = request.user.username
    idtxtabuscar = request.GET.get('idtxtabuscarsr')
    fecha_strsrini = request.GET.get('idfechabusquedasrini')
    fecha_strsrfin = request.GET.get('idfechabusquedasrfin')
    estadoasr = request.GET.get('estadosr')
    nregistros = 0
    conexiondb = 0
    tipo = "SR"
    opcion = 'casos SR'
    conexiondb = probar_conexion_db(DBMANTTOLOCAL)


    if request.method == "POST":
        insertar_registros_sr(request)
        return redirect(reverse('agregar_sr', kwargs={'pagina': pagina}))
    
    is_range_search = fecha_strsrini and fecha_strsrfin

    if is_range_search:
        
        pagina =1
        total_paginas = 1
        rango_paginas = [1]
        listarsr = muestraregistrossr(idtxtabuscar, fecha_strsrini, fecha_strsrfin, estadoasr, tipo, pagina, None, pagina)
        
    else:
        nregistros = conteoderegistros(estadoasr, tipo)
        total_paginas = (nregistros // ndivisor) + (1 if nregistros % ndivisor > 0 else 0) 
        inicio = max(1, pagina - max_paginas // 2)
        fin = min(total_paginas, inicio + max_paginas - 1)
        if fin - inicio < max_paginas:
            inicio = max(1, fin - max_paginas + 1)
        rango_paginas = list(range(inicio, fin + 1))    
        offset = (pagina - 1) * ndivisor  
        limit = ndivisor
        listarsr = muestraregistrossr(idtxtabuscar, None, None, estadoasr, tipo, limit, offset, pagina)

    return render(request, 'paginas/casossr.html', {
        'opcion': opcion,
        'listasr': listarsr,
        'HEADTABLESR': HEADTABLESR,
        'proveedores': proveedores,
        'conexiondb':conexiondb,
        'paises': paises,
        'estados': estados,
        'nregistros': nregistros,
        'ndivisor': ndivisor,
        'pagina_actual': pagina,
        'total_paginas': total_paginas,
        'rango_paginas': rango_paginas,
        'user': username,
    })



def muestraregistrossr(idtxtabuscar, fecha_strsrini, fecha_strsrfin, estadoasr, tipo, limit, offset, pagina): 
    listarsr = []
    mydb = conexion_dbown(DBMANTTOLOCAL)
    mycursor = mydb.cursor()

    query = """
        SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
        FROM bitacora
        WHERE 1=1
    """
    params = []

    if idtxtabuscar:
        query += " AND (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s)"
        params.extend(['%' + idtxtabuscar + '%'] * 3)

    if fecha_strsrini and fecha_strsrfin:
        fecha_formateada_ini = fecha_strsrini.split('-')[2] + '/' + fecha_strsrini.split('-')[1] + '/' + fecha_strsrini.split('-')[0]
        fecha_formateada_fin = fecha_strsrfin.split('-')[2] + '/' + fecha_strsrfin.split('-')[1] + '/' + fecha_strsrfin.split('-')[0]
        query += " AND STR_TO_DATE(fecha, '%d/%m/%Y') BETWEEN STR_TO_DATE(%s, '%d/%m/%Y') AND STR_TO_DATE(%s, '%d/%m/%Y')"
        params.extend([fecha_formateada_ini, fecha_formateada_fin])
    elif fecha_strsrini:
        fecha_formateada = fecha_strsrini.split('-')[2] + '/' + fecha_strsrini.split('-')[1] + '/' + fecha_strsrini.split('-')[0]
        query += " AND STR_TO_DATE(fecha, '%d/%m/%Y') >= STR_TO_DATE(%s, '%d/%m/%Y')"
        params.append(fecha_formateada)
    elif fecha_strsrfin:
        fecha_formateada = fecha_strsrfin.split('-')[2] + '/' + fecha_strsrfin.split('-')[1] + '/' + fecha_strsrfin.split('-')[0]
        query += " AND STR_TO_DATE(fecha, '%d/%m/%Y') <= STR_TO_DATE(%s, '%d/%m/%Y')"
        params.append(fecha_formateada)

    if estadoasr not in [None, "", "ESTADO"]:
        query += " AND estado = %s"
        params.append(estadoasr)

    query += " AND tipo = %s"
    params.append(tipo)

    if limit is not None and offset is not None:
        query += " LIMIT %s OFFSET %s"
        params.extend([limit, offset])


    mycursor.execute(query, params)
    listarsr = mycursor.fetchall()
   
    for i in range(len(listarsr)):
        registro_id = listarsr[i][0]
        rma_list = obtener_rma_por_id(registro_id)
        registro_total = (pagina - 1) * limit + (i + 1)
        listarsr[i] += (rma_list, registro_total, '3')

    return listarsr

def obtener_rma_por_id(registro_id):    
    registros = Registrobitacora.objects.using('dblocal_mantto').filter(
        bitacora_registrobitacora=registro_id,
        clase__in=['0', '1']  
    ).order_by('-clase').values()  

    if not registros:  
        return []  

    registro_prioritario = registros[0]
    
    return [registro_prioritario]  

def obtener_rma_por_id(registro_id):
    registros = Registrobitacora.objects.using('dblocal_mantto').filter(
        bitacora_registrobitacora=registro_id,
        clase__in=['0', '1']
    ).order_by('rma', '-clase').values(
        'idregistro', 'fechafin', 'horafin', 'fechacierre', 'horacierre', 'fechahoragrabacion', 
        'rma', 'ttrma', 'actualizacion', 'detalle', 'observacion', 'usuariomodifica', 'estadomodifica', 'vendormodifica', 'paismodifica', 'clase', 'bitacora_registrobitacora'
    )

    if not registros:
        return []

    registros_agrupados = {}
    for registro in registros:
        rma = registro.get('rma') 
        if not rma:
            continue  
        
        if rma not in registros_agrupados:
            registros_agrupados[rma] = registro 
        elif registro['clase'] == '1':  
            registros_agrupados[rma] = registro

    return list(registros_agrupados.values())



def insertar_registros_sr(request):
    try:
        codigoact = clean_input(request.POST.get('ididentificadorsr'), max_length=45, default_value="0")
        titulo = clean_input(request.POST.get('idtitulosr'), max_length=150, default_value="sin_titulo")
        fecha_stact = request.POST.get('idfechasr')  
        hora = request.POST.get('idhorasr')
        descripcion = clean_input(request.POST.get('iddescripcionsr'), max_length=200, default_value="sin_descripcion_act")
        falla = clean_input(request.POST.get('idfalla'), max_length=50, default_value="sin_falla_act").upper()
        hostname= clean_input(request.POST.get('idhostname'), max_length=75, default_value="sin_hostname_act").upper()
        iphost= clean_input(request.POST.get('idip'), max_length=50, default_value="sin_iphost_act")
        proveedor = request.POST.get('idproveedores')
        pais = request.POST.get('idpaissr')
        fechahoragrabacion = request.POST.get('idfechahorasr')
        usuario = request.POST.get('idusuariosr')

        if fecha_stact:
            try:
                fecha_dtact = datetime.strptime(fecha_stact, '%Y-%m-%d')
                fecha = fecha_dtact.strftime('%d/%m/%Y')
            except ValueError:
                fecha = None
        else:
            fecha = None

        bitacora = Bitacora(
            codigo=codigoact,
            titulo=titulo,
            fecha=fecha,
            hora=hora,
            descripcion=descripcion,
            detalle=falla+"-"+hostname+"-"+iphost,
            observaciones="0",
            vendor=proveedor,
            estado="OPEN",
            pais=conviertepais(pais), 
            tipo="SR",
            fechahoragrabacion=fechahoragrabacion,
            usuariocrea=usuario
        )
        bitacora.save(using='dblocal_mantto')
        logger.info(f"Registro agregado exitosamente con ID {bitacora.registrosractividad}.")
        return {"status": "success", "message": "Registro insertado correctamente."}

    except Exception as e:
        logger.error(f"Error al guardar el registro: {e}")
        return {"status": "error", "message": f"Error al guardar el registro: {e}"}
    


def actualizarsrs(request, pagina, registrosr, fechahoragrabacion, rma, ttrma, fecharmain, actualizacion, usuariosr, estadosr, vendorsr, paissr):

    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}) 

    try:
        try:
            fechaactualizacion = bytes.fromhex(fecharmain).decode('utf-8')
            fechahoragrabacion = bytes.fromhex(fechahoragrabacion).decode('utf-8')
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Formato de fecha inválido.'})
        
        try:
            bitacora_instance = Bitacora.objects.using(DBMANTTOLOCAL).get(registrosractividad=registrosr)
        except Bitacora.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Registro de Bitácora no encontrado.'})
        
        if not rma or rma == '0':
            fechaactualizacion = '0'
            clase = 'act-sr'
        else:
            clase = '0'

        if not ttrma:
            ttrma = '0'

        actualizacion = actualizacion[:195] if len(actualizacion) > 195 else actualizacion

        registro = Registrobitacora(
            fechafin=fechaactualizacion, 
            horafin="0",
            fechacierre="0",
            horacierre="0",
            fechahoragrabacion=fechahoragrabacion,
            rma=rma,
            ttrma=ttrma,
            actualizacion=actualizacion,
            detalle="0",  
            observacion="0",
            usuariomodifica=usuariosr,
            estadomodifica="OPEN",
            vendormodifica=vendorsr,
            paismodifica=paissr,
            clase=clase,
            bitacora_registrobitacora=bitacora_instance       
        )
        registro.save(using='dblocal_mantto')
        bitacora_instance.estado = estadosr
        bitacora_instance.vendor = vendorsr
        bitacora_instance.save(using='dblocal_mantto')

        return JsonResponse({'success': True, 'message': 'Registro actualizado exitosamente.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error al procesar la solicitud: {str(e)}'})



def cierrermas(request, pagina, registrosr, fechahoragrabacion, rmarecibido, ttrmarecibido, fecharmasrcierre, actualizacioncierre, usuariosr, estadosr, vendorsr, paissr):

    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Método no permitido.'})
    
    try:
        try:
            fechaactualizacion = bytes.fromhex(fecharmasrcierre).decode('utf-8')
            fechahoragrabacion = bytes.fromhex(fechahoragrabacion).decode('utf-8')
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Formato de fecha inválido.'})
        
            
        actualizacioncierre = actualizacioncierre[:195] if len(actualizacioncierre) > 195 else actualizacioncierre

        try:
            bitacora_instance = Bitacora.objects.using('dblocal_mantto').get(registrosractividad=registrosr)
        except Bitacora.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Registro de Bitácora no encontrado.'})

        registro = Registrobitacora(
            fechafin="0", 
            horafin="0",
            fechacierre=fechaactualizacion,
            horacierre="0",
            fechahoragrabacion=fechahoragrabacion,
            rma=rmarecibido, 
            ttrma=ttrmarecibido,
            actualizacion=actualizacioncierre,
            detalle="0",  
            observacion="0",
            usuariomodifica=usuariosr,
            estadomodifica="CLOSED",
            vendormodifica=vendorsr,
            paismodifica=paissr,
            clase="1",
            bitacora_registrobitacora=bitacora_instance       
        )
        registro.save(using='dblocal_mantto')
      

        return JsonResponse({'success': True, 'message': 'Registro actualizado exitosamente.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error al procesar la solicitud: {str(e)}'})


def traelistasselectsmodal(request): #CARGAR SELECTED MODALES 
    return JsonResponse(
        {
        'estados': estados,
        'vendors': vendors,
        'paises': paises,
        })


def conviertepais(pais):
    paises = {
        "GUATEMALA": "GT",
        "HONDURAS": "HN",
        "NICARAGUA": "NI",
        "EL SALVADOR": "SV",
        "COSTA RICA": "CR"
    }
    return paises.get(pais, "País desconocido")


def clean_input(input_string, max_length=None, default_value=None):
    if input_string is None:
        return default_value

    cleaned_string = re.sub(r'[^\w\.\s]', '_', input_string)

    if not cleaned_string:
        return default_value

    if max_length and len(cleaned_string) > max_length:
        return cleaned_string[:max_length]

    return cleaned_string


def conteoderegistros(estado, tipo):
    query = Bitacora.objects.using(DBMANTTOLOCAL).filter(tipo=tipo)
    if estado is not None and estado != "ESTADO":
        query = query.filter(estado=estado)
    return query.count()

def obtiene_proveedores_estados_paises(request, pagina):
    return JsonResponse({'proveedores': proveedores, 'paises': paises, 'estados': estados})


def mostrarInformacionDescripcionsr(request, registro):
    query = Bitacora.objects.using(DBMANTTOLOCAL).filter(registrosractividad=registro)
    
    if query.exists():
        resultado = query.first().descripcion  
        return JsonResponse({'descripcionSR': resultado})
    else:
        return JsonResponse({'error': 'No se encontró la descripción'}, status=404)
    
    
def probar_conexion_db(db_alias):
    try:
        connection = connections[db_alias]
        connection.ensure_connection()
        return 0
    except OperationalError as e:
        return 1