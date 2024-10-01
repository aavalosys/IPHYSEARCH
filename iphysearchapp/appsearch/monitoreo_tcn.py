from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *


def monitoreotcns(request):
    return render(request,'paginas/monitoreotcn.html')
