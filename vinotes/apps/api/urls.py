"""
Contains API app URLs.
"""
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    # API root.
    # Ex: /
    url(r'^$',
        views.api_root,
        name='api-root'),

    # Fetches list of notes.
    # Ex: /notes/
    url(r'^notes/$',
        views.NoteList.as_view(),
        name='note-list'),

    # Fetches details for single note.
    # Ex: /notes/1/
    url(r'^notes/(?P<pk>[0-9]+)/$',
        views.NoteDetail.as_view(),
        name='note-detail'),

    # Fetches list of traits.
    # Ex: /traits/
    url(r'^traits/$',
        views.TraitList.as_view(),
        name='trait-list'),

    # Fetches details for single trait.
    # Ex: /traits/1/
    url(r'^traits/(?P<pk>[0-9]+)/$',
        views.TraitDetail.as_view(),
        name='trait-detail'),

    # Fetches list of wines.
    # Ex: /wines/
    url(r'^wines/$',
        views.WineList.as_view(),
        name='wine-list'),

    # Fetches details for single wine.
    # Ex: /wines/1/
    url(r'^wines/(?P<pk>[0-9]+)/$',
        views.WineDetail.as_view(),
        name='wine-detail'),

    # Fetches list of wineries.
    # Ex: /wineries/
    url(r'^wineries/$',
        views.WineryList.as_view(),
        name='winery-list'),

    # Fetches details for single winery.
    # Ex: /wineries/1/
    url(r'^wineries/(?P<pk>[0-9]+)/$',
        views.WineryDetail.as_view(),
        name='winery-detail'),

    # Fetches list of users.
    # Ex: /users/
    url(r'^users/$',
        views.UserList.as_view(),
        name='emailuser-list'),

    # Fetches details for single user.
    # Ex: /users/1/
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='emailuser-detail'),
])
