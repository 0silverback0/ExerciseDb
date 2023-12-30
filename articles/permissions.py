# permissions.py
from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow superusers to perform write operations
        return request.user and request.user.is_superuser
