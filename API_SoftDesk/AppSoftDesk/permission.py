from rest_framework import permissions


class ProjectPermission(permissions.BasePermission):
    """"""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author_user_id
        else:
            return False


class IssuesPermission(permissions.BasePermission):
    """"""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author_user_id
        else:
            return False


class CommentsPermission(permissions.BasePermission):
    """"""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author_user_id
        else:
            return False