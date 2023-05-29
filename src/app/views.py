from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django import forms 

@login_required(login_url='/logar_usuario')
def home(request):
    return render(request, 'home.html')

def deslogar_usuario(request):
    logout(request)
    return redirect('index')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'users/cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            # pegando código da empresa
            # user = User.objects.get(pk = request.user.id)
            # prof = user.get_profile()
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'users/login.html', {'form_login': form_login})

# def index(request):
#     return render(request, 'users/login.html')

@login_required(login_url='/logar_usuario')
def index(request):
    return render(request, 'users/login.html')

# @login_required(login_url='/logar_usuario')
# def deslogar_usuario(request):
#     logout(request)
#     return redirect('index')

@login_required(login_url='/logar_usuario')
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'users/alterar_senha.html', {'form_senha': form_senha})



