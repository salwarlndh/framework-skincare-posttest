from django.urls import path
from . import views

# app_name = 'app'
urlpatterns = [
    path('about', views.about),
    path('home', views.homepage),
    path('product', views.product_index2, name='product_index2'),
    path('product/', views.product_index, name='product_index'), # Read product
    path('product/create/', views.product_create, name='product_create'), # Create Product
    path('product/update/<int:product_id>/', views.product_update, name='product_update'), # Update Product
    path('product/delete/<int:product_id>', views.product_delete, name='product_delete'), # Delete Product
]