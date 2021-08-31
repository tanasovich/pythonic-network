from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsNewUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            elif request.method == 'POST':
                return True
            else:
                return False
        else:
            return False
