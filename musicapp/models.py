from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artise(models.Model):
    first_name:models.CharField
    last_name:models.CharField
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


