from django.urls import path
from .views import projects, new_project


urlpatterns = [
    path('', projects , name='projects-list'),
    path('new-project/', new_project, name='new-project'),
]