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
    if propertie == 'q_densidad' and operation == 'Sum':
        total = dq.filter(q_densidad=value).aggregate(t=Sum('pob_total'))
        op = total['t']
        return op

    if propertie == 'q_densidad' and operation == 'Count':
        total = dq.filter(q_densidad=value).aggregate(t=Count('pob_total'))
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








def index(request):
    dist = model.objects.all()
    data = FS.PublicSerializer(dist)
    return render(request,r'home/index.html',{
        'data': data

    })

@login_required
def webmap(request):
    query = request.GET.get('search')
    dq = model.objects.all()
    nombre = ''
    class_riesgo = ['Muy Alto', 'Alto', 'Medio', 'Bajo']
    colores = ["#dc3545c2", "#ff6a00c2", "#ffc107c2",
               "#198754c2"]
    pob_riesgo = []
    qm_riesgo = []
    percent_pob = []
    total = pobTotal(dq)
    data = FS.PublicSerializer(dq) 
    if query != None:
        dq = dq.filter(
            Q(distrito__icontains=query) | Q(nom_ccpp__icontains=query))
        data = FS.PublicSerializer(dq)
        total = pobTotal(dq)
        for x in class_riesgo: 
            pob_riesgo.append(SumCount(dq,'n_riesgo',x,'Sum'))
        for x in class_riesgo: 
            qm_riesgo.append(SumCount(dq,'n_riesgo',x,'Count'))
        for i in pob_riesgo: 
            percent_pob.append(round((i*100/total),1))
                
        vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Sum')
        h = SumCount(dq, "n_riesgo", 'Alto', 'Sum')
        m = SumCount(dq, "n_riesgo", 'Medio', 'Sum')
        l = SumCount(dq, "n_riesgo", 'Bajo', 'Sum')
        
        p_vh = round((vh*100/total),1)
        p_h = round((h*100/total),1)
        p_m = round((m*100/total),1)
        p_l = round((l*100/total),1)
        
        q_vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Count')
        q_h = SumCount(dq, "n_riesgo", 'Alto', 'Count')
        q_m = SumCount(dq, "n_riesgo", 'Medio', 'Count')
        q_l = SumCount(dq, "n_riesgo", 'Bajo', 'Count')

        nombre = query.capitalize()
        for x in class_riesgo:
            pob_riesgo.append(SumCount(dq, 'n_riesgo', x, 'Sum'))
        for x in class_riesgo:
            qm_riesgo.append(SumCount(dq, 'n_riesgo', x, 'Count'))
        for i in pob_riesgo:
            percent_pob.append(round((i*100/total), 1))

        table = list(zip(class_riesgo, qm_riesgo, pob_riesgo, percent_pob,colores))
    
    vh = SumCount(dq, "n_riesgo", 'Muy Alto', 'Sum')
    h = SumCount(dq, "n_riesgo", 'Alto', 'Sum')
    m = SumCount(dq, "n_riesgo", 'Medio','Sum' )
    l = SumCount(dq, "n_riesgo", 'Bajo', 'Sum')

    total = pobTotal(dq)

    for x in class_riesgo:
        pob_riesgo.append(SumCount(dq, 'n_riesgo', x, 'Sum'))
    for x in class_riesgo:
        qm_riesgo.append(SumCount(dq, 'n_riesgo', x, 'Count'))
    for i in pob_riesgo:
        percent_pob.append(round((i*100/total), 1))

    table = list(zip(class_riesgo,qm_riesgo,pob_riesgo,percent_pob,colores))
    print(table)

    if len(dq) >= 1:
        return render(request, r'dashboard/geoportal.html', {
            'data': data,
            'info':table,
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
            
            ''
            'nombre': nombre
        })
    
    else:
        return render(request, r'shared/noexiste.html', {

        })





