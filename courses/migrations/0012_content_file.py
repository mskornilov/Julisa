# Generated by Django 2.1.4 on 2018-12-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_filetest'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='file',
            field=models.FileField(default=1, upload_to='files'),
            preserve_default=False,
        ),
    ]