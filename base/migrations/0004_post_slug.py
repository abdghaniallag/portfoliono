# Generated by Django 4.1.5 on 2023-01-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
