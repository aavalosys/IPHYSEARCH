from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

def monitoreotcns(request):
    return render(request,'paginas/monitoreo_tcn.html')
