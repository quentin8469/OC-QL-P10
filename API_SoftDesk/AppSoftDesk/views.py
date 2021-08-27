from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from rest_framework.response import Response

from .permission import ProjectPermission
from .serializers import (ProjectsSerializer,
                          CommentsSerializer,
                          ContributorsSerializer,
                          IssuesSerializer,
                          UserSerializer, RegisterSerializer)
from .models import Projects, Comments, Contributors, Issues
# Create your views here.


class ProjectsViewSet(viewsets.ModelViewSet):
    """"""
    #queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        contributors = Contributors.objects.filter(user_id=self.request.user)
        info_p = [contributor.projet_id.id for contributor in contributors]
        return Projects.objects.filter(id__in=info_p)


class CommentsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """"""
        id_issue = get_object_or_404(Issues, pk=self.kwargs['id'])
        return Comments.objects.filter(issue_id=id_issue)


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


class UserViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = UserSerializer
    #permission_classes =

    def get_queryset(self):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return User.objects.filter(projects=id_project)


class RegisterUsers(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
            }
        )


