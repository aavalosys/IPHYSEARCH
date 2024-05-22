from django.db import connection
import requests
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
from django.http import JsonResponse
import json

def elementoespingajax(request, ippe, ipcpe, mac, vlan, vrf, pais, dbcpe):
    res_ping = ''
    try:
        url = f"http://10.10.26.4:5000/api/getpingvrf/"
        data_to_send = [dbcpe, ippe, vrf, ipcpe]
        response = requests.post(url, json=data_to_send)
        print(response.json())
        if response.status_code == 200:             
            resultado = response.json()
            res_ping = resultado[1]
            tipoalerta = '0'
        else:
            res_ping ='PROBLEMA EN LA API. Error:' + str(response.status_code)
            tipoalerta = '1'
    except Exception as e:
            res_ping = 'Excepcion en la API = ' + str(e)
            tipoalerta = '2'
    return JsonResponse({"res_ping": res_ping, "tipoalerta":tipoalerta})


def detalleinterface(request, dbcpe, ipsw, mac, vlan, interface):
    detalleinter = 'X'
    dbcpe = ''
    try:
            url = f"http://10.10.26.4:5000/api/getinterface/"
            data_to_send = [dbcpe, ipsw, interface]
            response = requests.post(url, json=data_to_send)
            if response.status_code == 200:
                datainterface = response.json()
                detalleinter = datainterface[1].split('\n')
                tipoalerta = '0'
    except Exception as e: 
        detalleinter = 'X'
        tipoalerta = '1'
    return JsonResponse({"detalleinter": detalleinter, "tipoalerta":tipoalerta})
