from django.utils.translation import ugettext, activate
from django.http import HttpResponse

# Create your views here.
def index(request):
    activate('en')
    output = ugettext("welcome")
    return HttpResponse(output)
# En este ejemplo se modificará en el propio código el cambio de
# idioma. Para ello basta con cambiar 'en' por 'es' para cambiar
# de inglés a español. Es importante resaltar que esta práctica
# suele realizarse a través de enlaces o botones en la página Web.
