from django.urls import path
from .views import usersView, RegistrationView, login_view, logout_view


urlpatterns = [
    path('', usersView, name='users'),
    path('new-user/', RegistrationView.as_view(), name='new-user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]