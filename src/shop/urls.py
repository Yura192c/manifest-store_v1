from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/<int:pk>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
