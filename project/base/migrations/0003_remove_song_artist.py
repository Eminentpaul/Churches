# Generated by Django 4.2.5 on 2023-09-10 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_album_artist_user_description_user_image_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
    ]