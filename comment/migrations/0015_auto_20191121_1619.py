# Generated by Django 2.2.6 on 2019-11-21 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0014_auto_20191121_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
