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
    if propertie == 'q_30_a_59' and operation == 'Sum':
        total = dq.filter(q_30_a_59=value).aggregate(t=Sum('pob_total'))
        op = total['t']
        return op

    if propertie == 'q_30_a_59' and operation == 'Count':
        total = dq.filter(q_30_a_59=value).aggregate(t=Count('pob_total'))
        op = total['t']
        return op
    if propertie == 'q_pob60' and operation == 'Sum':
        total = dq.filter(q_pob60=value).aggregate(t=Sum('pob_total'))
        op = total['t']
        return op

    if propertie == 'q_pob60' and operation == 'Count':
        total = dq.filter(q_pob60=value).aggregate(t=Count('pob_total'))
        op = total['t']
        return op




def pobTotal(dq):
    total = dq.aggregate(t=Sum('pob_total'))
    op = total['t']
    return op


def getIndex(clases,dq,variable, lgnd, colores=[]):
    
    clases = clases
    poblacion = []
    porcentaje = []
    manzanas = []
    colores = colores
    values = []
    

    

    for d in dq:
        values.append(getattr(d, lgnd))
    for x in clases:
        try:
            poblacion.append(SumCount(dq, variable, x, 'Sum'))
        except: 
            poblacion.append(0)
    for x in clases:
        try:
            manzanas.append(SumCount(dq, variable, x, 'Count'))
        except: 
            manzanas.append(0)
    for i in poblacion:
        try:
            porcentaje.append(round((i*100/pobTotal(dq)),1))
        except: 
            porcentaje.append(0)
    
    leyenda = list(set(values))
    leyenda.sort()
    # print(leyenda)

    tabla = list(zip(clases, manzanas, poblacion, porcentaje, colores,leyenda))
    

    mapIndex = {
        'tabla': tabla,
        'total_manzanas': sum(manzanas),
        'total_porcentaje': round(sum(porcentaje),0)
    }

    # print(variable, mapIndex['tabla'])
    
    return mapIndex






def index(request):
    dist = model.objects.all()
    data = FS.PublicSerializer(dist)
    return render(request,r'home/index.html',{
        'data': data

    })



