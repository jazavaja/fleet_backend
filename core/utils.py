from django.core.exceptions import PermissionDenied

def require_permission(perm_code):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.has_perm(perm_code):
                raise PermissionDenied(f"دسترسی {perm_code} را ندارید.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator