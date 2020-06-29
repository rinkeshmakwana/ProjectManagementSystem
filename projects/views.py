from .models import Project
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from .forms import ProjectCreateForm
from django.urls import reverse_lazy


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects_new'] = Project.objects.filter(status='1').order_by('-end_date')
        context['projects_progress'] = Project.objects.filter(status='2').order_by('-end_date')
        context['projects_completed'] = Project.objects.filter(status='3').order_by('-end_date')
        context['projects_cancelled'] = Project.objects.filter(status='4').order_by('-end_date')
        return context


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy('projects-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projects-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects-list')
