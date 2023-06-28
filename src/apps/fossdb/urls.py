from django.urls import path

from . import views

urlpatterns = [
    path("explore/", views.ProjectListView.as_view(), name="explore"),
    path("add/", views.ProjectCreateView.as_view(), name="add-project"),
    path("<str:owner>/<str:project_name>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("<str:owner>/<str:project_name>/edit/", views.ProjectUpdateView.as_view(), name="project-update"),
    path("<str:owner>/<str:project_name>/delete/", views.ProjectDeleteView.as_view(), name="project-delete"),
]
