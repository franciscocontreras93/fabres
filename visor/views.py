from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from visor.models import DistritosModel as model
from visor.serializer import FabresSerializer as FS


from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes

from django.contrib.gis.geos import GEOSGeometry

# Create your views here.


def index(request):

    return render(request,r'home/index.html',{

    })


