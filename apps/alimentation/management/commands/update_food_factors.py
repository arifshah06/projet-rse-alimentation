import csv
import requests
import io
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.alimentation.models import FoodEmissionFactor

class Command(BaseCommand):
    help = 'Updates food emission factors from local CSV or Agribalyse API'

    API_URL = "https://data.ademe.fr/data-fair/api/v1/datasets/agribalyse-31-synthese/lines?format=csv"
    LOCAL_FILE = os.path.join(settings.BASE_DIR, 'apps', 'alimentation', 'fixtures', 'Base_Carbone_V23.9.csv')

    def handle(self, *args, **options):
        # Accumulators
        categories = {
            'beef': {'sum': 0.0, 'count': 0, 'keywords': ['steack', 'bœuf', 'veau', 'rôti', 'bourguignon', 'viande bovine']},
            'pork': {'sum': 0.0, 'count': 0, 'keywords': ['porc', 'côte', 'filet mignon', 'jambon', 'lardon']},
            'poultry_fish': {'sum': 0.0, 'count': 0, 'keywords': ['poulet', 'dinde', 'poisson', 'saumon', 'cabillaud', 'colin']},
            'vegetarian': {'sum': 0.0, 'count': 0, 'keywords': ['végétarien', 'soja', 'tofu', 'galette végétale', 'steak végétal']},
        }

        content = None
        source_name = ""
        delimiter = ','
        
        # 1. Try Local File
        if os.path.exists(self.LOCAL_FILE):
            self.stdout.write(f"Loading local file: {self.LOCAL_FILE}")
            try:
                # Base Carbone often Latin-1
                with open(self.LOCAL_FILE, 'r', encoding='latin-1') as f:
                    file_lines = f.readlines()
                
                # Find start of data
                start_line = 0
                for i, line in enumerate(file_lines[:50]):
                    if "Identifiant de l'élément" in line or "Nom base français" in line:
                        start_line = i
                        delimiter = ';' # Base Carbone default
                        break
                
                content = file_lines[start_line:]
                source_name = "Base Carbone Local"
            except Exception as e:
                self.stderr.write(self.style.WARNING(f"Error reading local file: {e}"))

        # 2. Fallback to API
        if not content:
            self.stdout.write("Fetching data from ADEME Agribalyse API...")
            try:
                response = requests.get(self.API_URL)
                response.raise_for_status()
                content = response.content.decode('utf-8').splitlines()
                source_name = "Agribalyse API"
                delimiter = ',' 
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Failed to download data: {e}"))
                return

        # Process CSV
        reader = csv.DictReader(content, delimiter=delimiter)
        
        row_count = 0
        matches = 0
        
        for row in reader:
            # Normalize names
            name = row.get('Nom du Produit en Français') or row.get('Nom base français') or row.get('Nom technique') or ''
            name = name.lower()
            
            # Normalize CO2 value
            # Agribalyse: "Changement climatique"
            # Base Carbone: "Total poste non décomposé" or "Total"
            co2_str = (
                row.get('Changement climatique') or 
                row.get('Total poste non décomposé') or 
                row.get('Total') or 
                '0'
            )
            
            try:
                # Handle French comma decimal
                co2_val = float(co2_str.replace(',', '.'))
            except ValueError:
                continue

            # Skip incomplete data or zero
            if co2_val <= 0:
                continue
                
            row_count += 1

            for cat_code, data in categories.items():
                if any(k in name for k in data['keywords']):
                    # Filter logic to avoid bad matches
                    if 'aliment pour bétail' in name: continue
                    
                    data['sum'] += co2_val
                    data['count'] += 1
                    matches += 1

        self.stdout.write(f"Processed {row_count} valid lines from {source_name}. Found {matches} matching products.")

        # Update Database
        MEAL_WEIGHT_KG = 0.45 

        for cat_code, data in categories.items():
            if data['count'] > 0:
                avg_val_per_kg = data['sum'] / data['count']
                final_val_per_meal = avg_val_per_kg * MEAL_WEIGHT_KG
                
                obj, created = FoodEmissionFactor.objects.update_or_create(
                    code=cat_code,
                    defaults={
                        'kg_co2_per_meal': round(final_val_per_meal, 3),
                        'source': f"{source_name} (Moy. {data['count']} produits)",
                    }
                )
                self.stdout.write(self.style.SUCCESS(
                    f"Updated {cat_code}: {final_val_per_meal:.3f} kgCO2e/repas (Source: {obj.source})"
                ))
            else:
                self.stdout.write(self.style.WARNING(f"No data found for {cat_code}, skipping update."))
