from tkinter import CASCADE
from django.db import models


# Create your models here.
class Artise(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    artise_id = models.ForeignKey(Artise, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date_released = models.IntegerField
    likes = models.IntegerField()
    

    def __int__(self):
        return self.title

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    def __int__(self):
        return self.content


