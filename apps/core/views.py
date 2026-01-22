from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.vehicles.models import VehicleData, EmissionFactor


def login_view(request):
    """Vue de connexion"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'dashboard'
            return redirect(next_url)
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    
    return render(request, 'core/login.html')


def logout_view(request):
    """Vue de déconnexion"""
    auth_logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('login')


@login_required
def dashboard_view(request):
    """Vue du tableau de bord"""
    context = {
        'vehicle_count': VehicleData.objects.filter(user=request.user).count(),
        'emission_factors_count': EmissionFactor.objects.filter(is_active=True).count(),
    }
    return render(request, 'core/dashboard.html', context)
