# -*- coding: utf-8 -*-

from django.conf.urls import url
from Apis.usuario.views import Registro
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registro/$', login_required(Registro.as_view()), name='registrar'),
]
