# Generated by Django 2.2.6 on 2019-11-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191106_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
