from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *
from django.views.decorators.http import require_GET
import mysql.connector

def informativo(request):
    return render(request, 'paginas/informativo.html')
   