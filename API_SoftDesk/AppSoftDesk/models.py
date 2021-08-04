from django.db import models
from django.conf import settings


# Create your models here.


class Users(models.Model):
    pass


class Contributors(models.Model):
    """"""
    user_id = models.IntegerField()
    projet_id = models.IntegerField()
    permission = models.CharField()
    role = models.CharField()

    pass


class Projects(models.Model):
    """"""
    project_id = models.CharField()
    title = models.CharField()
    description = models.CharField()
    type = models.CharField()
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_time = models.DateTimeField()
    pass


class Issues(models.Model):
    """"""
    tile = models.CharField()
    description = models.CharField()
    tag = models.CharField()
    priority = models.CharField()
    projetct_id = models.IntegerField()
    status = models.CharField()

    pass


class Comments(models.Model):
    """"""
    comment_id = models.IntegerField()
    description = models.CharField()
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    issue_id = models.ForeignKey()
    created_time = models.DateTimeField()

    pass
