from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from visor.models import DistritosModel as model
from visor.forms import LoginForm
from django.db.models import Q,Sum,Count
from django.db.models.query import QuerySet

from visor.serializer import FabresSerializer as FS
import os

# Create your views here.


def SumCount(dq, propertie, value, operation=''):

    if propertie == 'n_riesgo' and operation == 'Sum':
        total = dq.filter(n_riesgo=value).aggregate(t=Sum('pob_total'))
        op = total['t']
        return op

    if propertie == 'n_riesgo' and operation == 'Count':
        total = dq.filter(n_riesgo=value).aggregate(t=Count('pob_total'))
        op = total['t']
        return op
    if propertie == 'q_densid' and operation == 'Sum':
        total = dq.filter(q_densid=value).aggregate(t=Sum('pob_total'))
        op = total['t']
        return op

    if propertie == 'q_densid' and operation == 'Count':
        total = dq.filter(q_densid=value).aggregate(t=Count('pob_total'))
        op = total['t']
        return op
    if propertie == 'q_propnbi' and operation == 'Sum':
        total = dq.filter(q_propnbi=value).aggregate(t=Sum('pob_total'))
        op = total['t']
        return op

    if propertie == 'q_propnbi' and operation == 'Count':
        total = dq.filter(q_propnbi=value).aggregate(t=Count('pob_total'))
        op = total['t']
        return op
    if propertie == 'q_propnbi' and operation == 'Sum':
        total = dq.filter(q_propnbi=value).aggregate(t=Sum('pob_total'))
        op = total['t']
        return op

    if propertie == 'q_propnbi' and operation == 'Count':
        total = dq.filter(q_propnbi=value).aggregate(t=Count('pob_total'))
        op = total['t']
        return op




def pobTotal(dq):
    total = dq.aggregate(t=Sum('pob_total'))
    op = total['t']
    return op


def getIndex(clases,dq,variable, colores=[]):
    
    clases = clases
    poblacion = []
    porcentaje = []
    manzanas = []
    colores = colores
    

    

    for x in clases:
        poblacion.append(SumCount(dq, variable, x, 'Sum'))
    for x in clases:
        manzanas.append(SumCount(dq, variable, x, 'Count'))
    for i in poblacion:
        porcentaje.append(round((i*100/pobTotal(dq)), 2))

    tabla = list(zip(clases, manzanas, poblacion, porcentaje, colores))
    

    mapIndex = {
        'tabla': tabla,
        'total_manzanas': sum(manzanas),
        'total_porcentaje': round(sum(porcentaje),0)
    }

    print(variable, mapIndex['tabla'])
    
    return mapIndex






def index(request):
    dist = model.objects.all()
    data = FS.PublicSerializer(dist)
    return render(request,r'home/index.html',{
        'data': data

    })







@login_required
def getDistrito(request): 
    query = request.GET.get('search')
    dq = dq.filter(Q(distrito__icontains=query) | Q(nom_ccpp__icontains=query))

    return render(request, 'dashboard/geoportal.html', {
        'data': dq,
    })




