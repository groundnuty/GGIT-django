from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime

def hello_world(request):
    my_context = {"time": datetime.datetime.now()}
    return render(request, template_name="hello.html", context=my_context)


def index(request):
    return render(request, template_name="index.html")

def subpage(request):
    return render(request, template_name="subpage.html")


from movies.models import Movie

def movie_list(request):
    my_context = {"movies": Movie.objects.all()}
    return render(request, template_name="movie_list.html", context=my_context)


def profile_view(request):
    return render(request, template_name="my_profile.html")


from django.contrib.auth.forms import UserCreationForm

def user_signup(request):
    if request.method == "POST":
        # przetwarzanie danych z formualrza
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        # czysty formularz do wypelnienia
        form = UserCreationForm()

    return render(
        request,
        template_name="registration/signup_form.html",
        context={'form':form}
    )