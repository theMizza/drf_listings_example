from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Check owner permission (is user obj owner)"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
