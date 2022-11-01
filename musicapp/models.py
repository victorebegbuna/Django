from django.db import models
from datetime import datetime

# Create your models here.

class Artise(models.Model):
    first_name = models.CharField(_max_lenght=40)
    last_name = models.CharField(_max_lenght=40)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title = models.CharField
    date_released = models.IntegerField
    likes = models.CharField
    artise_id = models.IntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.CharField
    song_id = models.IntegerField()


