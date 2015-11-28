"""
Contains custom permissions for API app.
"""
from rest_framework import permissions


class IsAuthenticatedOrRegistering(permissions.BasePermission):
    """Allow access for authenticated users or those registering."""

    def has_permission(self, request, view):
        return request.user.is_authenticated() or request.method == 'POST'
