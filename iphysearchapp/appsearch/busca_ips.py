from django.shortcuts import render
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.var_functions import *
from .models import *

def buscaips(request):
    textrbs = request.GET.get('idrbs')
    textcpe = request.GET.get('ipcpe')

    dbrbs = request.GET.get('dbrbs')
    dbcpe = request.GET.get('dbcpe')

    pivrbs = request.GET.get('pivrbsrbs')
    pivcpe = request.GET.get('pivcpe')

    mydb =  conexion_dbnet(dbrbs)
    mycursor = mydb.cursor()
    infor = INFOR
                  
    if textrbs and not textcpe:
        print (textrbs)
        pararbs = ('%' + textrbs + '%',)
        querbstxt = QUERBSTXT
        mycursor.execute(querbstxt.format(dbrbs), pararbs)
        listarbs = mycursor.fetchall()
        return render(request, "paginas/buscaips.html", {'qrbss':listarbs, 'dbs': esquemata(), 'infor': infor})
    elif textcpe and not textrbs:
        print (textcpe) 
        paracpd = ('%' + textcpe + '%',)
        quecpetxt = "SELECT * FROM (SELECT * FROM  {}.arp_gt UNION SELECT * FROM  {}.arp_sv UNION  SELECT * FROM  {}.arp_hn UNION SELECT * FROM  {}.arp_ni UNION  SELECT * FROM  {}.arp_cr ) as resultado where resultado.ipcpe like %s"
        mycursor.execute(quecpetxt.format(dbrbs), paracpd)
        listaips = mycursor.fetchall()
        return render(request, "paginas/buscaips.html", {'qrbss':listaips, 'dbs': esquemata(), 'infor': infor})
    else:
        return render(request, 'paginas/buscaips.html', {'dbs': esquemata(), 'infor': infor})
    
    

