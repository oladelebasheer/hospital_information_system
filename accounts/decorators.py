from django.core.exceptions import PermissionDenied
from functools import wraps


def role_required(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            user_groups = request.user.groups.values_list('name', flat=True)

            if any(group in allowed_roles for group in user_groups):
                return view_func(request, *args, **kwargs)

            raise PermissionDenied
        return wrapper
    return decorator