# Generated by Django 2.1.4 on 2018-12-20 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20181220_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='courses.Module'),
        ),
    ]
