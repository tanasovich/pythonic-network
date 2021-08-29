from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, LikeViewSet, UserViewSet, AnalyticsView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', AnalyticsView.as_view())
]
