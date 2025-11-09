from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class PostCommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """Проверка для безопасных методов. редактирование и удаление
        только автору."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and obj.author == request.user

    def get_permissions(self):
        """Возвращает разрешения в зависимости от действия."""
        if self.action == 'create':
            return [IsAuthenticated]
        return [PostCommentPermission()]
