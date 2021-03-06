from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^principal/$', views.PrincipalView.as_view(), name='principal'),
    url(r'^principal/resultados/$', views.ResultadosView.as_view(), name='resultados'),
]
