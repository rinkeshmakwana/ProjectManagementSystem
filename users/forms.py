from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()

        return user


class UserProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['emp_type']

    def save(self, commit=True):
        userprofile = super(UserProfileRegisterForm, self).save(commit=False)
        userprofile.emp_type = self.cleaned_data['emp_type']

        if commit:
            user = User.objects.latest('pk')
            user_profile = UserProfile.objects.get(user=user)
            user_profile.emp_type = userprofile.emp_type
            user_profile.save()

        return userprofile
