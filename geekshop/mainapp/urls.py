from . import views
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='all'),
    path('<int:pk>', views.category, name='category'),
]