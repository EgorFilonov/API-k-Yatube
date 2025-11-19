from rest_framework import viewsets
from posts.models import Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer, GroupSerializer
from .serializers import FollowSerializer
from rest_framework.pagination import LimitOffsetPagination
from .permissions import PostCommentPermission
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin


class PostViewSet(viewsets.ModelViewSet):
    """вьюсет для постов"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        else:
            return [PostCommentPermission()]


class CommentViewSet(viewsets.ModelViewSet):
    """вьюсет для комментариев"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [PostCommentPermission]


class CommentNestedViewSet(viewsets.ModelViewSet):
    """вьюсет для обработки"""
    serializer_class = CommentSerializer
    permission_classes = [PostCommentPermission]

    def get_queryset(self):
        """Возвращает комментарии для поста с id=post_id."""
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        """Создаёт комментарий для указанного поста."""
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        else:
            return [PostCommentPermission()]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """используется для отображения."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class FollowViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    """"исопльзуется"""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter,]
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
