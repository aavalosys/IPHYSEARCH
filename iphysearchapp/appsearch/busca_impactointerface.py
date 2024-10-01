from django.shortcuts import render
from mysql.connector import Error
from django.core.cache import cache
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *

def impactointerfaces(request):
    db = request.GET.get('dbstr')
    ip = request.GET.get('strbuscado') 
    pais = '-'
    interface='-'
    tabla_mac_vlan='-'
    conteo_vlan_mac='-'

    if db is not None and ip is not None:
        listadointerfaces = buscainterfaces(db, ip)
        pais = obtenerpais(db,ip)
    else:
        ip = '-'
        listadointerfaces = ''
        pais = '-'
        interface='-'
        db = '-'
        tabla_mac_vlan='-'
        conteo_vlan_mac='-'
    return render(request,'paginas/buscaimpactointerface.html',
                {   'db':db,  
                    'ip':ip,
                    'pais':pais,
                    'interface':interface, 
                    'tabla_mac_vlan':tabla_mac_vlan,
                    'conteo_vlan_mac':conteo_vlan_mac,
                    'listadointerfaces':listadointerfaces,   
                    'dbs': esquemata(),
                    'user': usuariolog(),
                })


def verimpactointerface(request, ip, no, dbinter, pais):

    interface='-'
    tabla_mac_vlan='-'
    conteo_vlan_mac='-'
    listadointerfaces = buscainterfaces(dbinter, ip)

    for inter in listadointerfaces:
        if int(inter[0])==int(no):
            interface = inter[2]
            break
        else:
            interface='--'

    ippe = obtenpeL3(dbinter, ip, pais)         #BUSCA LA IP DEL L3

    conteo_vlan_mac, tabla_mac_vlan = contar_vlans_inter(ippe, dbinter, ip, pais, interface)

    return render(request,'paginas/buscaimpactointerface.html',
                {   'db':dbinter,  
                    'ip':ip,
                    'pais':pais,
                    'interface':interface, 
                    'listadointerfaces':listadointerfaces,
                    'tabla_mac_vlan':tabla_mac_vlan,
                    'conteo_vlan_mac':conteo_vlan_mac,   
                    'dbs': esquemata(),
                    'user': usuariolog(),
                })

    
def buscainterfaces(db, idtxtabuscar): 
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ROW_NUMBER() OVER (ORDER BY resultado.ip) AS correlativo, resultado.*, '" + 
                    db + "' AS db FROM ( SELECT * FROM " +
                    db + ".int_gt UNION  SELECT * FROM "+ 
                    db + ".int_sv UNION  SELECT * FROM "+ 
                    db + ".int_hn UNION  SELECT * FROM "+ 
                    db + ".int_ni UNION  SELECT * FROM "+ 
                    db + ".int_cr UNION  SELECT * FROM "+
                    db + ".int_xt ) AS resultado WHERE resultado.ip LIKE '"+
                    idtxtabuscar + "' and description not like '%LIBRE%' and interface not like '%NULL%'")
    resultadointerfaces = mycursor.fetchall()
    mydb.close()
    return resultadointerfaces


  

    


