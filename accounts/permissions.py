from rest_framework import permissions


class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('accounts.view_user')
        elif request.method == 'POST':
            return request.user.has_perm('accounts.add_user')
        elif request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('accounts.change_user')
        elif request.method == 'DELETE':
            return request.user.has_perm('accounts.delete_user')

        return False
