import re
import requests
from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from appsearch.busca_ips import *
from .models import *
 

def buscavarios(request, selectedoption):
    resultado =""
    opcion ="Ninguna..."
    headtable = ["!!!!", "!!!", "!!", "!", "!", "?"]
    db = request.GET.get('dbstr')
    idtxtabuscar = request.GET.get('strbuscado')

    if selectedoption == 'mac':
        opcion = 'mac'
        headtable = headselector(selectedoption)
    elif selectedoption == 'equipos':
        opcion = 'equipos'
        headtable = headselector(selectedoption)
    elif selectedoption == 'descripciones':
        opcion = 'descripciones'
        headtable = headselector(selectedoption)
    elif selectedoption == 'arp':
        opcion = 'arp'
        headtable = headselector(selectedoption)
    elif selectedoption == 'valoresopticos':
        opcion = 'valores ópticos'
        headtable = headselector(selectedoption)


    if db is not None and idtxtabuscar is not None:
        if selectedoption == 'mac':
            resultado = buscamacs(db, idtxtabuscar)
        elif selectedoption == 'equipos':
            resultado = buscaequipos(db, idtxtabuscar)
        elif selectedoption == 'descripciones':
            resultado = buscadescripcion(db, idtxtabuscar)
        elif selectedoption == 'arp':
            resultado = buscaarp(db, idtxtabuscar)
        elif selectedoption == 'valoresopticos':
            resultado = buscavaloresopticos(db, idtxtabuscar)
    else:
        return render(request,'paginas/buscavarios.html',
                {   'opcion':opcion,  
                    'headtable':headtable, 
                    'resultado':resultado,    
                    'dbs': esquemata(),
                })
        
    return render(request,'paginas/buscavarios.html',
                {   'opcion':opcion,  
                    'headtable':headtable, 
                    'resultado':resultado,    
                    'dbs': esquemata(),
                })


def buscamacs(db, idtxtabuscar): 
    idtxtabuscar = formatear_direccion_mac(idtxtabuscar) 
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ( SELECT *, 'GT' AS table_name FROM "+ 
                     db + ".mac_address_gt UNION  SELECT *, 'SV' AS table_name FROM "+ 
                     db + ".mac_address_sv UNION  SELECT *, 'HN' AS table_name FROM "+ 
                     db + ".mac_address_hn UNION  SELECT *, 'NI' AS table_name FROM "+ 
                     db + ".mac_address_ni UNION  SELECT *, 'CR' AS table_name FROM "+ 
                     db + ".mac_address_cr UNION  SELECT *, 'XT' AS table_name FROM "+
                     db + ".mac_address_xt ) AS resultado WHERE resultado.mac LIKE '%" + 
                     idtxtabuscar + "%'") 
    resultadomacs = mycursor.fetchall()
    mydb.close()
    return resultadomacs

def buscaarp(db, idtxtabuscar):
    idtxtabuscarip = idtxtabuscar
    idtxtabuscarmac = formatear_direccion_mac(idtxtabuscar)          
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    paracpe = ('%' + idtxtabuscarmac,)
    mycursor.execute(CPEARP.format(db, db, db, db, db), paracpe)
    resultados = mycursor.fetchall()
    listaips = [(resultado + (db,)) for resultado in resultados]
    
    if not resultados:
        listaips = buscacaipcpe(db, idtxtabuscarip)
        mydb.close()
    else:
        mydb.close()
  
    return listaips 


def buscaequipos(db, txtequipo):       
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT hostname, ip, localidad, localidad2, pais, modelo, version, vendor, rol FROM "+ db +".equipos WHERE hostname LIKE '%" + txtequipo + "%'")
    resultadoequipos = mycursor.fetchall()

    if not resultadoequipos:
        mycursor.execute("SELECT hostname, ip, localidad, localidad2, pais, modelo, version, vendor, rol  FROM "+ db +".equipos WHERE ip LIKE '%" + txtequipo + "%'")
        resultadoequipos = mycursor.fetchall()
        mydb.close()
    else:
        mydb.close()
    return resultadoequipos

