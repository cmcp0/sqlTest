from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^index$', views.index),
    url(r'^(?P<tabla>\w{1,50})$', views.brw),
    url(r'^(?P<tabla>\w{1,50})/guardar$', views.guardar),
    url(r'^(?P<tabla>\w{1,50})/seleccionar$', views.seleccionar),
    url(r'^(?P<tabla>\w{1,50})/borrar$', views.borrar),
]
