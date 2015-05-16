from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    url(r'^$', 
        views.api_root, 
        name='api-root'),
    url(r'^notes/$', 
        views.NoteList.as_view(), 
        name='note-list'),
    url(r'^notes/(?P<pk>[0-9]+)/$', 
        views.NoteDetail.as_view(), 
        name='note-detail'),
    url(r'^traits/$', 
        views.TraitList.as_view(), 
        name='trait-list'),
    url(r'^traits/(?P<pk>[0-9]+)/$', 
        views.TraitDetail.as_view(), 
        name='trait-detail'),
    url(r'^wines/$', 
        views.WineList.as_view(), 
        name='wine-list'),
    url(r'^wines/(?P<pk>[0-9]+)/$', 
        views.WineDetail.as_view(), 
        name='wine-detail'),
    url(r'^wineries/$', 
        views.WineryList.as_view(), 
        name='winery-list'),
    url(r'^wineries/(?P<pk>[0-9]+)/$', 
        views.WineryDetail.as_view(), 
        name='winery-detail'),
    url(r'^users/$', 
        views.UserList.as_view(), 
        name='emailuser-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', 
        views.UserDetail.as_view(), 
        name='emailuser-detail'),
])