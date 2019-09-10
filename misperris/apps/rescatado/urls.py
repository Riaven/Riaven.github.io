from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.rescatado.views import getdata,index, rescatado_view, rescatado_list, rescatado_edit, rescatado_delete, somos, servicios, contactanos

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(rescatado_view), name='rescatado_crear'),
    url(r'^listar$', login_required(rescatado_list), name='rescatado_listar'),
    url(r'^editar/(?P<id_rescatado>\d+)/$', login_required(rescatado_edit), name='rescatado_editar'),
    url(r'^eliminar/(?P<id_rescatado>\d+)/$', login_required(rescatado_delete), name='rescatado_eliminar'),
    url(r'^somos$', somos, name='somos'),
    url(r'^servicios$', servicios, name='servicios'),
    url(r'^contactanos$', contactanos, name='contactanos'),
    url(r'^getdata$', getdata, name='getdata' )
]