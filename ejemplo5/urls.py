from django.conf.urls import url
from ejemplo5 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