@login_required
def webmap(request):
    query = request.GET.get('search')
    dq = model.objects.all()
    nombre = ''
    total = pobTotal(dq)
    data = FS.PublicSerializer(dq)
    data_riesgo = getIndex(['Muy Alto', 'Alto', 'Medio', 'Bajo'], dq, 'n_riesgo', ["#dc3545c2", "#ff6a00c2", "#ffc107c2", "#198754c2", ])
    data_densidad = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_densid', [
                             '#fde725c2', '#5dc962c2', '#20908dc2', '#3a528bc2', '#440154c2'])



    if query != None:
        dq = dq.filter(
            Q(distrito__icontains=query) | Q(nom_ccpp__icontains=query))
        data = FS.PublicSerializer(dq)
        total = pobTotal(dq)
        vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Sum')
        h = SumCount(dq, "n_riesgo", 'Alto', 'Sum')
        m = SumCount(dq, "n_riesgo", 'Medio', 'Sum')
        l = SumCount(dq, "n_riesgo", 'Bajo', 'Sum')
        densidad_q1 = SumCount(dq, "q_densid", 'Q1', 'Sum')
        densidad_q2 = SumCount(dq, "q_densid", 'Q2', 'Sum')
        densidad_q3 = SumCount(dq, "q_densid", 'Q3', 'Sum')
        densidad_q4 = SumCount(dq, "q_densid", 'Q4', 'Sum')
        densidad_q5 = SumCount(dq, "q_densid", 'Q5', 'Sum')
        nombre = query.capitalize()
        data_riesgo = getIndex(['Muy Alto', 'Alto', 'Medio', 'Bajo'], dq, 'n_riesgo', ["#dc3545c2", "#ff6a00c2", "#ffc107c2", "#198754c2", ])
        data_densidad = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_densid', [
                            '#fde725c2', '#5dc962c2', '#20908dc2', '#3a528bc2', '#440154c2'])

        if len(dq) >= 1:
            return render(request, r'dashboard/geoportal.html', {
                'data': data,
                'riesgo': data_riesgo['tabla'],
                'total_manzana': data_riesgo['total_manzanas'],
                'total_porcentaje': data_riesgo['total_porcentaje'],
                'densidad': data_densidad['tabla'],
                'vh': vh,
                'h': h,
                'm': m,
                'l': l,
                'densidad_q1': densidad_q1,
                'densidad_q2': densidad_q2,
                'densidad_q3': densidad_q3,
                'densidad_q4': densidad_q4,
                'densidad_q5': densidad_q5,

                'total': total,

                'nombre': nombre
            })

        else:
            return render(request, r'shared/noexiste.html', {

            })
        pass


    vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Sum')
    h = SumCount(dq, "n_riesgo", 'Alto', 'Sum')
    m = SumCount(dq, "n_riesgo", 'Medio','Sum' )
    l = SumCount(dq, "n_riesgo", 'Bajo', 'Sum')
   
    total = pobTotal(dq)   

    if len(dq) >= 1:
        return render(request, r'dashboard/geoportal.html', {
            'data': data,
            'riesgo': data_riesgo['tabla'],
            'total_manzana': data_riesgo['total_manzanas'],
            'total_porcentaje': data_riesgo['total_porcentaje'],
            'densidad': data_densidad['tabla'],
            'vh': vh,
            'h': h,
            'm': m,
            'l': l,
            'total': total,

            'nombre': nombre
        })
    
    else:
        return render(request, r'shared/noexiste.html', {

        })

@login_required
def distIndicadores(request):
    nombre = ''
    query = request.GET.get('search')
    print(type(query))
    dq = model.objects.all()
    if query != None:
        dq = dq.filter(
            Q(distrito=query.upper())
            # Q(nom_ccpp=query.upper())
        )
        print(len(dq))
        vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Sum')
        h = SumCount(dq, "n_riesgo", 'Alto', 'Sum')
        m = SumCount(dq, "n_riesgo", 'Medio', 'Sum')
        l = SumCount(dq, "n_riesgo", 'Bajo', 'Sum')
        total = pobTotal(dq)
        nombre = query.capitalize()
        pass
    vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Sum')
    h = SumCount(dq, "n_riesgo", 'Alto', 'Sum')
    m = SumCount(dq, "n_riesgo", 'Medio', 'Sum')
    l = SumCount(dq, "n_riesgo", 'Bajo', 'Sum')
    total = pobTotal(dq)
    print(total)

    if len(dq) >= 1:
        return render(request, r'dashboard/indicadores.html', {
            'vh': vh,
            'h': h,
            'm': m,
            'l': l,
            
            'total': total,
            'nombre': nombre
        })
    
    else:
        return render(request, r'shared/noexiste.html', {

        })





