from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MyUser(User):
    class Meta:
        proxy = True
        ordering = ('first_name',)


class Rating(models.Model):
    rate = models.IntegerField(default=0)


class Movie(models.Model):
    name = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to="my_folder_name")
    video_url = models.URLField()
    genre = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    long_desc = models.CharField(max_length=1000)
    rate = models.ForeignKey(
        Rating, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


