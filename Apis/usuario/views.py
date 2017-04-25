from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from Apis.usuario.form import RegistroUsuario

# Create your views here.

class Registro(CreateView):
    model = User
    form_class = RegistroUsuario
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('canino:exito')
