from django.http import HttpResponse
from ejemplo4.models import Usuario

def index(request):
    usuarios = Usuario.objects.all()
    respuesta = "Usuarios <br/>"
    respuesta += '<br/>'.join(["nombre: %s, edad: %s"%(u.nombre, u.edad) for u in usuarios])
    return HttpResponse(respuesta)
