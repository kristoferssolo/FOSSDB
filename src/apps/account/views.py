from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, SignUpForm
from .models import User


def profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        "title": user.username + ("" if not user.full_name else f" ({user.full_name})"),
        "user": user,
    }
    return render(request, "profile.html", context)


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("homepage")

    context = {
        "title": "FOSSDB | SignUp",
        "form": form,
    }
    return render(request, "signup.html", context)


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("homepage")

    context = {
        "title": "FOSSDB | Login",
        "form": form,
    }
    return render(request, "login.html", context)
