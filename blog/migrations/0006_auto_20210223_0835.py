# Generated by Django 3.1.5 on 2021-02-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210223_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
