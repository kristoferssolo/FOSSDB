from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_project, name="add-project"),
    path("<str:username>/<str:project_name>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("<str:username>/<str:project_name>/update/", views.ProjectUpdateView.as_view(), name="project-update"),
]
