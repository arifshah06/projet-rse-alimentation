# apps/alimentation/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

class FoodEmissionFactor(models.Model):
    """
    Facteur moyen kgCO2e / repas pour une catégorie Agribalyse.
    Ex : boeuf, porc, volaille/poisson, végétarien, pique-nique...
    """
    code = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
    kg_co2_per_meal = models.DecimalField(
        max_digits=6, decimal_places=3,
        validators=[MinValueValidator(0)]
    )
    source = models.CharField(
        max_length=200,
        default="ADEME Base Carbone / Agribalyse"
    )

    class Meta:
        verbose_name = "Facteur d'émission repas"
        verbose_name_plural = "Facteurs d'émission repas"

    def __str__(self):
        return f"{self.label} ({self.kg_co2_per_meal} kgCO2e/repas)"


class FoodEntry(models.Model):
    """
    Saisie annuelle par service : nombre de repas par type.
    """
    YEAR_CHOICES = [(y, y) for y in range(2020, 2036)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=150)
    year = models.IntegerField(choices=YEAR_CHOICES)

    # Nombre de repas sur l'année
    beef_meals = models.PositiveIntegerField(
        default=0, verbose_name="Repas bœuf/veau"
    )
    pork_meals = models.PositiveIntegerField(
        default=0, verbose_name="Repas porc"
    )
    poultry_fish_meals = models.PositiveIntegerField(
        default=0, verbose_name="Repas poulet/poisson"
    )
    vegetarian_meals = models.PositiveIntegerField(
        default=0, verbose_name="Repas végétariens"
    )
    picnic_no_meat_meals = models.PositiveIntegerField(
        default=0, verbose_name="Pique-niques sans viande"
    )
    picnic_meat_meals = models.PositiveIntegerField(
        default=0, verbose_name="Pique-niques avec viande"
    )

    total_co2_kg = models.DecimalField(
        max_digits=12, decimal_places=3,
        null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Donnée alimentation"
        verbose_name_plural = "Données alimentation"
        ordering = ["-year", "service"]
        unique_together = ("service", "year")

    def calculate_impact(self):
        factors = {f.code: f.kg_co2_per_meal for f in FoodEmissionFactor.objects.all()}

        def f(code):
            return factors.get(code, 0)

        total = (
            self.beef_meals * f("beef")
            + self.pork_meals * f("pork")
            + self.poultry_fish_meals * f("poultry_fish")
            + self.vegetarian_meals * f("vegetarian")
            + self.picnic_no_meat_meals * f("picnic_veg")
            + self.picnic_meat_meals * f("picnic_meat")
        )
        self.total_co2_kg = total
        return total

    def save(self, *args, **kwargs):
        self.calculate_impact()
        super().save(*args, **kwargs)
