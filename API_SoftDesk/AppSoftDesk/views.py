from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


from .serializers import (ProjectsSerializer,
                          CommentsSerializer,
                          ContributorsSerializer,
                          IssuesSerializer,
                          UserSerializer)
from .models import Projects, Comments, Contributors, Issues
# Create your views here.


class ProjectsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    #permission_classes =


class CommentsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = CommentsSerializer
    #permission_classes =
    def get_queryset(self):
        """"""
        id_issue = get_object_or_404(Issues, pk=self.kwargs['id'])
        return Comments.objects.filter(issue_id=id_issue)


class ContributorsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = ContributorsSerializer
    #permission_classes =
    def get_queryset(self):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return Contributors.objects.filter(projet_id=id_project)


class IssuesViewSet(viewsets.ModelViewSet):
    """"""

    serializer_class = IssuesSerializer
    #permission_classes =

    def get_queryset(self):
        """"""
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return Issues.objects.filter(project_id=id_project)


class UserViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = UserSerializer
    #permission_classes =

    def get_queryset(self):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return User.objects.filter(projects=id_project)




