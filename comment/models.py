from django.contrib.auth.models import User
from django.db import models

from blog.models import Post


class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    author_comment = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Комментарии"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.comment
