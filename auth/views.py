from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from auth.forms import RegistrationForm, LoginForm


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    username = None

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            form = None
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'username': username
    }

    return render(
        request,
        'signup.html',
        context
    )


def login(request):
    msg = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    form = LoginForm()
                    msg = 'Пользователь с такими данными не зарегистрирован'
            else:
                form = LoginForm()
                msg = 'Данные для входа введены неправильно'
    else:
        form = LoginForm()

    context = {
        'form': form,
        'msg': msg
    }

    return render(
        request,
        'login.html',
        context
    )


def logout(request):
    auth.logout(request)

    return render(
        request,
        'logout.html'
    )
