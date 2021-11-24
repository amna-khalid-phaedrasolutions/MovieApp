from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.shortcuts import redirect
from django.urls import path

from movies import views
from MovieApp import settings
from movies.models import MyUser, Movie


app_name = 'movies'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('login', views.LoginView, name='loginPage'),
    path('logout', views.LogoutView, name='logout'),
    path('signup', views.SignupView, name='signup'),
    path('index', Movie.getMovies, name='index1'),
    path('<int:movie_id>/', views.GetMovieView, name='movie_page'),
    path('filteredMovies', views.FilterView, name='filter_movies'),
    path('search', views.SearchView, name='search'),
    path('addMovie', Movie.createMovie, name='add_movie_page'),
    path('addMovie', Movie.createMovie, name='add_movie'),
    path('deleteMovie', Movie.deleteMovie, name='deleteMovie'),
    path('editMovie', views.EditMovieView, name='edit_movie'),
    path('MovieUpdated', views.EditMovieView, name='editMovie'),
    path('Users', MyUser.getUsers, name='allUsers'),
    path('userProfile', views.ProfileView, name='profile'),
    path('CreateUser', MyUser.createUser, name='createUser'),
    path('checkUser', views.LoginView, name='check_user'),
    path('addUser', views.SignupView, name='add_user_page'),
    path('DeleteUser', MyUser.deleteUser, name='deleteUser'),
    path('editUser', views.EditUserView, name='edit_user'),
    path('UserUpdated', views.EditUserView, name='update_user'),
    path('RateMovie', views.RateMovie, name='rating'),
    path("password_reset", views.password_reset_request, name="password_reset")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
