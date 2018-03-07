from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('ejemplo5/index.html')
