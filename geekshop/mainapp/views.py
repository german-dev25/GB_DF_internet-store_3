from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory

MENU_LINKS = [
    {'url': 'main', 'active': ['main'],'name': 'домой'},
    {'url': 'products:all', 'active': ['products:all', 'products:category'], 'name': 'продукты'},
    {'url': 'contact', 'active': ['contact'], 'name': 'контакты'},
]


def index(request):
    products = Product.objects.all()[:4]

    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'products': products,
    })


def products(request):
    # with open('products.json', 'r', encoding='UTF-8') as file:
    #     products = json.load(file)
    products = Product.objects.all()[:4]
    categories = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': products,
        'categories': categories
    })


def category(request, pk):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': products,
        'categories': categories
    })

def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
