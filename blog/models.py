from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

from PIL import Image

from django.urls import reverse


class Post(models.Model):
    title = models.CharField("Название", max_length=255)
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата", default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    image = models.ImageField("Изображение", default='', upload_to="posts/")

    def __str__(self):
        return self.title  

    def get_absolute_url(self):
        return reverse('single-page', args=[str(self.id)])

    class Meta():
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Комментироваль {} на {}'.format(self.user.username, self.post.title) 

    class Meta:
        ordering = ('created',)
