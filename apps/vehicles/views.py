from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import VehicleData, EmissionFactor
from .forms import VehicleFuelForm, VehicleDistanceForm


@login_required
def vehicle_form_view(request):
    """Vue du formulaire de saisie véhicules"""
    # Récupérer la méthode choisie (par défaut: fuel)
    method = request.GET.get('method', 'fuel')
    
    if request.method == 'POST':
        # Déterminer quel formulaire utiliser
        if method == 'fuel':
            form = VehicleFuelForm(request.POST)
        else:
            form = VehicleDistanceForm(request.POST)
        
        if form.is_valid():
            vehicle_data = form.save(commit=False)
            vehicle_data.user = request.user
            vehicle_data.calculation_method = form.cleaned_data['calculation_method']
            vehicle_data.save()
            
            messages.success(
                request,
                f'✅ Données enregistrées ! Impact carbone : {vehicle_data.total_co2_kg:.2f} kg CO₂e'
            )
            return redirect('vehicle_list')
    else:
        if method == 'fuel':
            form = VehicleFuelForm()
        else:
            form = VehicleDistanceForm()
    
    # Récupérer les facteurs d'émission pour affichage
    emission_factors = EmissionFactor.objects.filter(is_active=True)
    
    context = {
        'form': form,
        'method': method,
        'emission_factors': emission_factors,
    }
    return render(request, 'vehicles/form.html', context)


@login_required
def vehicle_list_view(request):
    """Vue de la liste des données véhicules"""
    vehicle_data = VehicleData.objects.filter(user=request.user).order_by('-year', '-created_at')
    
    # Calculer le total
    total_co2 = sum(vd.total_co2_kg or 0 for vd in vehicle_data)
    
    context = {
        'vehicle_data': vehicle_data,
        'total_co2': total_co2,
        'count': vehicle_data.count(),
    }
    return render(request, 'vehicles/list.html', context)


@login_required
def vehicle_detail_view(request, pk):
    """Vue de détail d'une donnée véhicule"""
    vehicle_data = get_object_or_404(VehicleData, pk=pk, user=request.user)
    
    context = {
        'vehicle_data': vehicle_data,
    }
    return render(request, 'vehicles/detail.html', context)


@login_required
def vehicle_delete_view(request, pk):
    """Vue de suppression d'une donnée véhicule"""
    vehicle_data = get_object_or_404(VehicleData, pk=pk, user=request.user)
    
    if request.method == 'POST':
        vehicle_data.delete()
        messages.success(request, '🗑️ Donnée supprimée avec succès.')
        return redirect('vehicle_list')
    
    context = {
        'vehicle_data': vehicle_data,
    }
    return render(request, 'vehicles/confirm_delete.html', context)
