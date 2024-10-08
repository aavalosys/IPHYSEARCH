from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from appsearch.varias_func import *
import networkx as nx
import json


def about(request): 
    
    return render(request, 'paginas/about.html', {
        'dbs': esquemata(),
        'user': usuariolog(),
        })


def diagramal2(request):
    G = nx.Graph()
    
    G.add_node("A", tipo="sw1", nombre="Switch - 1")
    G.add_node("B", tipo="sw1", nombre="Switch - 2")
    G.add_node("C", tipo="sw1", nombre="Switch - 3")
    G.add_node("D", tipo="sw1", nombre="Switch - 4")
    G.add_node("E", tipo="sw1", nombre="Switch - 5")

    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("C", "D")
    G.add_edge("D", "E")
    G.add_edge("A", "E")
    
    grafo_json = nx.node_link_data(G)

    for node in grafo_json['nodes']:
        node['image'] = f"/static/img/{node['tipo']}.png"
        node['nombre'] = node['nombre']

    return JsonResponse(grafo_json) #devuelve un grafo en formato json

    

   



