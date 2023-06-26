from django import forms
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import ProjectForm
from .hosting_platform.forms import HostingPlatformForm
from .models import Project
from .programming_language.forms import ProgrammingLanguageForm

User = settings.AUTH_USER_MODEL


def index(request):
    context = {
        "title": "FOSSDB",
        "projects": Project.objects.all(),
    }
    return render(request, "fossdb/index.html", context)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "fossdb/add_project.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        hosting_platform_form = HostingPlatformForm(self.request.POST, instance=self.object)
        if hosting_platform_form.is_valid():
            hosting_platform = hosting_platform_form.save(commit=False)
            hosting_platform.project = self.object
            hosting_platform.save()

        # TODO: allow adding multiple languages
        programming_language_form = ProgrammingLanguageForm(self.request.POST, instance=self.object)
        if programming_language_form.is_valid():
            programming_language = programming_language_form.save(commit=False)
            programming_language.project = self.object
            programming_language.save()

        return response

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add project"
        context["project_form"] = ProjectForm()
        context["hosting_platform_form"] = HostingPlatformForm()
        context["programming_language_form"] = ProgrammingLanguageForm()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "fossdb/detailed_view.html"
    context_object_name = "project"
    slug_field = "name"
    slug_url_kwarg = "project_name"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner__username=self.kwargs.get("username"))


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = "fossdb/update_view.html"
    form_class = (
        ProjectForm,
        HostingPlatformForm,
        ProgrammingLanguageForm,
    )
    slug_field = "name"
    slug_url_kwarg = "project_name"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner__username=self.kwargs.get("username"))

    def test_func(self):
        return self.get_object().owner == self.request.user


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "fossdb/delete_view.html"
    slug_field = "name"
    slug_url_kwarg = "project_name"
    success_url = reverse_lazy("index")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner__username=self.kwargs.get("username"))

    def test_func(self):
        return self.get_object().owner == self.request.user
