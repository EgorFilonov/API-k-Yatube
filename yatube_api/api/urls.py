from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, CommentNestedViewSet, GroupViewSet
from api.views import FollowViewSet
router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet)


urlpatterns = [
    path('v1/', include([
        path('', include(router_v1.urls)),
        path('posts/<int:post_id>/comments/',
             CommentNestedViewSet.as_view({'get': 'list', 'post': 'create'})),
        path('posts/<int:post_id>/comments/<int:pk>/',
             CommentNestedViewSet.as_view({
                 'get': 'retrieve',
                 'put': 'update',
                 'patch': 'partial_update',
                 'delete': 'destroy'
             })),
        path('', include('djoser.urls')),

        path('', include('djoser.urls.jwt')),
    ])),
]
