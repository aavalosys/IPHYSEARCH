from django.shortcuts import render
from django.db import connection
from sistema.databases import DATABASES
from sistema.var_env import *

def buscadorvarios(request):
    return render(request,'paginas/buscadorvarios.html')
