from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')

@login_required
def productos(request):
    productos = Libro.objects.all()
    return render(request,'productos/index.html',{'productos': productos})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('productos')
    return render(request,'productos/crear.html', {'formulario':formulario})

def editar(request,id):
    producto=Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request,'productos/editar.html', {'formulario':formulario})

def eliminar(request, id):
    producto=Libro.objects.get(id=id)
    producto.delete()
    return redirect ('productos')

def exit(request):
    logout(request)
    return redirect('inicio')