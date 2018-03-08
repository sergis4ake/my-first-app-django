from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

from practica.models import Alumno, Actividad, InformeActividad

def index(request):
    template = loader.get_template('practica/index.html')
    title = "Menú Principal"
    context = {
        'title' : title,
    }
    return HttpResponse(template.render(context, request))

def alumnos(request):
    alumnos = Alumno.objects.all()
    template = loader.get_template('practica/alumnos.html')
    title = "Alumnos"
    context = {
        'title' : title,
        'alumnos' : alumnos,
    }
    return HttpResponse(template.render(context, request))

def actividades(request):
    actividades = Actividad.objects.all()
    template = loader.get_template('practica/actividades.html')
    title = "Actividades"
    context = {
        'title' : title,
        'actividades' : actividades,
    }
    return HttpResponse(template.render(context, request))

def informes_actividades(request):
    informes_actividades = InformeActividad.objects.all()
    template = loader.get_template('practica/informes.html')
    title = "Informes"
    context = {
        'title' : title,
        'informes_actividades' : informes_actividades,
    }
    return HttpResponse(template.render(context, request))
