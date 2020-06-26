from django.shortcuts import render
from .models import Project
from django.views.generic import ListView
from .forms import ProjectCreateForm


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    # context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects_new'] = Project.objects.filter(status='1').order_by('-end_date')
        context['projects_progress'] = Project.objects.filter(status='2').order_by('-end_date')
        context['projects_completed'] = Project.objects.filter(status='3').order_by('-end_date')
        context['projects_cancelled'] = Project.objects.filter(status='4').order_by('-end_date')
        return context

# Create your views here.
# def projects(request):
#     projects_list = Project.objects.all()    
#     context = {
#         'projects': projects_list,
#     }
#     return render(request, 'projects/projects.html', context)


def new_project(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            form = ProjectCreateForm()
            return render(request, 'projects/new_project.html', context)
        else:
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'projects/new_project.html', context)
