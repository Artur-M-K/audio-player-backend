from django.db import models

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=64)
    song_title = models.CharField(max_length=64)
    song_img = models.ImageField(upload_to='media/song_images')
    song_src = models.FileField(upload_to='media/songs', default='')