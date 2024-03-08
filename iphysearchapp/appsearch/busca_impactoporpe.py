from django.shortcuts import render
from mysql.connector import Error
from django.core.cache import cache
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import * 
from .models import *

def impactoporpe(request):
    db = request.GET.get('dbstr')
    ip = request.GET.get('strbuscado')
    conteovlans = []

    if db is not None and ip is not None:
        pais = obtpais(db,ip)
        resultadoarp = buscaarppe(db, ip, pais)
        conteovlans = contar_vlans(resultadoarp)
        cache_key = f'interfaces_{ip}'
        cache.set(cache_key, {'resultadoarp': resultadoarp, 'db': db})
    else:
        db = '-'
        ip = '-'
        pais = '-'
        resultadoarp = []
        conteovlans = []
    return render(request,'paginas/buscaimpactoporpe.html',
                {   'db':db,  
                    'ip':ip,
                    'pais':pais,
                    'conteovlans':conteovlans,
                    'resultadoarp':resultadoarp,  
                    'dbs': esquemata(),
                })

def buscaarppe(db, ip, pais): 
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM "+db+".arp_"+pais+" where ip = '"+ip+"';")
    resultadoarp = mycursor.fetchall()
    mydb.close()
    return resultadoarp

def obtpais(db,ip):
    mydb =  conexion_dbnet(db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT pais FROM "+db+".equipos where ip like '%"+ip+"';")
    pais = mycursor.fetchall()
    pais = pais[0][0].lower()
    mydb.close()
    return pais


def contar_vlans(resultadoarp):
    conteo = []
    for item in resultadoarp:
        valor_columna_3 = item[2]
        encontrado = False
        for elemento in conteo:
            if elemento[0] == valor_columna_3:
                elemento[1] += 1
                encontrado = True
                break
        if not encontrado:
            conteo.append([valor_columna_3, 1, ""])  # Puedes añadir una descripción aquí si lo necesitas
        
    return conteo




