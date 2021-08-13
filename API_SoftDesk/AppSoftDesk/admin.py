from django.contrib import admin
from .models import Comments, Contributors, Projects, Issues

# Register your models here.


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    """"""
    list_display = ('title', 'description', 'type', 'author_user_id')


@admin.register(Issues)
class IssuesAdmin(admin.ModelAdmin):
    """"""
    list_display = ('title', 'description', 'tag', 'priority', 'project_id', 'status', 'author_user_id',
                    'assignee_user_id', 'created_time',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """"""
    list_display = ('description', 'author_user_id', 'issue_id', 'created_time',)


@admin.register(Contributors)
class ContributorsAdmin(admin.ModelAdmin):
    """"""
    list_display = ('user_id', 'projet_id', 'permission', 'role',)

