# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def inicio(request):
    return render(request, 'usuarios/inicio.html')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registrar.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
    return render(request, 'usuarios/iniciar_sesion.html')

def menu(request):
    return render(request, 'usuarios/menu.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')
