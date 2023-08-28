from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),  
    path('buscaips', views.buscaips, name='buscaips'),
    path('impactointerfaces', views.impactointerfaces, name='impactointerfaces'),
    path('pruebaaci', views.pruebaaci, name='pruebaaci'),
    path('monitoreotcns', views.monitoreotcns, name='monitoreotcns'),
    path('buscadorvarios', views.buscadorvarios, name='buscadorvarios'),
    path('pruebas', views.pruebas, name='pruebas'),
]