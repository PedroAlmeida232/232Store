from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'usuarios/index.html')

# Cadastro
def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe')
        else:
            User.objects.create_user(username=username, password=senha)
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html')


# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'usuarios/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Página protegida
@login_required(login_url='login')
def home_view(request):
    return render(request, 'usuarios/home.html')
