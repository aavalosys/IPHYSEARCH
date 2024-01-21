from django.shortcuts import render
from django.db import connection
import requests
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
from django.views.decorators.http import require_GET
import mysql.connector

def cgnat(request):
    
    return render(request, 'paginas/cgnatreport.html',
                   {'dbs': esquemata(),
                    #'datacgnat':intdetail() 
                    })

def intdetail():
    try:
        url = f"http://10.10.26.4:5000/api/cgnat_info/"
        data_to_send = ["GT"]
        response = requests.post(url, json=data_to_send)
        if response.status_code == 200:
            data = response.json()
            datacg = data[1]
        else:
            datacg = 'X'
        return datacg
    except Exception as e:
        datacg = 'X'
        return datacg



