from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm  
from users.forms import CustomUserCreationForm

def index(request):
    return redirect("/users/login")

def password_change_done(request):
    return redirect("/users/login")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("store:index"))
        return render(
            request, "users/register.html",
            {
                "form": CustomUserCreationForm,
                "messages": form.error_messages
            }
        )
