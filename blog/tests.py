from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Post
from django.test import Client


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.man = User.objects.create_user(username = 'man', password = 'password')
        time = timezone.now()
        texts = "TEST"
        author_test = User.objects.create()
        self.post = Post.objects.create(text=texts,created_date=time,published_date=time,title=texts,author=author_test)

        self.client = Client()
        assert self.client.login(username='man', password='password')

        self.badman = Client()

    def test_clients(self):
        response = self.client.get(reverse('post_detail', kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)

    def test_badclients(self):
        response = self.badman.get(reverse('post_edit', kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 302)
