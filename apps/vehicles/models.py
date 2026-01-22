from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class EmissionFactor(models.Model):
    """
    Facteurs d'émission ADEME pour les carburants et véhicules
    """
    CATEGORY_CHOICES = [
        ('fuel', 'Carburant'),
        ('vehicle_km', 'Véhicule par km'),
    ]
    
    name = models.CharField(
        max_length=100,
        verbose_name="Nom"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Catégorie"
    )
    subcategory = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Sous-catégorie",
        help_text="Ex: essence, gazole, voiture_thermique"
    )
    unit = models.CharField(
        max_length=20,
        verbose_name="Unité",
        help_text="L, km, kWh, etc."
    )
    factor_value = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        verbose_name="Facteur d'émission",
        help_text="kg CO₂e par unité"
    )
    source = models.CharField(
        max_length=200,
        default="ADEME Base Carbone",
        verbose_name="Source"
    )
    source_url = models.URLField(
        blank=True,
        verbose_name="URL source"
    )
    valid_from = models.DateField(
        null=True,
        blank=True,
        verbose_name="Valide depuis"
    )
    verified_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Vérifié le"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Actif"
    )
    
    class Meta:
        verbose_name = "Facteur d'émission"
        verbose_name_plural = "Facteurs d'émission"
        ordering = ['category', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.factor_value} kg CO₂e/{self.unit})"


class VehicleData(models.Model):
    """
    Données de consommation des véhicules par service
    """
    CALCULATION_METHOD_CHOICES = [
        ('fuel', 'Par carburant'),
        ('distance', 'Par distance'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur"
    )
    year = models.IntegerField(
        default=2026,
        verbose_name="Année"
    )
    service = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Service/Direction"
    )
    calculation_method = models.CharField(
        max_length=20,
        choices=CALCULATION_METHOD_CHOICES,
        default='fuel',
        verbose_name="Méthode de calcul"
    )
    
    # Méthode par carburant
    essence_liters = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        null=True,
        blank=True,
        verbose_name="Essence (litres)",
        help_text="Consommation totale d'essence en litres"
    )
    gazole_liters = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        null=True,
        blank=True,
        verbose_name="Gazole (litres)",
        help_text="Consommation totale de gazole en litres"
    )
    
    # Méthode par distance
    distance_km = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        null=True,
        blank=True,
        verbose_name="Distance (km)",
        help_text="Distance totale parcourue en kilomètres"
    )
    
    # Résultats calculés
    total_co2_kg = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True,
        verbose_name="Total CO₂ (kg)",
        help_text="Impact carbone total en kg CO₂e"
    )
    essence_co2_kg = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True,
        verbose_name="CO₂ Essence (kg)"
    )
    gazole_co2_kg = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True,
        verbose_name="CO₂ Gazole (kg)"
    )
    
    # Métadonnées
    notes = models.TextField(
        blank=True,
        verbose_name="Notes"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Créé le"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Mis à jour le"
    )
    
    class Meta:
        verbose_name = "Donnée véhicule"
        verbose_name_plural = "Données véhicules"
        ordering = ['-created_at']
        unique_together = [['user', 'year', 'service']]
    
    def __str__(self):
        return f"{self.service or 'Service'} - {self.year} ({self.user.username})"
    
    def calculate_impact(self):
        """Calcule l'impact carbone total"""
        # Facteurs ADEME vérifiés
        FACTEUR_ESSENCE = Decimal('2.79')  # kg CO₂e/L
        FACTEUR_GAZOLE = Decimal('3.16')   # kg CO₂e/L
        FACTEUR_KM = Decimal('0.192')      # kg CO₂e/km (voiture thermique)
        
        if self.calculation_method == 'fuel':
            essence_impact = (self.essence_liters or Decimal('0')) * FACTEUR_ESSENCE
            gazole_impact = (self.gazole_liters or Decimal('0')) * FACTEUR_GAZOLE
            
            self.essence_co2_kg = essence_impact
            self.gazole_co2_kg = gazole_impact
            self.total_co2_kg = essence_impact + gazole_impact
        
        elif self.calculation_method == 'distance':
            self.total_co2_kg = (self.distance_km or Decimal('0')) * FACTEUR_KM
        
        return self.total_co2_kg
    
    def save(self, *args, **kwargs):
        """Override save pour calculer automatiquement l'impact"""
        self.calculate_impact()
        super().save(*args, **kwargs)
    
    @property
    def total_co2_tonnes(self):
        """Retourne l'impact en tonnes"""
        if self.total_co2_kg:
            return self.total_co2_kg / Decimal('1000')
        return Decimal('0')
