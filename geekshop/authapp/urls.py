from . import views
from django.urls import path

app_name = 'authapp'

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('edit', views.edit, name='edit'),
]