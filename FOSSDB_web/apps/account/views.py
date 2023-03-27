from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegisterForm


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("")
    else:
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"title": "Sign Up", "form": form})


def login_(request):
    return render(request, "registration/login.html", {"title": "Login"})
