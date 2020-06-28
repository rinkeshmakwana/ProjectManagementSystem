from django.urls import path
from .views import ( ProjectListView, 
                        ProjectUpdateView, 
                        ProjectDetailView, 
                        ProjectDeleteView, 
                        ProjectCreateView )


urlpatterns = [
    path('', ProjectListView.as_view() , name='projects-list'),
    path('<int:pk>/', ProjectDetailView.as_view() , name='project-detail'),
    path('new-project/', ProjectCreateView.as_view(), name='new-project'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]