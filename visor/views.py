import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from visor.models import DistritosModel as model
from visor.serializer import FabresSerializer as FS


from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from django.contrib.gis.geos import GEOSGeometry

# Create your views here.


def index(request):

    return HttpResponse('''<h1>Hello, Sam Sepiol</h1><br>
                            <img src="https://preview.redd.it/4jrd00tfbix71.jpg?width=640&crop=smart&auto=webp&s=43920f074388430896da8e942b82367ed6e3dc12" alt="alternatetext">
    ''')


@api_view(['GET'])
def re_distritos(request,distrito=False):
    # distrito = 'LURICOCHA' # ! UNCOMMENT TO DEBUG
    if not distrito:        
        feat = model.objects.all()
        result = FS.PublicSerializer(feat)
    elif distrito:
        dist = distrito.upper()
        feat = model.objects.filter(distrito=dist)
        result = FS.PublicSerializer(feat)
        
    return HttpResponse(result, content_type='application/json')

@api_view(['GET'])
def re_ccpp(request , nom_ccpp=False):
    try:
        # nom_ccpp = 'CANAYRE' # ! UNCOMMENT TO DEBUG
        if not nom_ccpp:        
            feat = model.objects.all()
            result = '''ERROR: Should pass a Poblational Center's name'''
        elif nom_ccpp:
            nom_ccpp = nom_ccpp.upper()
            feat = model.objects.filter(nom_ccpp=nom_ccpp)
            result = FS.PublicSerializer(feat)
            
        return HttpResponse(result, content_type='application/json')
    except:
        return HttpResponse('Hubo un error Tilin')


@api_view(['GET'])
def re_manzana(request,idmanzana=False):
    # manzana = '05040200100008E' # ! UNCOMMENT TO DEBUG
    if not idmanzana:        
        feat = model.objects.all()
        result = 'ERROR: Should pass an ID'
    elif idmanzana:
        feat = model.objects.filter(idmanzana=idmanzana)
        result = FS.PublicSerializer(feat)
        
    return HttpResponse(result, content_type='application/json')


@api_view(['GET'])
def re_query(request,width):
    def transformWidth(width=width):
        result = width / 100000
        return result
    #TODO GET USER POSITION WITH JAVASCRIPT FRAMEWORK 
    coords = '-74.244024,-12.825474'
    lCoords = coords.split(',')
    long = lCoords[0]
    lat = lCoords[1]
    pnt = GEOSGeometry(f'POINT({long} {lat})')
    buffer = pnt.buffer(transformWidth(100),quadsegs=8)
    feat = model.objects.filter(geom__intersects=buffer)
    result = FS.TestingSerializer(feat)
    return HttpResponse(result, content_type='application/json')



