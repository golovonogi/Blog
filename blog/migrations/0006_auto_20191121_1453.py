# Generated by Django 2.2.6 on 2019-11-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rssurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rssurl',
            name='url',
        ),
        migrations.AddField(
            model_name='rssurl',
            name='Ссылка для ленты',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
