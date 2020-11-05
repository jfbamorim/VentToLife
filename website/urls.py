from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('login', views.loginv2, name='login'),
    url('technical', views.technical, name='technical'),
    url('hospital', views.hospital, name='hospital'),
    url('forum', views.forum, name='forum'),
    url(r'^/saojoao/', views.saojoao, name='saojoao'),
    url(r'^/currycabral/', views.currycabral, name='currycabral'),
    url(r'^/hpcoimbra/', views.hpcoimbra, name='hpcoimbra'),
    url(r'^/ulsguarda/', views.ulsguarda, name='ulsguarda'),
    url(r'^/hospbraga/', views.hospbraga, name='hospbraga'),
    url('sair', views.sair, name='sair'),
    url('pedido', views.pedido, name='pedido'),
    url(r'^(?P<pedido_id>[0-9]+)/$', views.changerequest, name='changerequest'),
]
