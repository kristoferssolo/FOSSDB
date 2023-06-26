from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(
                username=user.username,
                password=raw_password,
            )
            login(request, user)
            return redirect("index")

    context = {
        "title": "Sign Up",
        "form": form,
    }
    return render(request, "registration/signup.html", context)


def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")

    context = {
        "title": "Login",
        "form": form,
    }
    return render(request, "registration/login.html", context)
