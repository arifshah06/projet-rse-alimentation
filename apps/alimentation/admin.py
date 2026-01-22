# Register your models here.
from django.contrib import admin
from .models import FoodEmissionFactor, FoodEntry

@admin.register(FoodEmissionFactor)
class FoodEmissionFactorAdmin(admin.ModelAdmin):
    list_display = ("code", "label", "kg_co2_per_meal")