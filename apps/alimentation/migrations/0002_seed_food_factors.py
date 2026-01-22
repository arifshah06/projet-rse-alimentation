from django.db import migrations

def seed_food_factors(apps, schema_editor):
    FoodEmissionFactor = apps.get_model("alimentation", "FoodEmissionFactor")

    data = [
        ("beef", "Repas dominante bœuf/veau", 9),
        ("pork", "Repas dominante porc", 2.00),
        ("poultry_fish", "Repas dominante poulet/poisson", 1.50),
        ("vegetarian", "Repas végétarien", 0.51),
        ("picnic_veg", "Pique-nique sans viande", 0.51),
        ("picnic_meat", "Pique-nique avec viande", 1.50),
    ]

    for code, label, factor in data:
        FoodEmissionFactor.objects.update_or_create(
            code=code,
            defaults={"label": label, "kg_co2_per_meal": factor},
        )

def unseed_food_factors(apps, schema_editor):
    FoodEmissionFactor = apps.get_model("alimentation", "FoodEmissionFactor")
    FoodEmissionFactor.objects.filter(
        code__in=[
            "beef",
            "pork",
            "poultry_fish",
            "vegetarian",
            "picnic_veg",
            "picnic_meat",
        ]
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ("alimentation", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_food_factors, unseed_food_factors),
    ]
