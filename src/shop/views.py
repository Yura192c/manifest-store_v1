from django.views.generic import ListView, DetailView
from .forms import SearchForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from src.cart.forms import CartAddProductForm
from .choices import SORTING_VALUES

# from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request):
    """Список Товаров"""
    data = filters(request)
    return render(request,
                    'shop/list.html',
                  data)


def product_detail(request, category_slug=None, id=None, slug=None):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form
                   })


def filters(request):
    data = {}
    search = request.GET.get('search', None)
    sort = request.GET.get('sort', None)
    page_number = request.GET.get('page', None)
    hender = request.GET.get('hender', None)

    if search is not None:
        if hender is not None:
            products = Product.objects.filter(available=True, name__icontains=search, hender=hender)
        else:
            products = Product.objects.filter(available=True, name__icontains=search)

    else:
        if hender is not None:
            products = Product.objects.filter(available=True, hender=hender)
        else:
            products = Product.objects.filter(available=True)

    if sort is not None:
        if sort == 'price_low':
            products = products.order_by('price')
        elif sort == 'price_high':
            products = products.order_by('-price')
        elif sort == 'name_a_z':
            products = products.order_by('name')
        elif sort == 'name_z_a':
            products = products.order_by('-name')

    paginator = Paginator(products, 9)

    page_obj = paginator.get_page(page_number)
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)

    data['products'] = products
    data['search'] = search
    data['sort'] = sort
    data['sorting_values'] = SORTING_VALUES
    data['page_obj'] = page_obj
    data['hender'] = hender

    return data