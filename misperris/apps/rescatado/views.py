from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.rescatado.forms import RescatadoForm
from apps.rescatado.models import Rescatado
from django.contrib.auth.decorators import login_required
from django.core import serializers

# Create your views here.


def index(request):
    rescatado = Rescatado.objects.all()
    contexto = {'rescatados':rescatado}
    return render (request, 'rescatado/index.html', contexto)

def somos(request):
    return render (request, 'principal/somos.html')

def servicios(request):
    return render (request, 'principal/servicios.html')

def contactanos(request):
    return render (request, 'principal/contactanos.html')

"""class RescatadoCreate(CreateView):
    model = Rescatado
    form_class = RescatadoForm
    template_name = 'rescatado/rescatado_form.html'
    success_url = reverse_lazy('rescatado:index')"""


#se visualiza el form para crear un nuevo rescatado

def rescatado_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = RescatadoForm(request.POST)
            
            if form.is_valid():
                form.save()
            return redirect('rescatado_listar')
        else:
            form = RescatadoForm()
        return render(request, 'rescatado/rescatado_form.html', {'form':form})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')



def rescatado_list(request):
    rescatado = Rescatado.objects.all()
    contexto = {'rescatados':rescatado}
    return render(request, 'rescatado/rescatado_list.html', contexto)


def rescatado_edit(request, id_rescatado):

    if request.user.is_superuser:
        rescatado = Rescatado.objects.get(id=id_rescatado)
        if request.method == 'GET':
            form = RescatadoForm(instance=rescatado)
        else:
            form = RescatadoForm(request.POST, instance=rescatado)
            if form.is_valid():
                form.save()
            return redirect('rescatado_listar')
        return render(request,'rescatado/rescatado_form.html',{'form':form})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')

def rescatado_delete(request, id_rescatado):
    if request.user.is_superuser:    
        rescatado = Rescatado.objects.get(id=id_rescatado)
        if request.method == 'POST':
            rescatado.delete()
            return redirect('rescatado_listar')
        return render(request,'rescatado/rescatado_delete.html', {'rescatado':rescatado})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')


def getdata(request):
	results=Rescatado.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)