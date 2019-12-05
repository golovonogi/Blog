# Generated by Django 2.2.6 on 2019-11-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191121_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rssurl',
            options={'verbose_name': 'Ссылка RSS', 'verbose_name_plural': 'Ссылки RSS'},
        ),
        migrations.AlterField(
            model_name='rssurl',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Название ссылки'),
        ),
    ]