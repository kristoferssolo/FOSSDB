from django.shortcuts import render


def homepage(request):
    return render(request, "main/homepage.html", {"title": "FOSSDB"})


def contribute(request):
    return render(request, "main/contribute.html", {"title": "FOSSDB | Contribute"})


def news(request):
    return render(request, "main/news.html", {"title": "FOSSDB | News"})


def dashboard(request):
    return render(request, "main/dashboard.html", {"title": "FOSSDB | Dashboard"})


def help(request):
    return render(request, "main/help.html", {"title": "FOSSDB | Help"})
