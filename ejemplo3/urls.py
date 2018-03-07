from django.conf.urls import url
from ejemplo3 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
