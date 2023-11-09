from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    message = 'Вы не являетесь администратором или владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        if obj.user == request.user:
            return True
        return False
