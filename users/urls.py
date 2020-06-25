from django.urls import path
from .views import usersView, register, login_view, logout_view


urlpatterns = [
    path('', usersView, name='users'),
    path('new-user/', register, name='new-user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]