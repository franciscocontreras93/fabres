from django.urls import path
from django.conf.urls import url, re_path

from visor import views,apiviews


urlpatterns = [
    path('', views.index, name='index'),
    re_path('rest/fabres$', apiviews.re_distritos, name='api'), 
    re_path(r'rest/query/?(?P<width>[0-9]+)$', apiviews.re_query, name='api'),
    re_path(r'rest/fabres/(?P<distrito>[a-zA-z]+)$', apiviews.re_distritos, name='distrito'),
    re_path(r'rest/fabres/(?P<nom_ccpp>[a-zA-z\s]+)$', apiviews.re_ccpp, name='centro poblado'),
    re_path(r'rest/fabres/(?P<idmanzana>[a-zA-z0-9]+)$', apiviews.re_manzana, name='manzana'),
]
