from django.urls import path

from . import views

urlpatterns = [
    path("profile/", views.ProfileUpdateView.as_view(), name="settings"),
    path("security/", views.PasswordChangeView.as_view(), name="change_password"),
]
