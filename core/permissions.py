# core/permissions.py

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


def PermissionRequired(perm_code: str):
    class _PermissionRequired(BasePermission):
        def has_permission(self, request, view):
            if not request.user.has_perm(perm_code):
                raise PermissionDenied(f"دسترسی {perm_code} را ندارید.")
            return True

    return _PermissionRequired


class ModelPermissionMap(BasePermission):
    """
    Dynamic permission checker based on model name and app_label.
    """

    def get_model_meta(self, view):
        if hasattr(view, 'queryset') and view.queryset is not None:
            model = view.queryset.model
        elif hasattr(view, 'get_queryset'):
            model = view.get_queryset().model
        else:
            raise Exception("ModelPermissionMap: Unable to determine model from ViewSet")
        print("VVIEEW", model._meta.app_label, "---", model._meta.model_name)
        return model._meta.app_label, model._meta.model_name

    def get_required_permission(self, action, app_label, model_name):
        perms = {
            'list': f'{app_label}.view_{model_name}',
            'retrieve': f'{app_label}.view_{model_name}',
            'create': f'{app_label}.add_{model_name}',
            'update': f'{app_label}.change_{model_name}',
            'partial_update': f'{app_label}.change_{model_name}',
            'destroy': f'{app_label}.delete_{model_name}',
        }
        return perms.get(action)

    def has_permission(self, request, view):
        action = getattr(view, 'action', None)
        app_label, model_name = self.get_model_meta(view)
        required_permission = self.get_required_permission(action, app_label, model_name)

        if not required_permission:
            return True  # If no permission mapped, allow access

        if not request.user.has_perm(required_permission):
            raise PermissionDenied(f"شما اجازه دسترسی به '{required_permission}' را ندارید.")
        return True


class GroupPermissionAccess(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            if not request.user.has_perm('auth.view_group'):
                raise PermissionDenied("اجازه مشاهده گروه‌ها را ندارید.")
        elif request.method == 'POST':
            if not request.user.has_perm('auth.change_group'):
                raise PermissionDenied("اجازه ویرایش گروه‌ها را ندارید.")
        return True


class GetProvincePermissionAccess(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            if not request.user.has_perm('auth.view_group'):
                raise PermissionDenied("اجازه مشاهده گروه‌ها را ندارید.")
        elif request.method == 'POST':
            if not request.user.has_perm('auth.change_group'):
                raise PermissionDenied("اجازه ویرایش گروه‌ها را ندارید.")
        return True
