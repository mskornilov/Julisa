# Generated by Django 2.1.4 on 2018-12-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20181220_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, max_length=500, upload_to='files/')),
            ],
        ),
    ]