from rest_framework import permissions


class IsAuthenticatedOrRegistering(permissions.BasePermission):
    """
    Custom permission to allow access to authenticated users or those registering.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated() or request.method == 'POST'