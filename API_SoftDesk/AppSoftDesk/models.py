from django.db import models
from django.conf import settings


# Create your models here.


class Users(models.Model):
    pass


class Contributors(models.Model):
    """"""
    user_id = models.IntegerField()
    projet_id = models.IntegerField()
    permission = models.CharField(max_length=150)
    role = models.CharField(max_length=150)


class Projects(models.Model):
    """"""
    project_id = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    author_user_id = models.CharField(max_length=150)
    assignee_user_id = models.CharField(max_length=150)
    created_time = models.DateTimeField()


class Issues(models.Model):
    """"""
    tile = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    tag = models.CharField(max_length=150)
    priority = models.CharField(max_length=150)
    projetct_id = models.CharField(max_length=150) # a modif
    status = models.CharField(max_length=150)


class Comments(models.Model):
    """"""
    comment_id = models.IntegerField()
    description = models.CharField(max_length=150)
    author_user_id = models.CharField(max_length=150)
    issue_id = models.CharField(max_length=150) # a modif ForeignKey
    created_time = models.DateTimeField()
