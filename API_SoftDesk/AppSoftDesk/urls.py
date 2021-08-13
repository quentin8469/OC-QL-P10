from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (ProjectsViewSet,
                    UserViewSet,
                    CommentsViewSet,
                    ContributorsViewSet,
                    IssuesViewSet,
                    )


"""
router = routers.DefaultRouter()
router.register(r'signup', UserViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'projects/(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments', CommentsViewSet)
router.register(r'contributors', ContributorsViewSet)
router.register(r'projects/(?P<id>[^/.]+)/issues', IssuesViewSet)
"""

router = routers.DefaultRouter()
router.register(r"", ProjectsViewSet, basename="projects")
router.register(r"^(?P<id>[^/.]+)/users", UserViewSet, basename="users")
router.register(r"^(?P<id>[^/.]+)/issues", IssuesViewSet, basename="issues")
router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", CommentsViewSet, basename="comments")
router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/contributors", ContributorsViewSet, basename="contibutors")

urlpatterns = [
    path('projects/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
