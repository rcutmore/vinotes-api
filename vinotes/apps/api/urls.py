from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^notes/$', views.NoteList.as_view()),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.NoteDetail.as_view()),
    url(r'^traits/$', views.TraitList.as_view()),
    url(r'^traits/(?P<pk>[0-9]+)/$', views.TraitDetail.as_view()),
    url(r'^wines/$', views.WineList.as_view()),
    url(r'^wines/(?P<pk>[0-9]+)/$', views.WineDetail.as_view()),
    url(r'^wineries/$', views.WineryList.as_view()),
    url(r'^wineries/(?P<pk>[0-9]+)/$', views.WineryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)