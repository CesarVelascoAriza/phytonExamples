from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona
# Create your views here.

def webApp(request):
    personas_var_count = Persona.objects.count()
    #listPersonas = Persona.objects.all()
    #listPersonas = Persona.objects.order_by('id','nombre') ascendente
    listPersonas = Persona.objects.order_by('-id')#decendente
    return render(request, 'index.html',{'count':personas_var_count,'personas':listPersonas})
def despedida(req):
    return HttpResponse("")