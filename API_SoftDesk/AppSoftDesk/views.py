from rest_framework import viewsets
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
    #permission_classes = (IsAuthenticated,)


class CommentsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class ContributorsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer


class IssuesViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer


class UserViewSet(viewsets.ModelViewSet):
    """"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
