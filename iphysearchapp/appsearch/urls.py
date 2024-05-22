from django.urls import path
from . import descargar, home, busca_ips, busca_impactointerface, busca_impactoporpe, monitoreo_tcn, busca_varios, about, cgnatreport, catalogos, descargar, resultaequipos
from iphysearchapp.var_functions import pingdesdepevpn

urlpatterns = [  #NAME ES EL NOMBRE DE LA URL
    path('welcome/', home.home, name='welcome'),   
    path('buscaips', busca_ips.buscaips, name='buscaips'), 
    path('impactointerfaces', busca_impactointerface.impactointerfaces, name='impactointerfaces'),
    path('impactoporpe', busca_impactoporpe.impactoporpe, name='impactoporpe'),
    path('monitoreotcns', monitoreo_tcn.monitoreotcns, name='monitoreotcns'),
    path('buscavarios/<str:selectedoption>/', busca_varios.buscavarios, name='buscavarios'),
    path('catalogos/<str:selectedoption>/', catalogos.catalogos, name='catalogo'), 
    path('agregar_act/', catalogos.agregaractividad, name='agregar_act'),
    path('agregar_sr/', catalogos.agregarsr, name='agregar_sr'),
    path('cgnatreport', cgnatreport.cgnat, name='cgnatreport'),
    path('descargarcsv/<str:pais>/', descargar.descargararchivo, name='descargarcsv'),
    path('about', about.about, name='about'),
    path('ping_cpeajax/<str:ippe>/<str:ipcpe>/<str:mac>/<str:vlan>/<str:vrf>/<str:pais>/<str:dbcpe>/', resultaequipos.elementoespingajax, name='ping_cpeajax'),
    path('pingdesdepevpn/<str:ippe>/<str:ipcpe>/<str:mac>/<str:vlan>/<str:vrf>/<str:pais>/<str:dbcpe>/', pingdesdepevpn, name='pingdesdepevpn'),
    path('about/diagramal2/', about.diagramal2, name='diagramal2'),
    path('buscar_mac/<str:ippe>/<str:ipcpe>/<str:mac>/<str:vlan>/<str:vrf>/<str:pais>/<str:dbcpe>/', busca_ips.buscaserviciomac, name='buscar_mac'),
    path('buscasaturacion/<str:ip>/<str:no>/', busca_impactointerface.verimpactointerface, name='buscasaturacion'),
]