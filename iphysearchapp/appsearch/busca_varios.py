from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *

def buscadorvarios(request):
    return render(request,'paginas/busca_varios.html')
