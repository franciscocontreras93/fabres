from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url('rest/fabres$', views.re_distritos, name='api'), # * EN DESARROLLO
    url('rest/query$', views.re_query, name='api'),
    url(r'rest/fabres/?distrito=(?P<distrito>[a-zA-z]+)$', views.re_distritos, name='distrito'),
    url(r'rest/fabres/?poblado=(?P<nom_ccpp>[a-zA-z\s]+)$', views.re_ccpp, name='centro poblado'),
    url(r'rest/fabres/?idmanzana=(?P<idmanzana>[a-zA-z0-9]+)$', views.re_manzana, name='manzana'),
    
]