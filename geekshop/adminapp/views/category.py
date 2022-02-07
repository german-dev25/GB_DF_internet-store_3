from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ProductCategoryAdminForm
from mainapp.models import ProductCategory
from adminapp.utils import superuser_required


@superuser_required
def category_create(request):
    if request.method == 'POST':
        form = ProductCategoryAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategoryAdminForm()

    content = {'title': 'Создание категории', 'form': form}
    return render(request, 'adminapp/category/edit.html', content)


@superuser_required
def categories(request):
    categories = ProductCategory.objects.all().order_by('id')

    return render(request, 'adminapp/category/categories.html', context={
        'title': 'Категории',
        'objects': categories,
    })


@superuser_required
def category_update(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryAdminForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategoryAdminForm(instance=category)

    content = {'title': 'Редактирование категории', 'form': form}
    return render(request, 'adminapp/category/edit.html', content)


@superuser_required
def category_delete(request, pk):
    title = 'Удаление категории'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.delete()
        # category.is_active = False
        # category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category/delete.html', content)
