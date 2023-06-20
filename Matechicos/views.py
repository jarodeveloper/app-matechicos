from django.http import HttpResponse
from django.shortcuts import render
from googleapiclient.discovery import build
from django.conf import settings

# HttpRequest : Para Realizar peticiones
# HttpResponse : Para ernviar respuestas usando el protocolo HTTP

# Esta es una primera vista:
def bienvenido(request):
    return HttpResponse("Hola Mundo")

def plantilla(request):
    return render(request, 'core/plantilla.html')