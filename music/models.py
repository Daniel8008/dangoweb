from django.db import models

class Albums(models.Model):
    artist=models.CharField(max_length=270)
    year=models.CharField(max_length=255)
    logo=models.ImageField(null=True,blank=True)
    genre=models.CharField(max_length=290)
    name=models.CharField(max_length=200, default='')

    def __str__(self):
        return  self.artist


class songs(models.Model):
    song_name=models.CharField(max_length=200)
    album=models.ForeignKey(Albums, on_delete=models.CASCADE)
    file_type=models.CharField(max_length=20)

    def __str__(self):
        return  self.song_name


