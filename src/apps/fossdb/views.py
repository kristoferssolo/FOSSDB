from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from django_filters.views import FilterView

from .filters import ProjectFilter

from .forms import HostingPlatformForm, ProgrammingLanguageForm, ProjectForm
from .models import Project, ProjectProgrammingLanguage

ProgrammingLanguageInlineFormset = inlineformset_factory(
    Project,
    ProjectProgrammingLanguage,
    form=ProgrammingLanguageForm,
    extra=1,
)


class ProjectListView(FilterView):
    model = Project
    template_name = "explore.html"
    filterset_class = ProjectFilter
    context_object_name = "projects"
    paginate_by = 100  # optional 10 projects a page


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "create_view.html"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["hosting_platform"] = HostingPlatformForm(self.request.POST or None, prefix="hosting")
        data["programming_language"] = ProgrammingLanguageInlineFormset(self.request.POST or None, prefix="language")
        data["empty_form"] = ProgrammingLanguageInlineFormset(prefix="language_empty")
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.owner = self.request.user
        hosting_platform = context["hosting_platform"]
        programming_language = context["programming_language"]
        self.object = form.save()
        if hosting_platform.is_valid():
            hosting_platform.instance.project = self.object
            hosting_platform.save()
        # TODO: allow adding multiple languages
        if programming_language.is_valid():
            for instance in programming_language.save(commit=False):
                instance.project = self.object
                instance.save()
        programming_language.save_m2m()
        if hosting_platform.is_valid() and programming_language.is_valid():
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ProjectDetailView(DetailView):
    model = Project
    template_name = "detailed_view.html"
    context_object_name = "project"
    slug_field = "name"
    slug_url_kwarg = "project_name"


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = "create_view.html"
    form_class = ProjectForm
    slug_field = "name"
    slug_url_kwarg = "project_name"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("login")

    def get_context_data(self, *args, **kwargs):
        data = super(ProjectUpdateView, self).get_context_data(**kwargs)
        data["hosting_platform"] = HostingPlatformForm(self.request.POST or None, instance=self.object.projecthostingplatform, prefix="hosting")
        data["programming_language"] = ProgrammingLanguageInlineFormset(self.request.POST or None, instance=self.object, prefix="language")
        data["empty_form"] = ProgrammingLanguageInlineFormset(prefix="language_empty")
        return data


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "delete_view.html"
    slug_field = "name"
    slug_url_kwarg = "project_name"
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    success_url = "/"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("login")
