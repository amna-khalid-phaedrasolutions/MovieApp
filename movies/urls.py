from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.shortcuts import redirect
from django.urls import path

from movies import views
from testProject import settings

app_name = 'movies'
urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='loginPage'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('index', views.allMovies, name='index1'),
    path('<int:movie_id>/', views.movie, name='movie_page'),
    path('filteredMovies', views.filterMovies, name='filter_movies'),
    path('search', views.searchMovie, name='search'),
    path('addMovie', views.add_movie_page, name='add_movie_page'),
    path('addingMovie', views.addMovie, name='add_movie'),
    path('deleteMovie', views.deleteMovie, name='deleteMovie'),
    path('editMovie', views.edit_movie, name='edit_movie'),
    path('MovieUpdated', views.updateMovie, name='editMovie'),
    path('Users', views.allUsers, name='allUsers'),
    path('userProfile', views.showProfile, name='profile'),
    path('createUser', views.createUser, name='createUser'),
    path('checkUser', views.checkUser, name='check_user'),
    path('addUser', views.add_user_page, name='add_user_page'),
    path('deleteUser', views.deleteUser, name='deleteUser'),
    path('editUser', views.edit_user, name='edit_user'),
    path('UserUpdated', views.updateUser, name='update_user'),
    path('RateMovie', views.RateMovie, name='rating'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
