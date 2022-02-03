from . import views
from django.urls import path

app_name = 'basketapp'

urlpatterns = [
    path('', views.view, name='view'),
    path('add/<int:product_id>', views.add, name='add'),
    path('remove/<int:basket_item_id>', views.remove, name='remove'),
]