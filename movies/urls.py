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
    path('login', views.LoginView.as_view(), name='loginPage'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('index', views.GetMovieView.as_view(), name='index1'),
    path('<int:movie_id>/', views.GetMovie, name='movie_page'),
    path('filteredMovies', views.FilterView.as_view(), name='filter_movies'),
    path('search', views.SearchView.as_view(), name='search'),
    # path('addMovie', views.AddMovieView.as_view(), name='add_movie_page'),
    path('addMovie', views.AddMovieView.as_view(), name='add_movie'),
    path('deleteMovie', views.deleteMovie, name='deleteMovie'),
    path('editMovie', views.EditMovieView.as_view(), name='edit_movie'),
    path('movieUpdated', views.EditMovieView.as_view(), name='edit_movie'),
    path('users', views.GetUser.as_view(), name='allUsers'),
    path('userProfile', views.ProfileView.as_view(), name='profile'),
    path('createUser', views.AddUserView.as_view(), name='createUser'),
    path('checkUser', views.LoginView.as_view(), name='check_user'),
    # path('addUser', views.SignupView.as_view(), name='add_user_page'),
    path('deleteUser', views.deleteUser, name='deleteUser'),
    path('editUser', views.EditUserView.as_view(), name='edit_user'),
    # path('userUpdated', views.EditUserView.as_view(), name='update_user'),
    path('rateMovie', views.RateMovie, name='rating'),
    path('password_reset', views.password_reset_request.as_view(), name="password_reset")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
