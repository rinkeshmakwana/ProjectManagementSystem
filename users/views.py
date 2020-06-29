from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from projects.models import Project
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UserProfileRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
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
    model = User

    def get(self, request, *args, **kwargs):
        p_form = UserProfileRegisterForm()
        u_form = UserRegistrationForm()

        context = {
            'p_form': p_form,
            'u_form': u_form
        }
        return render(request, 'users/register_form.html', context)

    def post(self, request, *args, **kwargs):
        p_form = UserProfileRegisterForm(request.POST)
        u_form = UserRegistrationForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been created.')
            return redirect('users')
        else:
            u_form = UserRegistrationForm()
            p_form = UserProfileRegisterForm()
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
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


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
