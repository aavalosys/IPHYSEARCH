from django.shortcuts import render
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *


def buscaips(request):

    if 'buscar_rbs' in request.GET:
        return buscarbs(request)
    elif 'buscar_ip' in request.GET:
        return buscacaipcpe(request)
    return render(request, "paginas/buscaips.html", {'dbs': esquemata(), 'infor': INFOR})


def buscacaipcpe(request):
    dbrbs = request.GET.get('dbrbs')
    textcpe = request.GET.get('ipcpe')
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    paracpd = ('%' + textcpe,)
    quecpetxt = QUECPETXT
    mycursor.execute(quecpetxt.format(dbrbs, dbrbs, dbrbs, dbrbs, dbrbs), paracpd)
    listaips = mycursor.fetchall()
    return render(request, "paginas/buscaips.html", {'listaips': listaips, 'dbs': esquemata(), 'infor': INFOR})


def buscarbs(request):
    dbrbs = request.GET.get('dbrbs')
    textrbs = request.GET.get('idrbs')
    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    pararbs = ('%' + textrbs + '%',)
    querbstxt = QUERBSTXT
    mycursor.execute(querbstxt.format(dbrbs), pararbs)
    listarbs = mycursor.fetchall()
    return render(request, "paginas/buscaips.html", {'listarbs': listarbs, 'dbs': esquemata(), 'infor': "entro a rbs"})
    

def buscaserviciomac (ip):
    print("hola mundo >> " + ip)

