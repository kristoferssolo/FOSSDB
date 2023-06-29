import django_filters
from django.contrib.auth import get_user_model

from .models import Project

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("username",)


class ProjectFilter(django_filters.FilterSet):
    owner = UserFilter()
    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Project
        fields = (
            "owner",
            "name",
            "description",
        )
