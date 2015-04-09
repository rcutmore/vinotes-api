from rest_framework import permissions


class IsSameUserOrAdmin(permissions.BasePermission):
    """
    Custom permissions to only allow same user or admins to view user details.
    """
    def has_object_permission(self, request, view, user):
        return request.user == user or request.user.is_staff