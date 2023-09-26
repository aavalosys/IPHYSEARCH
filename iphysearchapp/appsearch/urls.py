from django.urls import path
from . import views, busca_ips, busca_impactointerface, busca_impactoporpe, monitoreo_tcn, busca_varios

urlpatterns = [
    path('welcome', views.home, name='welcome'),  
    path('buscaips', busca_ips.buscaips, name='buscaips'),
    path('impactointerfaces', busca_impactointerface.impactointerfaces, name='impactointerfaces'),
    path('impactoporpe', busca_impactoporpe.impactoporpe, name='impactoporpe'),
    path('monitoreotcns', monitoreo_tcn.monitoreotcns, name='monitoreotcns'),
    path('buscadorvarios', busca_varios.buscadorvarios, name='buscadorvarios'),
]