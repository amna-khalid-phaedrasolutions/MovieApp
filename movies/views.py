import django.contrib.auth
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Movie, MyUser


class ProfileView(LoginRequiredMixin, TemplateView):
    def post(self, request):
        user1 = request.user
        context = {
            'user': user1
        }
        return render(request, 'movies/user_profile.html', context)


class GetMovieView(LoginRequiredMixin, View):
    def get(self, request, movie_id):
        try:
            movie1 = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise Http404("Movie does not exist")
        context = {'movie': movie1}

        return render(request, 'movies/movie_page.html', context)


class FilterView(TemplateView, LoginRequiredMixin):
    def post(self, request):
        type1 = request.POST.get('genre')
        movies = Movie.objects.filter(genre=type1)
        return render(request, 'movies/index.html', movies)


class SignupView(TemplateView):
    def get(self, request):
        return render(request, 'movies/signup.html')

    def post(self, request):
        MyUser.createUser()


class LoginView(View):
    template_name = 'movies/login.html'

    def get(self, request):
        return render(request, 'movies/login.html')

    def post(self, request):
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


class LogoutView(LoginRequiredMixin, TemplateView):
    def post(self, request):
        logout(request)
        return redirect('movies:login')


class SearchView(TemplateView):
    def post(self, request):
        title = request.POST['input']
        try:
            movies = Movie.objects.get(name__icontains=title)
            context = {'movies': movies}
            return render(request, 'movies/search_movie.html', context)
        except Movie.DoesNotExist:
            raise Http404("Movie does not exist")


class AddMovieView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'movies/add_movie.html')

    def post(self, request):
        Movie.createMovie()


class AddUserView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'movies/add_user.html')

    def post(self, request):
        MyUser.createUser()


class EditMovieView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            id1 = request.POST.get('edit')
            movie1 = Movie.objects.get(id=id1)
            context = {
                'movies': movie1
            }
            return render(request, 'movies/edit_movie.html', context)

    def post(self, request):
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


class EditUserView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            id1 = request.POST.get('edit')
            user1 = User.objects.get(id=id1)
            context = {
                'user': user1
            }
            return render(request, 'movies/update_profile.html', context)

    def post(self, request):
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


class password_reset_request(View):
    def post(self, request):
        if request.method == "POST":
            password_reset_form = PasswordResetForm(request.POST)
            if password_reset_form.is_valid():
                data = password_reset_form.cleaned_data['email']
                associated_users = User.objects.filter(Q(email=data))
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "main/password/password_reset_email.txt"
                        c = {
                            "email": user.email,
                            'domain': '127.0.0.1:8000',
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        try:
                            send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                        except BadHeaderError:
                            return HttpResponse('Invalid header found.')
                        return redirect("/password_reset/done/")
            password_reset_form = PasswordResetForm()
            return render(request=request, template_name="/password/password_reset.html",
                          context={"password_reset_form": password_reset_form})
