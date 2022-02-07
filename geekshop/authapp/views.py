from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.GET.keys():
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse('main'))
    else:
        login_form = ShopUserLoginForm()

    content = {'title': 'Вход', 'form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': 'Вход', 'form': register_form}
    return render(request, 'authapp/register.html', content)


def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': 'Редактирование', 'form': edit_form}
    return render(request, 'authapp/edit.html', content)