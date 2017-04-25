from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # vistas genericas
from django.core.urlresolvers import reverse_lazy
from Apis.canino.models import Perro
from Apis.canino.forms import PerroForm

# Create your views here.
def index(request):
    return render(request, 'base/base.html')

def exito(request):
    return render(request, 'canino/success.html')

class PerroList(ListView):
    model = Perro
    paginate_by = 2
    template_name = 'canino/canino_listar.html'


class PerroCreate(CreateView):
    model = Perro
    form_class = PerroForm
    template_name = 'canino/canino_agregar.html'
    success_url = reverse_lazy('canino:exito')


class PerroUpdate(UpdateView):
    model = Perro
    form_class = PerroForm
    template_name = 'canino/canino_agregar.html'
    success_url = reverse_lazy('canino:exito')


class PerroDelete(DeleteView):
    model = Perro
    template_name = 'canino/canino_eliminar.html'
    success_url = reverse_lazy('canino:listar_caninos')
