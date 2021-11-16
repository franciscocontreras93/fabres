from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from visor.models import DistritosModel as model
from visor.forms import LoginForm
from django.db.models import Q,Sum
from django.db.models.query import QuerySet

from visor.serializer import FabresSerializer as FS

# Create your views here.


def index(request):
    dist = model.objects.all()
    data = FS.PublicSerializer(dist)

    return render(request,r'portal/index.html',{
        'data': data

    })

@login_required
def webmap(request):
    # q = model.objects.all().query().group_by('distrito')
    # q.group_by = ['distrito']
    # data2 = QuerySet(query= q, model= model)
    # print(len(data2))
    # # for d in data2:
    # #     print(d)
    dist = model.objects.all()
    data = FS.PublicSerializer(dist)
    return render(request,r'dashboard/geoportal.html',{
        'data': data

    })


def sumPob(dq, value):
    total = dq.filter(n_riesgo=value).aggregate(t=Sum('pob_total'))
    op = total['t']
    return op
def pobTotal(dq):
    total = dq.aggregate(t=Sum('pob_total'))
    op = total['t']
    return op


@login_required
def distIndicadores(request):
    nombre = ''
    query = request.GET.get('search')
    print(type(query))
    dq = model.objects.all()
    print(len(dq))
    # vh = sumPob(dq, 'Muy Alto')
    # h = sumPob(dq, 'Alto')
    # m = sumPob(dq, 'Medio')
    # l = sumPob(dq, 'Bajo')
    # total = pobTotal(dq)
    # print(total)
    if query != None:
        dq = dq.filter(
            Q(distrito=query.upper())
            # Q(nom_ccpp=query.upper())
        )
        print(len(dq))
        vh = sumPob(dq, 'Muy Alto')
        h = sumPob(dq, 'Alto')
        h = sumPob(dq, 'Medio')
        h = sumPob(dq, 'Bajo')
        total = pobTotal(dq)
        nombre = query.capitalize()
        pass
    vh = sumPob(dq, 'Muy Alto')
    h = sumPob(dq, 'Alto')
    m = sumPob(dq, 'Medio')
    l = sumPob(dq, 'Bajo')
    total = pobTotal(dq)
    print(total)

    if len(dq) >= 1:
        return render(request, r'dashboard/indicadores.html', {
            'very_high': vh,
            'high': h,
            'medium': m,
            'low': l,
            'total': total,
            'nombre': nombre
        })
    
    else:
        return render(request, r'shared/noexiste.html', {

        })





