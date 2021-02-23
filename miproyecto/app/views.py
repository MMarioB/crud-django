from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Estudiante

# Create your views here.

class EstudianteLista(ListView):
    model = Estudiante

class EstudianteDetalle(DetailView):
    model = Estudiante

class EstudianteCrear(CreateView):
    model = Estudiante
    fields = ['nombre', 'identificador', 'direccion', 'departamento']
    success_url = reverse_lazy('estudiante_list')

class EstudianteModificar(UpdateView):
    model = Estudiante
    fields = ['nombre', 'identificador', 'direccion', 'departamento']
    success_url = reverse_lazy('estudiante_list')

class EstudianteBorrar(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
