"""
This module contains the views for the ListApp application.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache


class RegisterForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        """
        Meta class for the RegisterForm. Specifies the model to be used and
        the fields to be included in the form.
        """

        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


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
    messages.success(request, "You have been logged out.", extra_tags="info")
    return redirect("home")


@login_required
@never_cache
def home(request):
    """
    This view returns the home page. It requires the user to be logged in.
    """
    return render(request, "home.html")


def login_view(request):
    """
    This view returns the home page. It requires the user to be logged in.
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(
                request, "Invalid username or password.", extra_tags="danger"
            )
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def register(request):
    """
    This view handles the registration process.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
