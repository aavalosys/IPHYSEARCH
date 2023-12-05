from django.urls import path
from . import home, busca_ips, busca_impactointerface, busca_impactoporpe, monitoreo_tcn, busca_varios

urlpatterns = [
    path('welcome', home.home, name='welcome'),  
    path('buscaips', busca_ips.buscaips, name='buscaips'),
    path('impactointerfaces', busca_impactointerface.impactointerfaces, name='impactointerfaces'),
    path('impactoporpe', busca_impactoporpe.impactoporpe, name='impactoporpe'),
    path('monitoreotcns', monitoreo_tcn.monitoreotcns, name='monitoreotcns'),
    path('buscadorvarios', busca_varios.buscadorvarios, name='buscadorvarios'),
    path('buscar_mac/<str:ipcpe>/<str:mac>/<str:vlan>/<str:pais>/<str:dbcpe>/', busca_ips.buscaserviciomac, name='buscar_mac'),

]