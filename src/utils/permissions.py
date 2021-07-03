from rest_framework import permissions


class CustomBasePermission(permissions.BasePermission):

    def auth(self, request):
        return bool(request.user and request.user.is_authenticated) and bool(
            request.user and request.user.is_staff)


class IsGet(CustomBasePermission):

    def has_permission(self, request, view):
        if hasattr(view, 'get_args'):
            return self.auth(request) and \
                   request.method == "GET" and \
                   request.user.has_perm(view.get_args)
        return request.method == "GET"


class IsPost(CustomBasePermission):

    def has_permission(self, request, view):
        if hasattr(view, 'post_args'):
            return self.auth(request) and \
                   request.method == "POST" and \
                   request.user.has_perm(view.post_args)
        return request.method == "POST"


class IsPut(CustomBasePermission):

    def has_permission(self, request, view):
        if hasattr(view, 'put_args'):
            return self.auth(request) and \
                   request.method == "PUT" and \
                   request.user.has_perm(view.put_args)
        return request.method == "PUT"


class IsPatch(CustomBasePermission):

    def has_permission(self, request, view):
        if hasattr(view, 'patch_args'):
            return self.auth(request) and \
                   request.method == "PATCH" and \
                   request.user.has_perm(view.patch_args)
        return request.method == "PATCH"


class IsDelete(CustomBasePermission):

    def has_permission(self, request, view):
        if hasattr(view, 'delete_args'):
            return self.auth(request) and \
                   request.method == "DELETE" and \
                   request.user.has_perm(view.delete_args)
        return request.method == "DELETE"
