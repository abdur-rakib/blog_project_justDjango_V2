# Generated by Django 2.2.4 on 2019-08-29 10:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test', verbose_name='Content'),
            preserve_default=False,
        ),
    ]