def buscadescripcion(db, idtxtabuscar):
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ip, interface, estado, description, CASE table_name  WHEN 'GT' "+
                     "THEN 'GT' WHEN 'SV' "+
                     "THEN 'SV' WHEN 'HN'"+ 
                     "THEN 'HN' WHEN 'NI'"+ 
                     "THEN 'NI' WHEN 'CR'"+ 
                     "THEN 'CR' WHEN 'XT'"+ 
                     "THEN 'XT' ELSE 'Desconocido' END AS"+ 
                     "pais FROM ( SELECT ip, interface, estado, description , 'GT' AS table_name FROM "+ 
                     db + ".int_gt  UNION  SELECT ip, interface, estado, description , 'SV' AS table_name FROM "+ 
                     db + ".int_sv  UNION  SELECT ip, interface, estado, description , 'HN' AS table_name FROM "+ 
                     db + ".int_hn  UNION  SELECT ip, interface, estado, description , 'NI' AS table_name FROM "+ 
                     db + ".int_ni  UNION  SELECT ip, interface, estado, description , 'CR' AS table_name FROM "+ 
                     db + ".int_cr UNION  SELECT ip, interface, estado, description , 'XT' AS table_name FROM "+
                     db + ".int_xt  ) AS resultado WHERE resultado.description LIKE '%" + 
                     idtxtabuscar + "%'") 
    resultadodescripcion = mycursor.fetchall()
    mydb.close()
    return resultadodescripcion


def buscavaloresopticos(db, idtxtabuscar):          
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ip, interface, description, bw, rx, tx, CASE table_name  WHEN 'GT' "+
                     "THEN 'GT' WHEN 'SV' "+
                     "THEN 'SV' WHEN 'HN'"+ 
                     "THEN 'HN' WHEN 'NI'"+ 
                     "THEN 'NI' WHEN 'CR'"+ 
                     "THEN 'CR' WHEN 'XT'"+ 
                     "THEN 'XT' ELSE 'Desconocido' END AS"+ 
                     "pais FROM ( SELECT ip, interface, description, bw, rx, tx,'GT' AS table_name FROM "+ 
                     db + ".int_gt  UNION  SELECT ip, interface, description, bw, rx, tx, 'SV' AS table_name FROM "+ 
                     db + ".int_sv  UNION  SELECT ip, interface, description, bw, rx, tx, 'HN' AS table_name FROM "+ 
                     db + ".int_hn  UNION  SELECT ip, interface, description, bw, rx, tx, 'NI' AS table_name FROM "+ 
                     db + ".int_ni  UNION  SELECT ip, interface, description, bw, rx, tx, 'CR' AS table_name FROM "+ 
                     db + ".int_cr UNION  SELECT ip, interface, description, bw, rx, tx, 'XT' AS table_name FROM "+
                     db + ".int_xt  ) AS resultado WHERE resultado.ip LIKE '%" + 
                     idtxtabuscar + "%' AND resultado.description NOT LIKE '%LIBRE%' AND resultado.interface NOT LIKE '%NULL0%'"+
                     "AND resultado.rx <> ''") 
    resultadodescripcion = mycursor.fetchall()
    mydb.close()
    return resultadodescripcion

def  headselector(selectedoption):
    if selectedoption == 'mac':
        headtable = ["IP EQUIPO", "MAC BUSCADA", "VLAN", "INTERFACE", "#", "PAÍS"]
    elif selectedoption == 'arp':
        headtable = ["IP PE", "IP ELEMENTO", "MAC", "VLAN", "INTERFACE", "VRF", "PAIS", "DB"]
    elif selectedoption == 'equipos':
        headtable = ["HOSTNAME", "IP EQUIPO", "UBICACION NEMONICO", "UBICACION SNMP","PAIS", "MODELO", "VERSIÓN", "MARCA", "ROL"]
    elif selectedoption == 'descripciones':
        headtable = ["IP EQUIPO", "INTERFACE", "ESTADO", "DESCRIPCION", "PAÍS"]
    elif selectedoption == 'valoresopticos':
        headtable = ["IP EQUIPO", "INTERFACE", "DESCRIPCIÓN", "BW", "TX", "RX", "PAÍS"]
    else:
        headtable = ["X", "X", "X", "X", "X", "?"]

    return headtable

def formatear_direccion_mac(idtxtabuscar):
    # Eliminar caracteres no deseados como ":" y "-"
    idtxtabuscar = re.sub(r'[^a-fA-F0-9]', '', idtxtabuscar)
    nueva_direccion_mac = f'{idtxtabuscar[:4]}.{idtxtabuscar[4:8]}.{idtxtabuscar[8:]}'
    return nueva_direccion_mac.lower()
   