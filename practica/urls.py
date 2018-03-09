from django.conf.urls import url
from practica import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alumnos/$', views.alumnos, name='alumnos'),
    url(r'^actividades/$', views.actividades, name='actividades'),
    url(r'^informes/$', views.informes_actividades, name='informes'),
    url(r'^informesuspensas/$', views.informe_suspensas, name='informesuspensas'),
    url(r'^contacto/$', views.contacto, name='contacto'),
]
