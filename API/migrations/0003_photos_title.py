# Generated by Django 3.1.3 on 2020-12-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20201201_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]