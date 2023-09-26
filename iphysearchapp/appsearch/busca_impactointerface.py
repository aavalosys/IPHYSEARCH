from django.shortcuts import render
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

def impactointerfaces(request):
    return render(request, 'paginas/buscaimpactointerface.html', {'dbs': esquemata()})


