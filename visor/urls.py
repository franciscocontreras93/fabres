from django.urls import path, include
from django.conf.urls import url, re_path

from visor import views,apiviews


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', include('django.contrib.auth.urls')),
    path("geoportal/",views.webmap, name="webmap"),
    path("geoportal/search/",views.getDistrito, name='filter'),    
    path("geoportal/indicadores",views.distIndicadores, name="indicadores"),
    re_path(r'rest/fabres$', apiviews.re_distritos, name='api'), 
    re_path(r'rest/fabres/(?P<distrito>[a-zA-z]+)$', apiviews.re_distritos, name='distrito'),
    re_path(r'rest/fabres/(?P<nom_ccpp>[a-zA-z\s]+)$', apiviews.re_ccpp, name='centro poblado'),
    re_path(r'rest/fabres/(?P<idmanzana>[a-zA-z0-9]+)$', apiviews.re_manzana, name='manzana'),
    re_path(r'rest/processing/buffer/?(?P<width>[0-9]+)$', apiviews.re_query, name='api'),
]
