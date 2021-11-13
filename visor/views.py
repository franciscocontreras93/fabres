from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from visor.models import DistritosModel as model
from django.db.models import Sum

from visor.serializer import FabresSerializer as FS

# Create your views here.


def index(request):
    dist = model.objects.all()
    data = FS.PublicSerializer(dist)

    return render(request,r'portal/index.html',{
        'data': data

    })
def webmap(request):

    dist = model.objects.all()
    
    
    data = FS.PublicSerializer(dist)

    return render(request,r'dashboard/geoportal.html',{
        'data': data

    })
def indicadores(request):
    dist = model.objects.all()
    risk_very_high = model.objects.filter(n_riesgo='Muy Alto').aggregate(t=Sum('pob_total'))
    risk_high = model.objects.filter(n_riesgo='Alto').aggregate(t=Sum('pob_total'))
    risk_medium = model.objects.filter(n_riesgo='Medio').aggregate(t=Sum('pob_total'))
    risk_low = model.objects.filter(n_riesgo='Bajo').aggregate(t=Sum('pob_total'))


    
    
    data = FS.PublicSerializer(dist)

    return render(request,r'dashboard/indicadores.html',{
        'data': data,
        'very_high': risk_very_high['t'],
        'high': risk_high['t'],
        'medium': risk_medium['t'],
        'low': risk_low['t'],
        
        

    })


