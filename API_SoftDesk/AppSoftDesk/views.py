from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .serializers import ProjectsSerializer, CommentsSerializer, ContributorsSerializer, IssuesSerializer
from .models import Projects, Comments, Contributors, Issues


class ProjectsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


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

