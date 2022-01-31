from django.shortcuts import render
from .models import Product, ProductCategory

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'mainapp:products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
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
    categories = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': [],
        'categories': categories
    })


def category(request, pk):
    return products(request)

def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
