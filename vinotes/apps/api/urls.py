from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^notes/$', views.note_list),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.note_detail),
    url(r'^wines/$', views.wine_list),
    url(r'^wines/(?P<pk>[0-9]+)/$', views.wine_detail),
    url(r'^wineries/$', views.winery_list),
    url(r'^wineries/(?P<pk>[0-9]+)/$', views.winery_detail),
]