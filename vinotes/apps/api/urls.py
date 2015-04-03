from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^notes/$', views.note_list),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.note_detail),
    url(r'^traits/$', views.trait_list),
    url(r'^traits/(?P<pk>[0-9]+)/$', views.trait_detail),
    url(r'^wines/$', views.wine_list),
    url(r'^wines/(?P<pk>[0-9]+)/$', views.wine_detail),
    url(r'^wineries/$', views.winery_list),
    url(r'^wineries/(?P<pk>[0-9]+)/$', views.winery_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)