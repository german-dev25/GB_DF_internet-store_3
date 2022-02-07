from . import views
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='all'),
    path('<int:category_id>', views.category, name='category'),
    path('product/<int:product_id>', views.product, name='product'),
]