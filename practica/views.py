from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse
from practica.models import Alumno, Actividad, InformeActividad

def index2(request):
    usuarios = Usuario.objects.all()
    respuesta = "Usuarios <br/>"
    respuesta += '<br/>'.join(["nombre: %s, edad: %s"%(u.nombre, u.edad) for u in usuarios])
    return HttpResponse(respuesta)

def index(request):
    return render_to_response('practica/index.html')
