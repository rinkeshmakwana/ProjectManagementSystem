from django.shortcuts import render
from .models import Project
from users.models import UserProfile
from .forms import ProjectCreateForm


# Create your views here.
def projects(request):
    projects_list = Project.objects.all()    
    context = {
        'projects': projects_list,
    }
    return render(request, 'projects/projects.html', context)


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
