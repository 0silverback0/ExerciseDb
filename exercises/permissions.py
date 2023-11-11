from rest_framework import permissions

class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow superusers full access, and read-only access for others
        if request.user and request.user.is_superuser:
            print('***superuser***')
            return True
        return request.method in permissions.SAFE_METHODS