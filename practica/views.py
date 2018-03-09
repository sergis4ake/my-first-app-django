from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

from practica.models import Alumno, Actividad, InformeActividad

def index(request):
    template = loader.get_template('practica/index.html')
    descubre = "¡Descubre!"
    primero = "Bienvenido a mi primera página web con Django"
    segundo = "Desarrollo de Sistemas de Supervisión y Entrenamiento Remoto"
    texto_primero = "El uso de patrones arquitectónicos en el desarrollo de software conlleva numerosas ventajas; los sistemas son más robustos, de mayor calidad, con mayor facilidad de mantenimiento y, por ello, con un desarrollo más rápido. Como contrapartida, el uso de patrones hace que el diseño del software sea más complejo. Por esta razón, requiere abstraer el comportamiento del conjunto de componentes del diseño para que pueda ser utilizado un componente independientemente del resto. En definitiva, en esto consiste la reusabilidad, considerada cada vez más como un aspecto esencial para reducir tiempos de desarrollo y coste del software, lo que conduce a una mayor calidad del mismo."
    texto_segundo = " El objetivo del segundo tema es conocer algunas alternativas de modelado de sistemas web aplicadas al diseño de de sistemas de monitorización y entrenamiento remoto así como algunas de las metodologías y técnicas de desarrollo de aplicaciones web más conocidas. Para ello, se presentarán las características particulares del desarrollo de aplicaciones web y se describirá y aplicará una de las metodologías de desarrollo de aplicaciones web más utilizadas. Finalmente, se expondrán las ventajas del uso de los patrones de diseño en el desarrollo de aplicaciones web así como sus tipos."
    title = "Inicio"
    menu = ['Inicio', 'Alumnos', 'Actividades', 'Informes', 'Informe suspensas', 'Contacto']
    context = {
        'title' : title,
        'texto_primero' : texto_primero,
        'texto_segundo' : texto_segundo,
        'primero' : primero,
        'segundo' : segundo,
        'descubre' : descubre,
        'menu' : menu,

    }
    return HttpResponse(template.render(context, request))

def alumnos(request):
    alumnos = Alumno.objects.all()
    template = loader.get_template('practica/alumnos.html')
    title = "Alumnos"
    menu = ['Inicio', 'Alumnos', 'Actividades', 'Informes', 'Informe suspensas', 'Contacto']
    context = {
        'title' : title,
        'alumnos' : alumnos,
        'menu' : menu,
    }
    return HttpResponse(template.render(context, request))

def actividades(request):
    actividades = Actividad.objects.all()
    template = loader.get_template('practica/actividades.html')
    title = "Actividades"
    menu = ['Inicio', 'Alumnos', 'Actividades', 'Informes', 'Informe suspensas', 'Contacto']
    context = {
        'title' : title,
        'actividades' : actividades,
        'menu' : menu,
    }
    return HttpResponse(template.render(context, request))

def informes_actividades(request):
    informes_actividades = InformeActividad.objects.all()
    template = loader.get_template('practica/informes.html')
    title = "Informes"
    menu = ['Inicio', 'Alumnos', 'Actividades', 'Informes', 'Informe suspensas', 'Contacto']
    context = {
        'title' : title,
        'informes_actividades' : informes_actividades,
        'menu' : menu,
    }
    return HttpResponse(template.render(context, request))

def informe_suspensas(request):
    informes_actividades = InformeActividad.objects.all()
    template = loader.get_template('practica/informesuspensas.html')
    title = "Informe Suspensas"
    menu = ['Inicio', 'Alumnos', 'Actividades', 'Informes', 'Informe suspensas', 'Contacto']
    context = {
        'title' : title,
        'informes_actividades' : informes_actividades,
        'menu' : menu,
    }
    return HttpResponse(template.render(context, request))


def contacto(request):
    formulario = "hola"
    template = loader.get_template('practica/contacto.html')
    title = 'Contacto'
    menu = ['Inicio', 'Alumnos', 'Actividades', 'Informes', 'Informe suspensas', 'Contacto']
    context = {
        'title' : title,
        'formulario' : formulario,
        'menu' : menu,
    }
    return HttpResponse(template.render(context, request))
