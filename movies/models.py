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
    def getUsers(cls, request):
        movies_list = Movie.objects.order_by('id')[:]
        context = {
            'movies_list': movies_list,
        }
        return render(request, 'movies/user_list.html', context)

    @staticmethod
    def createUser(request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        password = request.POST.get('password')
        user = MyUser.objects.create(username=username, email=email, firstName=fname, lastName=lname,
                                     password=password)
        user.set_password(password)
        user.save()
        return redirect('movies:allUsers')

    @staticmethod
    def deleteUser(request):
        id1 = request.POST.get('delete')
        user1 = User.objects.get(id=id1)
        user1.delete()
        return redirect('movies:allUsers')


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
    def getMovies(cls, request):
        movies_list = Movie.objects.order_by('id')[:]
        context = {
            'movies_list': movies_list,
        }
        return render(request, 'movies/index.html', context)

    @staticmethod
    def createMovie(request):
        name = request.POST.get('title', None)
        thumbnail = request.FILES.get('thumbnail')
        video_url = request.POST.get('video_url')
        genre = request.POST.get('genre')
        short_desc = request.POST.get('short_desc')
        long_desc = request.POST.get('long_desc')

        movies = Movie.objects.create(name=name, thumbnail=thumbnail, video_url=video_url, genre=genre,
                                      short_desc=short_desc, long_desc=long_desc)
        movies.save()
        return redirect('movies:index1')

    @staticmethod
    def deleteMovie(request):
        id1 = request.POST.get('delete')
        movie1 = Movie.objects.get(id=id1)
        movie1.delete()
        return redirect('movies:index1')


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=False, default=1)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=False, default=1)
    rate = models.IntegerField(default=5)
    created_at = models.DateTimeField(null=True, blank=True)
