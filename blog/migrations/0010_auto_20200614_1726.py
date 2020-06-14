# Generated by Django 3.0.7 on 2020-06-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200614_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topics',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='blog.Category'),
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
