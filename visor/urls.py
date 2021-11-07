from django.urls import path
from django.conf.urls import url, re_path

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    re_path('rest/fabres$', views.re_distritos, name='api'), # * EN DESARROLLO
    re_path('rest/query$', views.re_query, name='api'),
    re_path(r'rest/fabres/?distrito=(?P<distrito>[a-zA-z]+)$', views.re_distritos, name='distrito'),
    re_path(r'rest/fabres/?poblado=(?P<nom_ccpp>[a-zA-z\s]+)$', views.re_ccpp, name='centro poblado'),
    re_path(r'rest/fabres/?idmanzana=(?P<idmanzana>[a-zA-z0-9]+)$', views.re_manzana, name='manzana'),
    
]