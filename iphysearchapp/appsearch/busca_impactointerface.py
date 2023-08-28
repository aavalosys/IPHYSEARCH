from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *

def impactointerfaces(request):
    return render(request,'paginas/impactointerfaces.html')

