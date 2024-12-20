from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout  
from django.http import HttpResponse

def errorpage(request):
    errores = []
    errordes =""    
    respuesta = ""
    return render(request, 'errorpage.html', {'respuesta': respuesta, 'errordes': errordes, 'errores': errores, })