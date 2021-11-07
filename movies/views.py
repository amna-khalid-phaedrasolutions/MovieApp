import django.contrib.auth
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Movie, MyUser


@login_required
def allMovies(request):
    movies_list = Movie.objects.order_by('id')[:10]
    context = {
        'movies_list': movies_list,
    }
    return render(request, 'movies/index.html', context)


@login_required
def allUsers(request):
    if request.user.is_authenticated:
        user_list = User.objects.order_by('id')[:10]
        context = {
            'user_list': user_list,
        }
        return render(request, 'movies/user_list.html', context)


@login_required
def showProfile(request):
    user1 = request.user
    context = {
        'user': user1
    }
    return render(request, 'movies/user_profile.html', context)

@login_required
def movie(request, movie_id):
    try:
        movie1 = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    context = {'movie': movie1}

    return render(request, 'movies/movie_page.html', context)


# ------------------------
def filterMovies(request):
    type = request.POST.get('genre')
    movies = Movie.objects.filter(genre=type)
    return render(request, 'movies/index.html', movies)


def signup(request):
    return render(request, 'movies/signup.html')


def login(request):
    return render(request, 'movies/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('movies:login')


def searchMovie(request):
    title = request.POST['input']
    try:
        movies = Movie.objects.get(name__icontains=title)
        context = {'movies': movies}
        return render(request, 'movies/search_movie.html', context)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")


@login_required
def createUser(request):
    if request.user.is_authenticated:
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        password = request.POST.get('password')
        user = User.objects.create(username=username, email=email, firstName=fname, lastName=lname, password=password)
        user.set_password(password)
        user.save()
        return redirect('movies:allUsers')


def checkUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse("movies:index1"))
        else:
            return render(request, "movies/login.html", {
                "message": "Invalid Credentials"
            })


@login_required
def add_movie_page(request):
    return render(request, 'movies/add_movie.html')


def addMovie(request):
    if request.user.is_authenticated:
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


@login_required
def add_user_page(request):
    return render(request, 'movies/add_user.html')


def deleteMovie(request):
    if request.user.is_authenticated:
        id1 = request.POST.get('delete')
        movie1 = Movie.objects.get(id=id1)
        movie1.delete()
        return redirect('movies:index1')


def deleteUser(request):
    if request.user.is_authenticated:
        id1 = request.POST.get('delete')
        user1 = User.objects.get(id=id1)
        user1.delete()
        return redirect('movies:allUsers')


def edit_movie(request):
    if request.user.is_authenticated:
        id1 = request.POST.get('edit')
        movie1 = Movie.objects.get(id=id1)
        context = {
            'movies': movie1
        }
        return render(request, 'movies/edit_movie.html', context)


def edit_user(request):
    if request.user.is_authenticated:
        id1 = request.POST.get('edit')
        user1 = User.objects.get(id=id1)
        context = {
            'user': user1
        }
        return render(request, 'movies/update_profile.html', context)


def updateMovie(request):
    if request.user.is_authenticated:
        id1 = request.POST.get('id')
        movies = Movie.objects.get(id=id1)
        title = request.POST.get('title', None)
        url = request.POST.get('video_url', None)
        s_desc = request.POST.get('short_desc', None)
        l_desc = request.POST.get('long_desc', None)
        type1 = request.POST.get('genre', None)
        movies.thumbnail = movies.thumbnail
        movies.name = title
        movies.video_url = url
        movies.short_desc = s_desc
        movies.long_desc = l_desc
        movies.genre = type1
        movies.save()
        return redirect('movies:index1')


def updateUser(request):
    id1 = request.POST.get('id')
    user = User.objects.get(id=id1)
    name = request.POST.get('username', None)
    email1 = request.POST.get('email', None)
    fname = request.POST.get('first_name', None)
    lname = request.POST.get('last_name', None)
    passcode = request.POST.get('password', None)
    user.username = name
    user.email = email1
    user.password = passcode
    user.firstName = fname
    user.lastName = lname
    user.save()
    return redirect('movies:allUsers')


def RateMovie(request):
    rate = request.POST.get('rating')
    return