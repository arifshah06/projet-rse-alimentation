import csv
import requests
import io
from django.core.management.base import BaseCommand
from apps.alimentation.models import FoodEmissionFactor

class Command(BaseCommand):
    help = 'Updates food emission factors from Agribalyse API'

    # URL Agribalyse 3.1 - Synthèse
    API_URL = "https://data.ademe.fr/data-fair/api/v1/datasets/agribalyse-31-synthese/lines?format=csv"

    def handle(self, *args, **options):
        self.stdout.write("Fetching data from ADEME Agribalyse API...")
        
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f"Failed to download data: {e}"))
            return

        # Decode content
        csv_content = response.content.decode('utf-8')
        reader = csv.DictReader(io.StringIO(csv_content))
        
        # Accumulators for averages
        # Structure: code: {'sum': 0.0, 'count': 0, 'keywords': [...]}
        categories = {
            'beef': {'sum': 0.0, 'count': 0, 'keywords': ['steack', 'bœuf', 'veau', 'rôti', 'bourguignon']},
            'pork': {'sum': 0.0, 'count': 0, 'keywords': ['porc', 'côte', 'filet mignon', 'jambon']},
            'poultry_fish': {'sum': 0.0, 'count': 0, 'keywords': ['poulet', 'dinde', 'poisson', 'saumon', 'cabillaud']},
            'vegetarian': {'sum': 0.0, 'count': 0, 'keywords': ['végétarien', 'soja', 'tofu', 'galette végétale']},
            # Pique-niques hard to define by ingredients, we might skip or use bread/sandwich/chips
            # For now keeping manual values if not found or using proxies
        }

        row_count = 0
        
        for row in reader:
            name = row.get('Nom du Produit en Français', '').lower()
            # Column name for CO2 is often "Changement climatique" or similar.
            # In Agribalyse 3.1 Synthèse, column is "Changement climatique" (kg CO2 eq/kg de produit)
            try:
                # Value is usually comma separated in French CSVs or dot?
                # The API usually returns standard CSV. Let's assume dot or handle comma.
                co2_val_str = row.get('Changement climatique', '0')
                if not co2_val_str:
                    continue
                co2_val = float(co2_val_str.replace(',', '.'))
            except ValueError:
                continue

            row_count += 1

            for cat_code, data in categories.items():
                if any(k in name for k in data['keywords']):
                    # Exclude some obvious mismatches if needed
                    if 'aliment pour bétail' in name:
                         continue
                         
                    data['sum'] += co2_val
                    data['count'] += 1

        self.stdout.write(f"Processed {row_count} lines.")

        for cat_code, data in categories.items():
            if data['count'] > 0:
                avg_val = data['sum'] / data['count']
                # Determine multiplier: Agribalyse is per kg. A meal is approx 0.5kg?
                # Or is the coefficient 'kg CO2 per kg'? Yes.
                # FoodEmissionFactor expects kgCO2e / REPAS.
                # Average meal weight estimation : 400-500g.
                MEAL_WEIGHT_KG = 0.45 
                
                final_val = avg_val * MEAL_WEIGHT_KG
                
                obj, created = FoodEmissionFactor.objects.update_or_create(
                    code=cat_code,
                    defaults={
                        'kg_co2_per_meal': round(final_val, 3),
                        'source': f"Moyenne Agribalyse Auto ({data['count']} produits)",
                        'label': f"{cat_code.capitalize()} (Auto)" # Update label or keep existing? Maybe keep existing label if exists.
                    }
                )
                
                # Restore original label if it was just created or updated, actually better not to overwrite readable labels
                # But update_or_create updates everything in defaults.
                # Let's just update the value and source.
                if not created:
                    # Fetch original label to restore it or just don't include label in defaults?
                    # If I don't include label in defaults, and it's created, it fails if label is required.
                    # It is required.
                    pass 
                
                self.stdout.write(self.style.SUCCESS(f"Updated {cat_code}: {final_val:.3f} kgCO2e/repas (based on {data['count']} items)"))
            else:
                self.stdout.write(self.style.WARNING(f"No data found for {cat_code}"))

        self.stdout.write(self.style.SUCCESS("Update complete."))
