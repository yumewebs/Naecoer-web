# Generated by Django 3.1.5 on 2021-02-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='studies', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'caso de estudio',
                'verbose_name_plural': 'casos de estudios',
                'ordering': ['-created'],
            },
        ),
    ]
