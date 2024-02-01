from django.shortcuts import render
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

def verimpactointerface(request, ip, interface):
    cache_key = f'interfaces_{ip}'
    cached_data = cache.get(cache_key)
    listadointerfaces = cached_data.get('listadointerfaces', [])
    db = cached_data.get('db', '')
    db = 'fy2024w02'
    print(db)
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ( SELECT * FROM "+ 
                     db + ".mac_address_gt UNION  SELECT * FROM "+
                     db + ".mac_address_sv UNION  SELECT * FROM "+
                     db + ".mac_address_hn UNION  SELECT * FROM "+
                     db + ".mac_address_ni UNION  SELECT * FROM "+
                     db + ".mac_address_cr UNION  SELECT * FROM "+ 
                     db + ".mac_address_xt) AS resultado WHERE resultado.ip LIKE '"+
                     ip + "'")
    tablamac = mycursor.fetchall()

    print(tablamac)
    conteovlans = tablamac
    pais = ''
    return render(request,'paginas/buscaimpactointerface.html',
                {   'db':db,  
                    'ip':ip,
                    'ip':pais,
                    'ip':interface, 
                    'listadointerfaces':listadointerfaces,
                    'conteovlans':conteovlans,   
                    'dbs': esquemata(),
                })
    
def buscainterfaces(db, idtxtabuscar): 
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ( SELECT * FROM "+ 
                     db + ".int_gt UNION  SELECT * FROM "+ 
                     db + ".int_sv UNION  SELECT * FROM "+ 
                     db + ".int_hn UNION  SELECT * FROM "+ 
                     db + ".int_ni UNION  SELECT * FROM "+ 
                     db + ".int_cr UNION  SELECT * FROM "+
                     db + ".int_xt ) AS resultado WHERE resultado.ip LIKE '"+
                     idtxtabuscar + "' and description not like '%LIBRE%' and interface not like '%NULL%'") 
    resultadointerfaces = mycursor.fetchall()
    print (resultadointerfaces)
    mydb.close()
    return resultadointerfaces

  

    


