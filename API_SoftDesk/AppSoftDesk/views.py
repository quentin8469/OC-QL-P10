from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from rest_framework.response import Response

from .permission import ProjectPermission
from .serializers import (ProjectsSerializer,
                          CommentsSerializer,
                          ContributorsSerializer,
                          IssuesSerializer,
                          UserSerializer,
                          RegisterSerializer)
from .models import Projects, Comments, Contributors, Issues
# Create your views here.


class ProjectsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [ProjectPermission & permissions.IsAuthenticated]

    def get_queryset(self):
        """"""
        return Projects.objects.filter(author_user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """"""
        query_issue_id = self.kwargs.get('issue_id')
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        id_issues = Issues.objects.filter(project_id=id_project)
        id_issue = id_issues.get(pk=query_issue_id)
        return Comments.objects.filter(issue_id=id_issue)

    def perform_create(self, serializer):
        query_issue_id = self.kwargs.get('issue_id')
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        id_issues = Issues.objects.filter(project_id=id_project)
        id_issue = id_issues.get(pk=query_issue_id)
        serializer.save(issue_id=id_issue)
        serializer.save(author_user_id=self.request.user)


class ContributorsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = ContributorsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return Contributors.objects.filter(projet_id=id_project)


class IssuesViewSet(viewsets.ModelViewSet):
    """"""

    serializer_class = IssuesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """"""
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return Issues.objects.filter(project_id=id_project)

    def perform_create(self, serializer):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        serializer.save(project_id=id_project)
        serializer.save(author_user_id=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return User.objects.filter(projects=id_project)


class RegisterUsers(generics.GenericAPIView):
    """"""
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
            }
        )
