from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProjectDetailView.as_view(), name="project-detail"),
    path("edit/", views.ProjectUpdateView.as_view(), name="project-update"),
    path("delete/", views.ProjectDeleteView.as_view(), name="project-delete"),
]
