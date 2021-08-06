from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from .views import ProjectsViewSet, UserViewSet, CommentsViewSet, ContributorsViewSet, IssuesViewSet

router = routers.DefaultRouter()
router.register(r'signup', UserViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'contributors', ContributorsViewSet)
router.register(r'issues', IssuesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
