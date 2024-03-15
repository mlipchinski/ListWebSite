"""
This module contains the views for the ListApp application.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def user_profile(request):
    """
    This view returns the user_profile page.
    """
    return render(request, "user_profile.html")


def user_list(request):
    """
    This view returns the user_list page.
    """
    return render(request, "user_list.html")


def logout_view(request):
    """
    This view logs out the user and redirects them to the home page.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


@login_required
def home(request):
    """
    This view returns the home page. It requires the user to be logged in.
    """
    return render(request, "home.html")


def login_view(request):
    """
    This view returns the home page. It requires the user to be logged in.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request, "login.html", {"error": "Invalid username or password"}
            )
    return render(request, "login.html")  # This will handle the 'GET' request


def register(request):
    """
    This view returns the home page. It requires the user to be logged in.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            return render(request, "register.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})
