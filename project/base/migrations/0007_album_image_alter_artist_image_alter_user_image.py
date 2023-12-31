# Generated by Django 4.2.5 on 2023-09-10 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_musicfavorite_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
