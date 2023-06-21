# Standard library imports
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from typing import Any, Dict, Union, Optional

# Third-party imports

# Local application/library imports
from .forms import SearchForm
from .models import Category, Product
from .choices import SORTING_VALUES
from src.cart.forms import CartAddProductForm


def product_list(request: HttpRequest) -> HttpResponse:
    """List of products"""
    data = filters(request)
    data['cart_product_form'] = CartAddProductForm()
    return render(
        request,
        'shop/list.html',
        data
    )


def product_detail(request: HttpRequest, category_slug: Optional[str] = None,
                   pk: Optional[int] = None, slug: Optional[str] = None) -> HttpResponse:
    """Product details"""
    product = get_object_or_404(Product, id=pk, slug=slug, available=True)
    similar_products = Product.objects.filter(category=product.category, name__icontains=product.name).exclude(
        id=product.id)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'shop/detail.html',
        {
            'product': product,
            'similar_products': similar_products,
            'cart_product_form': cart_product_form,
        }
    )


def filters(request: HttpRequest) -> Dict[str, Union[Product, str, Optional[str], Dict[str, Any], Paginator]]:
    """Filters for products"""
    data: Dict[str, Union[Product, str, Optional[str], Dict[str, Any], Paginator]] = {}
    search = request.GET.get('search', None)
    sort = request.GET.get('sort', None)
    page_number = request.GET.get('page', None)
    gender = request.GET.get('gender', None)

    products: QuerySet[Product] = Product.objects.filter(available=True)

    if search:
        products = products.filter(name__icontains=search)
    if gender:
        products = products.filter(gender=gender)

    sorting_options: Dict[str, str] = {
        'price_low': 'price',
        'price_high': '-price',
        'name_a_z': 'name',
        'name_z_a': '-name',
    }

    if sort:
        sort_key: Optional[str] = sorting_options.get(sort)
        if sort_key:
            products = products.order_by(sort_key)

    paginator: Paginator = Paginator(products, 9)
    page_obj = paginator.get_page(page_number)

    try:
        products = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        products = paginator.page(1)

    data['products'] = products
    data['search'] = search
    data['sort'] = sort
    data['sorting_values'] = SORTING_VALUES
    data['page_obj'] = page_obj
    data['gender'] = gender
    # data['page'] = page_number if page_number else 1

    url_params = '&'.join(
        [f"{key}={data[key]}" for key in data if key not in ['products', 'sorting_values', 'page_obj'] and data[key]])

    url_string = f"?{url_params}"
    data['url_string'] = url_string
    return data
