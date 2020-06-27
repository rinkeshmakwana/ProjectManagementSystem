from django.forms import ModelForm
from .models import Project
from users.models import UserProfile


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def save(self, commit=True):
        Project = super(ProjectCreateForm, self).save(commit=False)
        Project.project_name = self.cleaned_data['project_name']
        Project.status = self.cleaned_data['status']
        Project.end_date = self.cleaned_data['end_date']
        Project.description = self.cleaned_data['description']
        Project.save()
        assigns = self.cleaned_data['assign']
        users = UserProfile.objects.all()
        for assign in assigns:
            Project.assign.add((assign))
            for user in users.filter(user=assign):
                user.project.add((Project))
                
        if commit:
            Project.save()

        return Project


    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.fields['project_name'].widget.attrs['class'] = 'form-control'
        self.fields['project_name'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['placeholder'] = 'Dead Line, type a date'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
        self.fields['assign'].widget.attrs['class'] = 'form-control'