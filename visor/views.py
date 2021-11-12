from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from visor.models import DistritosModel as model

from visor.serializer import FabresSerializer as FS

# Create your views here.


def index(request):

    return render(request,r'home/index.html',{

    })
def portal(request):

    dist = model.objects.all()
    # pol = dist.mpoly.geojson
    
    data = FS.PrivateSerializer(dist)

    return render(request,r'portal/index.html',{
        'data': data

    })


