from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("contribute/", views.contribute, name="contribute"),
    path("news/", views.news, name="news"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("help/", views.help, name="help"),
]
