
from django.shortcuts import render
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
def impactoporpe(request):
    return render(request,'paginas/buscaimpactoporpe.html', {'dbs': esquemata()})
