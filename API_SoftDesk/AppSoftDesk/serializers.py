from rest_framework import serializers
from models import Comments, Contributors, Projects, Issues


class CommentsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Comments


class ContributorsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Contributors


class ProjectsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Projects


class IssuesSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Issues
