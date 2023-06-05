from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # path('M/', views.product_list, {'hender': 'M'}, name='product_list_M'),
    # path('W/', views.product_list, {'hender': 'W'}, name='product_list_W'),
    # path('K/', views.product_list, {'hender': 'K'}, name='product_list_K'),
    # path('search/', views.Search.as_view(), name='search'),
    # path('search/', views.search, name='search'),
    # path('<slug:category_slug>/', views.product_list,
    #      name='product_list_by_category'),
    # path('<slug:category_slug>/<slug:subcategory_slug>/', views.product_list_by_subcategory,
    #      name='product_list_by_subcategory'),
    path('<slug:category_slug>/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
