from django.shortcuts import redirect, render


def homepage(request):
    return render(request, "homepage.html", {"title": "FOSSDB"})


def login(request):
    return redirect("login")


def logout(request):
    return redirect("logout")


def signup(request):
    return redirect("signup")


def contribute(request):
    return render(request, "contribute.html", {"title": "FOSSDB | Contribute"})


def news(request):
    return render(request, "news.html", {"title": "FOSSDB | News"})


def dashboard(request):
    return render(request, "dashboard.html", {"title": "FOSSDB | Dashboard"})


def help(request):
    return render(request, "help.html", {"title": "FOSSDB | Help"})
