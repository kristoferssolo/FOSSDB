from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("settings/", views.ProfileUpdateView.as_view(), name="settings"),
    path("settings/security/", views.PasswordChangeView.as_view(), name="change_password"),
]
