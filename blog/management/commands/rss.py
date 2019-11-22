import feedparser
from dateutil.parser import parse
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import Rss, Post


class Command(BaseCommand):
    help = 'RSS here'

    def handle(self, *args, **options):
        objects = Rss.objects.all()
        for object in objects:
            if object.url:
                NewsFeed = feedparser.parse(object.url)
                for entry in NewsFeed.entries:
                    author_post = entry.author
                    title = entry.title
                    text = entry.summary
                    published_date = parse(entry.published)
                    link = entry.guid
                    if Post.objects.filter(link=link).exists() is False:
                        post = Post.objects.create(
                            author=User.objects.get(username="admin"),
                            author_post=author_post,
                            title=title,
                            text=text,
                            published_date=published_date,
                            link=link,
                            )
                        print (post)
            else:
                pass


