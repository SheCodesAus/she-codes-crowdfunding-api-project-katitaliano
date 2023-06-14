from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow read actions for any user

        if request.user.is_superuser:
            return True  # Allow write actions for superuser

        return obj.owner == request.user  # Only allow owner to perform write actions
