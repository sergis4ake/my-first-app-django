from django.utils.translation import ugettext, activate
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.shortcuts import render

# Create your views here.
#def index(request):
#    activate('en')
#    output = ugettext("welcome")
#    return HttpResponse(output)

def index(request):
    #return render(request, 'ejemplo3/index.html')

    template = loader.get_template('ejemplo3/index.html')
    title = "Hola"
    context = {
        'title' : title,
    }
    return HttpResponse(template.render(context, request))
