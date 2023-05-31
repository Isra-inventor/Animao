from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import *
# Create your views here.

def index(request):
    return render(request, "animao/index.html")

def about(request):
    return render(request, "animao/about.html")

def contact(request):
    return render(request, "animao/contact.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "animao/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "animao/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "animao/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "animao/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "animao/register.html")

@csrf_exempt
def api_get_courses(request):
    if request.method == "GET":
        courses = Course.objects.all()
        return JsonResponse(serializers.serialize('json', courses), safe=False)