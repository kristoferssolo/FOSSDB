from account.views import ProfileProjectListView
from django.urls import path
from fossdb.views import ProjectCreateView, ProjectListView, SearchResultsListView

from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("search/", SearchResultsListView.as_view(), name="search"),
    path("explore/", ProjectListView.as_view(), name="explore"),
    path("contribute/", ProjectCreateView.as_view(), name="contribute"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("news/", views.news, name="news"),
    path("help/", views.help, name="help"),
    path("<str:username>/", ProfileProjectListView.as_view(), name="profile"),
]
