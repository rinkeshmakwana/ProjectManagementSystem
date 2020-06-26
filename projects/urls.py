from django.urls import path
from .views import ProjectListView, new_project 


urlpatterns = [
    path('', ProjectListView.as_view() , name='projects-list'),
    path('new-project/', new_project, name='new-project'),
]