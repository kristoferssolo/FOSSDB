from django.urls import path

from . import views

urlpatterns = [
    path("", views.sign_up, name="singup"),
    path("signup", views.sign_up, name="signup"),
    path("login", views.login_, name="login"),
]
