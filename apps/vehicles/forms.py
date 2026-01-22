from django import forms
from .models import VehicleData
from decimal import Decimal


class VehicleFuelForm(forms.ModelForm):
    """Formulaire de saisie par carburant"""
    
    class Meta:
        model = VehicleData
        fields = ['year', 'service', 'essence_liters', 'gazole_liters', 'notes']
        widgets = {
            'year': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '2026',
                'min': '2020',
                'max': '2040'
            }),
            'service': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nom du service ou direction'
            }),
            'essence_liters': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'gazole_liters': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Notes ou commentaires (optionnel)',
                'rows': 3
            }),
        }
        labels = {
            'year': 'Année',
            'service': 'Service / Direction',
            'essence_liters': 'Consommation essence (litres)',
            'gazole_liters': 'Consommation gazole (litres)',
            'notes': 'Notes',
        }
        help_texts = {
            'essence_liters': 'Facteur ADEME : 2.79 kg CO₂e/L',
            'gazole_liters': 'Facteur ADEME : 3.16 kg CO₂e/L',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Rendre les champs de carburant non requis
        self.fields['essence_liters'].required = False
        self.fields['gazole_liters'].required = False
        self.fields['service'].required = False
        self.fields['notes'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        essence = cleaned_data.get('essence_liters')
        gazole = cleaned_data.get('gazole_liters')
        
        # Au moins un carburant doit être renseigné
        if not essence and not gazole:
            raise forms.ValidationError(
                "Vous devez renseigner au moins une consommation (essence ou gazole)."
            )
        
        # Définir la méthode de calcul
        cleaned_data['calculation_method'] = 'fuel'
        
        return cleaned_data


class VehicleDistanceForm(forms.ModelForm):
    """Formulaire de saisie par distance"""
    
    class Meta:
        model = VehicleData
        fields = ['year', 'service', 'distance_km', 'notes']
        widgets = {
            'year': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '2026',
                'min': '2020',
                'max': '2040'
            }),
            'service': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nom du service ou direction'
            }),
            'distance_km': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Notes ou commentaires (optionnel)',
                'rows': 3
            }),
        }
        labels = {
            'year': 'Année',
            'service': 'Service / Direction',
            'distance_km': 'Distance parcourue (km)',
            'notes': 'Notes',
        }
        help_texts = {
            'distance_km': 'Facteur ADEME : 0.192 kg CO₂e/km (voiture thermique moyenne)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].required = False
        self.fields['notes'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        distance = cleaned_data.get('distance_km')
        
        if not distance or distance == Decimal('0'):
            raise forms.ValidationError(
                "Vous devez renseigner une distance parcourue."
            )
        
        # Définir la méthode de calcul
        cleaned_data['calculation_method'] = 'distance'
        
        return cleaned_data
