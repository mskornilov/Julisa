# Generated by Django 2.1.4 on 2018-12-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail_image',
            field=models.ImageField(blank=True, upload_to='post/thumbnails'),
        ),
    ]
