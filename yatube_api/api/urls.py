from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CommentViewSet, GroupViewSet, PostViewSet
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', obtain_auth_token),
]
