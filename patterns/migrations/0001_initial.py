# Generated by Django 3.2.23 on 2023-11-26 22:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('difficulty_level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], max_length=20)),
                ('yarn_type', models.CharField(max_length=50)),
                ('hook_size', models.CharField(max_length=10)),
                ('gauge', models.CharField(max_length=50)),
                ('instructions', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
