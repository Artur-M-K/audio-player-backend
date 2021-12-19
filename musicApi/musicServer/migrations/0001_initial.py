# Generated by Django 3.2.9 on 2021-12-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=64)),
                ('song_title', models.CharField(max_length=64)),
                ('song_img', models.ImageField(upload_to='media/song_images')),
            ],
        ),
    ]
