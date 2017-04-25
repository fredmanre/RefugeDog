from django.conf.urls import url
from Apis.adopcion.views import SolicitudListView, SolicitudCreateView, SolicitudUpdateView, SolicitudDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^listar/$', login_required(SolicitudListView.as_view()), name='listar'),
    url(r'^crear/$', login_required(SolicitudCreateView.as_view()), name='crear'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(SolicitudUpdateView.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(SolicitudDeleteView.as_view()), name='eliminar'),
]
