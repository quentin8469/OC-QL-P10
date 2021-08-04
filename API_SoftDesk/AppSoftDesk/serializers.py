from rest_framework import serializers
from models import Comments, Contributors, Projects, Issues


class CommentsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Comments
        fields = ['id', 'description', 'author',
                  'created_time']


class ContributorsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Contributors
        fields = ['id', 'user', 'project', 'permission', 'role']


class ProjectsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type']


class IssuesSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Issues
        fields = ['id', 'title', 'desc', 'tag', 'priority',
                  'status', 'author', 'assignee', 'created_time']
