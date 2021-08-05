from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from .views import ProjectsViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
