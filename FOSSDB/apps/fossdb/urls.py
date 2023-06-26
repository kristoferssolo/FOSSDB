from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.ProjectCreateView.as_view(), name="add-project"),
    path("<str:username>/<str:project_name>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("<str:username>/<str:project_name>/update/", views.ProjectUpdateView.as_view(), name="project-update"),
    path("<str:username>/<str:project_name>/delete/", views.ProjectDeleteView.as_view(), name="project-delete"),
]
