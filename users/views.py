from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from projects.models import Project
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy


def usersView(request):
    users = UserProfile.objects.all()
    projects = Project.objects.all()
    context = {
        'users': users,
        'projects': projects,
    }
    return render(request, 'users/users.html', context)


class RegistrationView(CreateView):
    model = UserProfile
    form_class = UserRegistrationForm
    template_name = 'users/register_form.html'
    success_url = reverse_lazy('new-user')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('projects-list')
        else:
            return render(request, 'users/login.html', {'login_form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'login_form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
