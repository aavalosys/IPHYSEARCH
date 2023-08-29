from django.shortcuts import render
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

def buscaips(request):
    mycursor = conexion()
    idrbs = request.GET.get('idrbs')
    dbrbs = request.GET.get('dbrbs')
    pivrbs = request.GET.get('pivrbs')
    
    ip = request.GET.get('ip')
    db = request.GET.get('db')
    piv = request.GET.get('piv')

    if idrbs and pivrbs=='0':               
        mycursor.execute('SELECT * FROM '+ dbrbs+'.nodob WHERE nodoid like "%"'+idrbs+'%"')
        qrbss = mycursor.fetchall()
        return render(request, "paginas/buscaips.html", {"qrbss":qrbss, 'dbs': esquemata()})
    elif ip and piv=='1':
        return render(request, "paginas/buscaips.html", {'dbs': esquemata()})
    
    return render(request, 'busca/home.html', {'dbs': esquemata()})
    

