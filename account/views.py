from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, PerfilForm
from .models import Perfil

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.perfil.tipo == 'admin':
                    return redirect('perfil_admin')
                elif user.perfil.tipo == 'staff':
                    return redirect('perfil_staff')
                else:
                    return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(lambda u: u.perfil.tipo == 'admin')
def perfil_admin(request):
    return render(request, 'perfil_admin.html')

@login_required
@user_passes_test(lambda u: u.perfil.tipo == 'staff')
def perfil_staff(request):
    return render(request, 'perfil_staff.html')

@login_required
def perfil(request):
    nombre_usuario = request.user.username
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'perfil.html', {'form': form, 'nombre_usuario': nombre_usuario})



def home(request):
    return render(request, 'home.html')