from django.conf.urls import url

from ProjekatTim6 import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ucitavanje/plugin/(.*?)', views.ucitavanje_plugin, name="ucitavanje_plugin"),
    url(r'^ucitavanje/plugin_param/(?P<id>([a-z]+|[_])+)$', views.ucitavanje_plugin_broj_param, name="ucitavanje_plugin_broj_param"),
    #url(r'^primer1$', views.complex_graph_prikaz, name="index"),
    url(r'^prikazati/plugin/(?P<id>([a-z]+|[_])+)$', views.prikazi_plugin, name="prikazi_plugin"),
    url(r'^primer1$', views.primer1, name="primer1"),
    url(r'^primer2$', views.primer2, name="primer2"),
]