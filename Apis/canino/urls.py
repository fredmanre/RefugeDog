from django.conf.urls import url
from Apis.canino.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(regex=r'^$', view=index, name='index'),
    url(r'^exito/$', login_required(exito), name='exito'),
    url(r'^lista/$', login_required(PerroList.as_view()), name='listar_caninos'),
    url(r'^crear/$', login_required(PerroCreate.as_view()), name='nuevo_canino'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(PerroUpdate.as_view()), name='editar_canino'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(PerroDelete.as_view()), name='eliminar_canino'),
]
