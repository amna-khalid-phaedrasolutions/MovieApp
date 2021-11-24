from datetime import datetime
from time import timezone

from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.shortcuts import redirect, render


class MyUser(User):
    class Meta:
        proxy = True
        ordering = ('first_name',)

    @classmethod
    def getUsers(cls, id1=None):
        user_list = cls.objects.all()
        if id1:
            user_list = user_list.objects.get(id=id1)
        return user_list

    @classmethod
    def createUser(cls, username, email, fname, lname, password):
        user = cls.objects.create(username=username, email=email, firstName=fname, lastName=lname,
                                  password=password)
        user.set_password(password)
        user.save()
        return user

    @classmethod
    def deleteUserQuery(cls, id):
        user1 = User.objects.get(id=id)
        user1.delete()


class Movie(models.Model):
    name = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to="my_folder_name")
    video_url = models.URLField()
    genre = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    long_desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    @classmethod
    def getMovies(cls, id1=None, title=None):
        movies_list = Movie.objects.all()
        if id1:
            movies_list = cls.objects.get(id=id1)
        if title:
            movies_list = cls.objects.get(name__icontains=title)
        return movies_list

    @classmethod
    def createMovie(cls, name, thumbnail, video_url, genre, short_desc, long_desc):
        movies = Movie.objects.create(name=name, thumbnail=thumbnail, video_url=video_url, genre=genre,
                                      short_desc=short_desc, long_desc=long_desc)
        movies.save()

    @staticmethod
    def deleteMovieQuery(id1):
        movie1 = Movie.objects.get(id=id1)
        movie1.delete()


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=False, default=1)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=False, default=1)
    rate = models.IntegerField(default=5)
    created_at = models.DateTimeField(null=True, blank=True)
