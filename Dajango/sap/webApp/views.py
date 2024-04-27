from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona
# Create your views here.

def webApp(request):
    personas_var_count = Persona.objects.count()

    return render(request, 'index.html',{'count':personas_var_count})
def despedida(req):
    return HttpResponse("")