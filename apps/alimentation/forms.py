# apps/alimentation/forms.py
from django import forms
from .models import FoodEntry

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = [
            "year",
            "service",
            "beef_meals",
            "pork_meals",
            "poultry_fish_meals",
            "vegetarian_meals",
            "picnic_no_meat_meals",
            "picnic_meat_meals",
        ]
        widgets = {
            "year": forms.Select(attrs={"class": "form-input"}),
            "service": forms.TextInput(attrs={"class": "form-input"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        # Exemple : pré-remplir le service selon le profil
        if user and not self.instance.pk:
            self.fields["service"].initial = getattr(user, "service_name", "")
