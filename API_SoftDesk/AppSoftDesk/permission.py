from rest_framework import permissions

from .models import Contributors


class ProjectPermission(permissions.BasePermission):
    """"""

    def has_permission(self, request, view):
        return True

