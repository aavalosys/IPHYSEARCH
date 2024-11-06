from django.urls import path
from . import descargar, home, busca_ips, busca_impactointerface, busca_impactoporpe, monitoreo_tcn, busca_varios, about, cgnatreport, catalogos, descargar, varias_func, login

urlpatterns = [  #NAME ES EL NOMBRE DE LA URL.... 
    path('login', login.loginmain, name='login'), 
    path('welcome', home.home, name='welcome'),    
    path('buscaips', busca_ips.buscaips, name='buscaips'), 
    path('impactointerfaces', busca_impactointerface.impactointerfaces, name='impactointerfaces'),
    path('buscasaturacion/<str:ip>/<str:no>/<str:dbinter>/<str:pais>/', busca_impactointerface.verimpactointerface, name='buscasaturacion'), 
    path('impactoporpe', busca_impactoporpe.impactoporpe, name='impactoporpe'),
    path('monitoreotcns', monitoreo_tcn.monitoreotcns, name='monitoreotcns'),
    path('buscavarios/<str:selectedoption>/', busca_varios.buscavarios, name='buscavarios'),
    path('catalogos/<str:selectedoption>/', catalogos.catalogos, name='catalogo'), 
    path('actualizarmodales/', catalogos.traelistasselectsmodal, name='actualizarmodales'),
    path('actualizacionactividades/<str:registroactividad>/', catalogos.actualizacionactividades, name='actualizacionactividades'),  
    path('catalogos/actividades/actualizacionact/<str:registroact>/<str:fechaactmodal>/<str:actualizacion>/<str:usuarioact>/<str:estadoact>/<str:vendoract>/', catalogos.actualizaractividad, name='actualizacionact'),
    path('catalogos/casossr/actualizacionsr/<str:registrosr>/<str:fechahoragrabacion>/<str:rma>/<str:ttrma>/<str:fecharmasr>/<str:actualizacion>/<str:usuariosr>/<str:estadosr>/<str:vendorsr>/<str:paissr>/', catalogos.actualizarsrs, name='actualizacionsr'),
    path('agregar_act/', catalogos.agregaractividad, name='agregar_act'), 
    path('agregar_sr/', catalogos.agregarsr, name='agregar_sr'),    
    path('cgnatreport', cgnatreport.cgnat, name='cgnatreport'),
    path('descargarcsv/<str:pais>/', descargar.descargararchivo, name='descargarcsv'), 
    path('about', about.about, name='about'),
    path('pingdesdepevpn/<str:ippe>/<str:ipcpe>/<str:vrf>/', varias_func.pingdesdepevpn, name='pingdesdepevpn'),
    path('detalleinterface/<str:dbcpe>/<str:ipsw>/<str:interface>/', varias_func.detalleinterface, name='detalleinterface'),
    path('buscar_mac/<str:ippe>/<str:ipcpe>/<str:mac>/<str:vlan>/<str:vrf>/<str:pais>/<str:dbcpe>/', busca_ips.buscaserviciomac, name='buscar_mac'), 
    path('buscar_macajax/<str:ippe>/<str:ipcpe>/<str:mac>/<str:vlan>/<str:interface>/<str:vrf>/<str:pais>/<str:dbcpe>/', varias_func.buscaserviciomacajax, name='buscar_macajax'),  
] 
