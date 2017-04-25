"""RefugioPerro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm,\
password_reset_complete
from .views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^canino/', include('Apis.canino.urls', namespace="canino")),
    url(r'^adopcion/', include('Apis.adopcion.urls', namespace="adopcion")),
    url(r'^usuario/', include('Apis.usuario.urls', namespace="usuario")),
    url(r'^accounts/login/$', login, {'template_name':'base/login.html'}, name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(regex=r'^$', view=index, name='index'),
# urls para recuperar contraseñas. Esta es para enviar la direccion de correo.
    url(r'^reset/password_reset/$', password_reset, {'template_name':'recuperacion/reset.html',
        'email_template_name':'recuperacion/reset_email.html'}, name='password_reset'),
# urls para recuperar contraseñas. Esta es para confirmar que se envio el correo.
    url(r'^reset/reset_done', password_reset_done, {'template_name':'recuperacion/reset_done.html'},
        name='password_reset_done'),
# urls para recuperar contraseñas. Esta permite el cambio de contraseña
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name':'recuperacion/reset_confirm.html'},
        name='password_reset_confirm'),
# urls para recuperar contraseñas. esta confirma el cambio de contraseña
    url(r'^reset/done', password_reset_complete, {'template_name':'recuperacion/reset_complete.html'},
        name='password_reset_complete')
]
