import logging
from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from appsearch.varias_func import *
import networkx as nx
import json
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@login_required
def about(request): 
    username = request.user.username 
    return render(request, 'paginas/about.html', {
        'dbs': esquemata_general(),
        'user': username,
        })


   



