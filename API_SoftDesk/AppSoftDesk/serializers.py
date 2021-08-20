from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comments, Contributors, Projects, Issues


class CommentsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Comments
        fields = "__all__"


class ContributorsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Contributors
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Projects
        fields = "__all__"


class IssuesSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Issues
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

