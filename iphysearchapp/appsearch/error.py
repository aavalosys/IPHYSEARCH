import logging
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout  
from django.http import HttpResponse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def errorpage(request):
    errores = []
    errordes =""    
    respuesta = ""
    return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores, })