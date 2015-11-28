"""
Contains main project URLs.
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # All API URLs.
    url(r'^',
        include('apps.api.urls')),

    # All admin URLs.
    url(r'^admin/',
        include(admin.site.urls)),

    # URLs for django-rest-framework authentiction.
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    # URLs for django-rest-framework token authentication.
    url(r'^api-token-auth/',
        'rest_framework.authtoken.views.obtain_auth_token'),
]
