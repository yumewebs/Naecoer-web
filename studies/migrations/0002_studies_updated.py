# Generated by Django 3.1.5 on 2021-02-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studies',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]
