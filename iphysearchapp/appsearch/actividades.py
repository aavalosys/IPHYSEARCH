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
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.utils import OperationalError
from django.db import connections
from django.shortcuts import redirect, render
from django.urls import reverse 
from models import *
from django.contrib.auth.decorators import login_required, user_passes_test

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

headtable = ["NO.","ACTIVIDAD", "TÍTULO", "FECHA ACTIVIDAD", "DESCRIPCIÓN", "VENDOR", "ESTADO","OPCIÓN"] 
dbrbs = "dblocal_default"
dbrbsmantto = "dblocal_mantto"

def grupo_requerido(grupos_permitidos, respuesta, errordes, errores):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=grupos_permitidos).exists():
                return view_func(request, *args, **kwargs)
            else:
                # Renderiza la página de error con los parámetros proporcionados
                return render(request, 'errorpage.html', {
                    'respuesta': respuesta,
                    'errordes': errordes,
                    'errores': errores
                })
        return _wrapped_view
    return decorator

@login_required
@grupo_requerido(
    grupos_permitidos=['superuser','adminusers', 'especialistas'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def actividades(request, pagina):
    username = request.user.username  
    idtxtabuscar = request.GET.get('idtxtabuscaract')
    fecha_stract = request.GET.get('idfechabusquedaact')
    estadoact = request.GET.get('idestadoact')
    nregistros = 0
    listaract = []
    tipo = "ACTIVIDAD"
    opcion = 'actividades'
    conexiondb = probar_conexion_db(dbrbsmantto)

    if request.method == "POST":
        insertar_registros_act(request)
        return redirect(reverse('agregar_act', kwargs={'pagina': pagina}))
    
    nregistros = conteoderegistros(estadoact, tipo)
    total_paginas = (nregistros // ndivisor) + (1 if nregistros % ndivisor > 0 else 0)
    inicio = max(1, pagina - max_paginas // 2)
    fin = min(total_paginas, inicio + max_paginas - 1)
    if fin - inicio < max_paginas:
        inicio = max(1, fin - max_paginas + 1)
    rango_paginas = list(range(inicio, fin + 1))
    offset = (pagina - 1) * ndivisor
    limit = ndivisor
    listaract = muestraregistrosact(idtxtabuscar, fecha_stract, estadoact, tipo, limit, offset, pagina)

    return render(request, 'paginas/actividades.html', {
        'opcion': opcion,
        'listaract': listaract,
        'headtable': headtable,
        'vendors': vendors,
        'conexiondb': conexiondb,
        'paises': paises,
        'estados': estados,
        'nregistros': nregistros,
        'ndivisor': ndivisor,
        'pagina_actual': pagina,
        'total_paginas': total_paginas,
        'rango_paginas': rango_paginas,
        'user': username,
    })



def muestraregistrosact(idtxtabuscar, fecha_str, estado, tipo, limit, offset, pagina): 
    listaract = []
    mydb = conexion_dbown(dbrbsmantto)
    mycursor = mydb.cursor()
    query = """
        SELECT *, DATEDIFF(CURDATE(), STR_TO_DATE(fecha, '%d/%m/%Y')) AS contador
        FROM bitacora
        WHERE 1=1
    """
    params = []

    if idtxtabuscar:
        print("entro en idtxtabuscar")
        query += " AND (codigo LIKE %s OR titulo LIKE %s OR descripcion LIKE %s)"
        params.extend(['%' + idtxtabuscar + '%'] * 3)
    if fecha_str:
        fecha_formateada = fecha_str.split('-')[2] + '/' + fecha_str.split('-')[1] + '/' + fecha_str.split('-')[0]
        query += " AND fecha = %s"
        params.append(fecha_formateada) 
    if estado not in [None, "", "ESTADO"]:
        query += " AND estado = %s"
        params.append(estado)

    query += " AND tipo = %s"
    params.append(tipo)
    query += " LIMIT %s OFFSET %s"
    params.extend([limit, offset])
    mycursor.execute(query, params)
    listaract = mycursor.fetchall()

    for i in range(len(listaract)):
        registro_total = (int(pagina) - 1) * ndivisor + (i + 1)
        listaract[i] += (registro_total, '2', '3')  # '2', '3' son placeholders para otros datos
    return listaract


def insertar_registros_act(request):
    try:
        codigoact = clean_input(request.POST.get('ididentificadoract'), max_length=45, default_value="00000000")
        titulo = clean_input(request.POST.get('idtituloact'), max_length=150, default_value="sin_titulo")
        fecha_stact = request.POST.get('idfechaact')  
        hora = request.POST.get('idhoraact')
        descripcion = clean_input(request.POST.get('iddescripcionact'), max_length=200, default_value="sin_descripcion_act")
        vendor = request.POST.get('idvendoract')
        fechahoragrabacion = request.POST.get('idfechaactgra')
        usuario = request.POST.get('idusuarioact')

        if fecha_stact:
            try:
                fecha_dtact = datetime.strptime(fecha_stact, '%Y-%m-%d')
                fecha = fecha_dtact.strftime('%d/%m/%Y')
            except ValueError:
                fecha = None
        else:
            fecha = None

        if not hora:
            hora = None

        bitacora = Bitacora(
            codigo=codigoact,
            titulo=titulo,
            fecha=fecha,
            hora=hora,
            descripcion=descripcion,
            detalle="0",
            observaciones="0",
            vendor=vendor,
            estado="OPEN",
            pais="0",
            tipo="ACTIVIDAD",
            fechahoragrabacion=fechahoragrabacion,
            usuariocrea=usuario
        )
        bitacora.save(using='dblocal_mantto')
        logger.info(f"Registro agregado exitosamente con ID {bitacora.registrosractividad}.")
        return {"status": "success", "message": "Registro insertado correctamente."}

    except Exception as e:
        logger.error(f"Error al guardar el registro: {e}")
        return {"status": "error", "message": f"Error al guardar el registro: {e}"}


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import logging
from models import *

logger = logging.getLogger(__name__)

@csrf_exempt
def actualizaractividad(request, pagina, registroact, fechaactmodal, actualizacion, usuarioact, estadoact, vendoract):
    try:
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Método no permitido.'})

        try:
            fechaactualizacion = bytes.fromhex(fechaactmodal).decode('utf-8')
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Formato de fecha inválido.'})

        actualizacion = clean_input(actualizacion[:195] if len(actualizacion) > 195 else actualizacion, max_length=200, default_value="sin_descripcion_act")

        try:
            bitacora_instance = Bitacora.objects.using('dblocal_mantto').get(registrosractividad=registroact)
        except Bitacora.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Registro de Bitácora no encontrado.'})

        registro = Registrobitacora(
            fechafin="0",
            horafin="0",
            fechacierre="0",
            horacierre="0",
            fechahoragrabacion=fechaactualizacion,
            rma="0",
            ttrma="0",
            actualizacion=actualizacion,
            detalle="0",
            observacion="0",
            usuariomodifica=usuarioact,
            estadomodifica=estadoact,
            vendormodifica=vendoract,
            paismodifica="0",
            clase="act-act",
            bitacora_registrobitacora=bitacora_instance  # Asignar la instancia de Bitacora
        )
        registro.save(using='dblocal_mantto')

        bitacora_instance.estado = estadoact
        bitacora_instance.vendor = vendoract
        bitacora_instance.save(using='dblocal_mantto')

        return JsonResponse({'success': True, 'message': 'Registro actualizado exitosamente.'})

    except Exception as e:
        logger.error(f"Error al procesar la solicitud: {str(e)}")
        return JsonResponse({'success': False, 'message': f'Error al procesar la solicitud: {str(e)}'})


def actualizacionactividades(request, registroactividad):
    registros = Registrobitacora.objects.using(dbrbsmantto).filter(bitacora_registrobitacora=registroactividad).order_by('idregistro')
    resultado = [
        {
            'idregistro': registro.idregistro,
            'fechahoragrabacion': registro.fechahoragrabacion,
            'actualizacion': registro.actualizacion,
            'usuariomodifica': registro.usuariomodifica
        }
        for registro in registros
    ]

    return JsonResponse({'listaactualizacionactividad': resultado})


def clean_input(input_string, max_length=None, default_value=None):
    if input_string is None:
        return default_value
    
    cleaned_string = re.sub(r'[^\w\s\.\-]', '_', input_string.strip())
    if not cleaned_string:
        return default_value
    
    if max_length and len(cleaned_string) > max_length:
        return cleaned_string[:max_length]
    
    return cleaned_string

def conteoderegistros(estado, tipo):
    query = Bitacora.objects.using(dbrbsmantto).filter(tipo=tipo)
    if estado is not None and estado != "ESTADO":
        query = query.filter(estado=estado)

    return query.count()


def obtiene_vendors_estados(request, pagina):
    return JsonResponse({'vendors': vendors, 'estados': estados})

def probar_conexion_db(db_alias):
    try:
        connection = connections[db_alias]
        connection.ensure_connection()
        return 0
    except OperationalError as e:
        return 1
 
def mostrarInformacionDescripcionact(request, registro):
    query = Bitacora.objects.using(dbrbsmantto).filter(registrosractividad=registro)
    
    if query.exists():
        resultado = query.first().descripcion  
        return JsonResponse({'descripcionACT': resultado})
    else:
        return JsonResponse({'error': 'No se encontró la descripción'}, status=404)