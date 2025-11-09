from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модели для групп"""
    title = models.CharField('название', max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField('описание')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


class Post(models.Model):
    """Модели для потсов."""
    text = models.TextField(null=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self) -> str:
        return self.text


class Follow(models.Model):
    """Модель для сооьществ."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following',)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Comment(models.Model):
    """Модель для комментариев"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'
