from django.contrib import admin
from .models import EmissionFactor, VehicleData


@admin.register(EmissionFactor)
class EmissionFactorAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'factor_value', 'unit', 'source', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'subcategory']
    ordering = ['category', 'name']
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('name', 'category', 'subcategory', 'unit', 'factor_value')
        }),
        ('Source et validation', {
            'fields': ('source', 'source_url', 'valid_from', 'is_active')
        }),
    )


@admin.register(VehicleData)
class VehicleDataAdmin(admin.ModelAdmin):
    list_display = [
        'year', 'service', 'user', 'calculation_method',
        'total_co2_kg', 'created_at'
    ]
    list_filter = ['year', 'calculation_method', 'service']
    search_fields = ['service', 'user__username', 'notes']
    ordering = ['-year', '-created_at']
    readonly_fields = ['total_co2_kg', 'essence_co2_kg', 'gazole_co2_kg', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('user', 'year', 'service', 'calculation_method')
        }),
        ('Méthode par carburant', {
            'fields': ('essence_liters', 'gazole_liters'),
            'classes': ['collapse'],
        }),
        ('Méthode par distance', {
            'fields': ('distance_km',),
            'classes': ['collapse'],
        }),
        ('Résultats', {
            'fields': ('total_co2_kg', 'essence_co2_kg', 'gazole_co2_kg'),
            'classes': ['wide'],
        }),
        ('Métadonnées', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ['collapse'],
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Auto-assigne l'utilisateur si non défini"""
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
