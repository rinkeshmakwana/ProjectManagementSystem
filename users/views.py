from django.shortcuts import render, redirect
from .models import UserProfile
from projects.models import Project
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def usersView(request):
    users = UserProfile.objects.all()
    projects = Project.objects.all()
    context = {
        'users': users,
        'projects': projects,
    }
    return render(request, 'users/users.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            user = form.save()
            created = True
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'created': created}
            return render(request, 'users/register_form.html', context)
        else:
            return render(request, 'users/register_form.html', context)
    else:
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'users/register_form.html', context)


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
