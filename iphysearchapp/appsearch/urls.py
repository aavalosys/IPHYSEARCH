from django.urls import path
from . import views, busca_ips, busca_impactointerface, busca_impactoporpe, monitoreo_tcn, busca_varios

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),  
    path('buscaips', busca_ips.buscaips, name='busca_ips'),
    path('buscaimpactointerface', busca_impactointerface.impactointerfaces, name='busca_impactointerface'),
    path('buscaimpactoporpe', busca_impactoporpe.impactoporpe, name='busca_impactoporpe'),
    path('monitoreotcn', monitoreo_tcn.monitoreotcns, name='monitoreo_tcn'),
    path('buscavarios', busca_varios.buscadorvarios, name='busca_varios'),
]