from django.shortcuts import render
from mysql.connector import Error
from django.core.cache import cache
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

def impactointerfaces(request):
    db = request.GET.get('dbstr')
    ip = request.GET.get('strbuscado')
    pais = '-'
    interface='-'
    print (db)
    print (ip)
    conteovlans = ''

    if db is not None and ip is not None:
        listadointerfaces = buscainterfaces(db, ip)
        cache_key = f'interfaces_{ip}'
        cache.set(cache_key, {'listadointerfaces': listadointerfaces, 'db': db})
        pais = obtpais(db,ip)
    else:
        ip = '-'
        listadointerfaces = ''
        pais = '-'
        interface='-'
        db = '-'
    return render(request,'paginas/buscaimpactointerface.html',
                {   'db':db,  
                    'ip':ip,
                    'pais':pais,
                    'interface':interface, 
                    'listadointerfaces':listadointerfaces,
                    'conteovlans':conteovlans,   
                    'dbs': esquemata(),
                })

def verimpactointerface(request, ip, no):
    cache_key = f'interfaces_{ip}'
    cached_data = cache.get(cache_key)
    listadointerfaces = cached_data.get('listadointerfaces', [])
    db = cached_data.get('db', '')
    interface='-'

    for inter in listadointerfaces:
        print(inter[0])
        if int(inter[0])==int(no):
            interface = inter[2]
            break
        else:
            interface='--'

    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT vlan, mac  FROM "+db+".mac_address_"+obtpais(db,ip)+
                     " where ip ='"+ip+
                     "' and interface like '%"+interface+"%'")
    tablamac = mycursor.fetchall()
    mydb.close()

    conteovlans = tablamac
    return render(request,'paginas/buscaimpactointerface.html',
                {   'db':db,  
                    'ip':ip,
                    'pais':obtpais(db,ip),
                    'interface':interface, 
                    'listadointerfaces':listadointerfaces,
                    'conteovlans':conteovlans,   
                    'dbs': esquemata(),
                })
    
def buscainterfaces(db, idtxtabuscar): 
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ROW_NUMBER() OVER (ORDER BY resultado.ip) AS correlativo, resultado.* FROM ( SELECT * FROM "+ 
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

def obtpais(db,ip):
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT pais FROM "+db+".equipos where ip like '%"+ip+"';")
    pais = mycursor.fetchall()
    pais = pais[0][0].lower()
    mydb.close()
    return pais

  

    


