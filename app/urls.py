from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='Login'),
    url(r'^index', views.index, name='index'),
]
