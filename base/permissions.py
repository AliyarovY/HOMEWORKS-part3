from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderator').exists()


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsNotModerator(BasePermission):
    def has_permission(self, request, view):
        return not request.user.groups.filter(name='Moderator').exists()
