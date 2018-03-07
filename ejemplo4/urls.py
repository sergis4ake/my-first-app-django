from django.conf.urls import url
from ejemplo4 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