def webmap(request):
    vh = 0
    h = 0
    m = 0
    l = 0
    distritos = ['Huanta', 'Ayahuanco', 'Huamanguilla', 'Iguain', 'Luricocha', 'Santillana', 'Sivia', 'Llochegua', 'Canayre', 'Uchuraccay', 'Pucacolpa' , 'Chaca']

    distritos.sort()
    query = request.GET.get('search')
    dq = model.objects.all()
    nombre = ''
    total = pobTotal(dq)
    data = FS.PublicSerializer(dq)
    data_riesgo = getIndex(['Muy Alto', 'Alto', 'Medio', 'Bajo'], dq, 'n_riesgo', 'lgn_r',["#dc3545c2", "#ff6a00c2", "#ffc107c2", "#198754c2", ])
    data_densidad = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_densid','lgn_d',['#fde725c2', '#5dc962c2', '#20908dc2', '#3a528bc2', '#440154c2'])
    data_nbi = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_propnbi','lgn_nbi', ['#ffff24c2', '#f3d31bc2', '#e7a612c2', '#db7909c2', '#9f4f00c2'])
    data_3059 = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_30_a_59', 'lgn_3059',[
        '#1a9641c2', '#abdd00c2', '#ffff00c2', '#fd7a00c2', '#d7191cc2'])
    data_60 = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_pob60', 'lgn_60',[
        '#1a9641c2', '#abdd00c2', '#ffff00c2', '#fd7a00c2', '#d7191cc2'])
    



    if query != None:
        dq = dq.filter(Q(distrito__icontains=query) |
                       Q(nom_ccpp__icontains=query))
        
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
        nbi_q1 = SumCount(dq, "q_propnbi", 'Q1', 'Sum')
        nbi_q2 = SumCount(dq, "q_propnbi", 'Q2', 'Sum')
        nbi_q3 = SumCount(dq, "q_propnbi", 'Q3', 'Sum')
        nbi_q4 = SumCount(dq, "q_propnbi", 'Q4', 'Sum')
        nbi_q5 = SumCount(dq, "q_propnbi", 'Q5', 'Sum')
        d3059_q1 = SumCount(dq, "q_30_a_59", 'Q1', 'Sum')
        d3059_q2 = SumCount(dq, "q_30_a_59", 'Q2', 'Sum')
        d3059_q3 = SumCount(dq, "q_30_a_59", 'Q3', 'Sum')
        d3059_q4 = SumCount(dq, "q_30_a_59", 'Q4', 'Sum')
        d3059_q5 = SumCount(dq, "q_30_a_59", 'Q5', 'Sum')
        d60_q1 = SumCount(dq, "q_pob60", 'Q1', 'Sum')
        d60_q2 = SumCount(dq, "q_pob60", 'Q2', 'Sum')
        d60_q3 = SumCount(dq, "q_pob60", 'Q3', 'Sum')
        d60_q4 = SumCount(dq, "q_pob60", 'Q4', 'Sum')
        d60_q5 = SumCount(dq, "q_pob60", 'Q5', 'Sum')
        nombre = query.capitalize()
        data_riesgo = getIndex(['Muy Alto', 'Alto', 'Medio', 'Bajo'], dq, 'n_riesgo', 'lgn_r',
                                ["#dc3545c2", "#ff6a00c2", "#ffc107c2", "#198754c2", ])
        data_densidad = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_densid', 'lgn_d',['#fde725c2', '#5dc962c2', '#20908dc2', '#3a528bc2', '#440154c2'])
        data_3059 = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_30_a_59', 'lgn_3059',['#1a9641c2', '#abdd00c2', '#ffff00c2', '#fd7a00c2', '#d7191cc2'])
        data_nbi = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_propnbi', 'lgn_nbi',['#ffff24c2', '#f3d31bc2', '#e7a612c2', '#db7909c2', '#9f4f00c2'])
        data_60 = getIndex(['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], dq, 'q_pob60', 'lgn_60',['#1a9641c2', '#abdd00c2', '#ffff00c2', '#fd7a00c2', '#d7191cc2'])

        if len(dq) >= 1:
            return render(request, r'dashboard/geoportal.html', {
                'distritos': distritos,
                'data': data,
                'riesgo': data_riesgo['tabla'],
                'densidad': data_densidad['tabla'],
                'nbi': data_nbi['tabla'],
                'd3059': data_3059['tabla'],
                'total_manzana': data_riesgo['total_manzanas'],
                'total_porcentaje': data_riesgo['total_porcentaje'],
                'd60': data_60['tabla'],
                'vh': vh,
                'h': h,
                'm': m,
                'l': l,
                'densidad_q1': densidad_q1,
                'densidad_q2': densidad_q2,
                'densidad_q3': densidad_q3,
                'densidad_q4': densidad_q4,
                'densidad_q5': densidad_q5,
                'nbi_q1': nbi_q1,
                'nbi_q2': nbi_q2,
                'nbi_q3': nbi_q3,
                'nbi_q4': nbi_q4,
                'nbi_q5': nbi_q5,
                'd3059_q1': d3059_q1,
                'd3059_q2': d3059_q2,
                'd3059_q3': d3059_q3,
                'd3059_q4': d3059_q4,
                'd3059_q5': d3059_q5,
                'd60_q1': d60_q1,
                'd60_q2': d60_q2,
                'd60_q3': d60_q3,
                'd60_q4':  d60_q4,
                'd60_q5': d60_q5,
                'total': total,

                'nombre': nombre
            })

        else:
            return render(request, r'shared/noexiste.html', {

            })
            
       

    vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Sum')
    h = SumCount(dq, "n_riesgo", 'Alto', 'Sum')
    m = SumCount(dq, "n_riesgo", 'Medio','Sum' )
    l = SumCount(dq, "n_riesgo", 'Bajo', 'Sum')
    densidad_q1 = SumCount(dq, "q_densid", 'Q1', 'Sum')
    densidad_q2 = SumCount(dq, "q_densid", 'Q2', 'Sum')
    densidad_q3 = SumCount(dq, "q_densid", 'Q3', 'Sum')
    densidad_q4 = SumCount(dq, "q_densid", 'Q4', 'Sum')
    densidad_q5 = SumCount(dq, "q_densid", 'Q5', 'Sum')
    nbi_q1 = SumCount(dq, "q_propnbi", 'Q1', 'Sum')
    nbi_q2 = SumCount(dq, "q_propnbi", 'Q2', 'Sum')
    nbi_q3 = SumCount(dq, "q_propnbi", 'Q3', 'Sum')
    nbi_q4 = SumCount(dq, "q_propnbi", 'Q4', 'Sum')
    nbi_q5 = SumCount(dq, "q_propnbi", 'Q5', 'Sum')
    d3059_q1 = SumCount(dq, "q_30_a_59", 'Q1', 'Sum')
    d3059_q2 = SumCount(dq, "q_30_a_59", 'Q2', 'Sum')
    d3059_q3 = SumCount(dq, "q_30_a_59", 'Q3', 'Sum')
    d3059_q4 = SumCount(dq, "q_30_a_59", 'Q4', 'Sum')
    d3059_q5 = SumCount(dq, "q_30_a_59", 'Q5', 'Sum')
    d60_q1 = SumCount(dq, "q_pob60", 'Q1', 'Sum')
    d60_q2 = SumCount(dq, "q_pob60", 'Q2', 'Sum')
    d60_q3 = SumCount(dq, "q_pob60", 'Q3', 'Sum')
    d60_q4 = SumCount(dq, "q_pob60", 'Q4', 'Sum')
    d60_q5 = SumCount(dq, "q_pob60", 'Q5', 'Sum')
   
    total = pobTotal(dq)   

    

    if len(dq) >= 1:
        return render(request, r'dashboard/geoportal.html', {
            'distritos': distritos,
            'data': data,
            'riesgo': data_riesgo['tabla'],
            'densidad': data_densidad['tabla'],
            'nbi': data_nbi['tabla'],
            'd3059': data_3059['tabla'],
            'total_manzana': data_riesgo['total_manzanas'],
            'total_porcentaje': data_riesgo['total_porcentaje'],
            'd60': data_60['tabla'],
            'vh': vh,
            'h': h,
            'm': m,
            'l': l,
            'densidad_q1': densidad_q1,
            'densidad_q2': densidad_q2,
            'densidad_q3': densidad_q3,
            'densidad_q4': densidad_q4,
            'densidad_q5': densidad_q5,
            'nbi_q1': nbi_q1,
            'nbi_q2': nbi_q2,
            'nbi_q3': nbi_q3,
            'nbi_q4': nbi_q4,
            'nbi_q5': nbi_q5,
            'd3059_q1': d3059_q1,
            'd3059_q2': d3059_q2,
            'd3059_q3': d3059_q3,
            'd3059_q4': d3059_q4,
            'd3059_q5': d3059_q5,
            'd60_q1': d60_q1,
            'd60_q2': d60_q2,
            'd60_q3': d60_q3,
            'd60_q4':  d60_q4,
            'd60_q5': d60_q5,
            'total': total,

            'nombre': nombre
        })
    
    else:
        return render(request, r'shared/noexiste.html', {

        })


def distIndicadores(request):
    nombre = ''
    query = request.GET.get('search')
    # print(type(query))
    dq = model.objects.all()
    if query != None:
        dq = dq.filter(
            Q(distrito=query.upper())
            # Q(nom_ccpp=query.upper())
        )
        # print(len(dq))
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
    # print(total)

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





