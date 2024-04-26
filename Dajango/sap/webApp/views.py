from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def webApp(request):
    return HttpResponse('Hola mundo desde djago')
def despedida(req):
    return HttpResponse("")