from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import ProjectForm
from .hosting_platform.forms import HostingPlatformForm
from .hosting_platform.models import ProjectHostingPlatform
from .models import Project
from .programming_language.forms import ProgrammingLanguageForm
from .programming_language.models import ProjectProgrammingLanguage


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
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        response = None
        with transaction.atomic():
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
    form_class = ProjectForm
    slug_field = "name"
    slug_url_kwarg = "project_name"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner__username=self.kwargs.get("username"))

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("index")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["project_form"] = ProjectForm(self.request.POST, instance=self.object)
            context["hosting_platform_form"] = HostingPlatformForm(self.request.POST, instance=self.object)
            context["programming_language_form"] = ProgrammingLanguageForm(self.request.POST, instance=self.object)
        else:
            context["project_form"] = ProjectForm(instance=self.object)
            context["hosting_platform_form"] = HostingPlatformForm(instance=self.object)
            context["programming_language_form"] = ProgrammingLanguageForm(instance=self.object)

        return context


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "fossdb/delete_view.html"
    slug_field = "name"
    slug_url_kwarg = "project_name"
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    success_url = "/"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner__username=self.kwargs.get("username"))

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("index")
