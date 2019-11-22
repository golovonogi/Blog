from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_post = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(upload_to='media/blog', blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Rss(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="Название ссылки")
    url = models.CharField(max_length=100, blank=True, verbose_name="Ссылка для ленты")

    class Meta:
        verbose_name = "Ссылка RSS"
        verbose_name_plural = "Ссылки RSS"

    def __str__(self):
        return self.title