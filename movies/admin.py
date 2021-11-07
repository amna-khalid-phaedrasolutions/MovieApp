from django.contrib import admin

# Register your models here.
from movies.models import MyUser, Movie

admin.site.register(MyUser)
admin.site.register(Movie)