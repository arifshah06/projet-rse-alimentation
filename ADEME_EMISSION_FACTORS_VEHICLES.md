# Facteurs d'Émission ADEME - Secteur Véhicules
## Base Carbone® ADEME - Données officielles 2024

---

## 📊 Sources

- **Base Carbone ADEME** : Base de données publique officielle
- **API Impact CO₂** : https://impactco2.fr/doc/api
- **Référence légale** : Article 75 de la loi Grenelle II
- **Dernière consultation** : Janvier 2026

---

## ⛽ Carburants - Facteurs d'émission par litre

### Valeurs ADEME officielles (kg CO₂e/L)

| Carburant | Facteur (kg CO₂e/L) | Périmètre | Source |
|-----------|---------------------|-----------|---------|
| **Essence (SP 95-98)** | **2.79** | Combustion + Amont* | ADEME Base Carbone |
| **Gazole routier** | **3.17** | Combustion + Amont* | ADEME Base Carbone |
| **Gazole non routier** | **3.17** | Combustion + Amont* | ADEME Base Carbone |

\* **Amont** = Production, raffinage, transport et distribution du carburant

### ⚠️ Comparaison avec vos données actuelles

| Carburant | Vos données Excel | ADEME 2024 | Écart | Observation |
|-----------|-------------------|------------|-------|-------------|
| Essence | 2.28 kg/L | **2.79 kg/L** | **-18%** | ⚠️ Sous-estimé (combustion seule?) |
| Gasoil | 2.67 kg/L | **3.17 kg/L** | **-16%** | ⚠️ Sous-estimé (combustion seule?) |

**Recommandation** : Utiliser les valeurs ADEME **2.79** et **3.17** pour un bilan conforme et complet (scope 1+3).

---

## 🚗 Véhicules - Facteurs d'émission par kilomètre

### Données Impact CO₂ API (kg CO₂e/km)

#### Véhicules particuliers

| Type de véhicule | Facteur (kg CO₂e/km) | ID API | Usage |
|------------------|----------------------|--------|-------|
| **Voiture thermique** | **0.192** | 4 | Essence/Diesel moyenne |
| **Voiture électrique** | **0.0198** | 5 | Incluant production électricité France |
| Covoiturage thermique (1 passager) | 0.096 | 22 | 2 personnes total |
| Covoiturage thermique (2 passagers) | 0.064 | 23 | 3 personnes total |
| Covoiturage thermique (3 passagers) | 0.048 | 24 | 4 personnes total |
| Covoiturage thermique (4 passagers) | 0.038 | 25 | 5 personnes total |
| Covoiturage électrique (1 passager) | 0.0099 | 26 | 2 personnes total |
| Covoiturage électrique (2 passagers) | 0.0066 | 27 | 3 personnes total |
| Covoiturage électrique (3 passagers) | 0.00495 | 28 | 4 personnes total |
| Covoiturage électrique (4 passagers) | 0.00396 | 29 | 5 personnes total |

#### Deux-roues motorisés

| Type | Facteur (kg CO₂e/km) | ID API |
|------|----------------------|--------|
| **Scooter/moto légère thermique** | **0.0604** | 12 |

#### Transports en commun

| Type | Facteur (kg CO₂e/km) | ID API | Notes |
|------|----------------------|--------|-------|
| **Bus thermique** | **0.1135** | 9 | Par passager |
| **Bus électrique** | **0.0095** | 16 | Par passager |
| **Bus GNV** | **0.1128** | 21 | Gaz naturel par passager |
| Tramway | 0.0038 | 10 | Par passager |
| Métro | 0.0042 | 11 | Par passager |
| TER | 0.0229 | 15 | Par passager |

#### Mobilités douces

| Type | Facteur (kg CO₂e/km) | ID API | Notes |
|------|----------------------|--------|-------|
| Marche | 0 | 30 | Zéro émission |
| Vélo mécanique | 0 | 7 | Zéro émission |
| Vélo à assistance électrique | 0.00223 | 8 | Production électricité |
| Trottinette électrique | 0.002 | 17 | Production + recharge |

---

## 🔄 Conversion : Litres ↔ Kilomètres

Pour passer d'une consommation en litres à un impact par kilomètre parcouru :

### Formule
```
Impact (kg CO₂) = Consommation (L) × Facteur carburant (kg CO₂/L)
```

OU si km connus :
```
Impact (kg CO₂) = Distance (km) × Facteur véhicule (kg CO₂/km)
```

### Exemple pratique - Véhicule essence

**Données :**
- Consommation annuelle : 1000 L d'essence
- Distance parcourue : 15 000 km
- Consommation moyenne : 1000L / 15000km = **6.67 L/100km**

**Calcul 1 - Par carburant :**
```
Impact = 1000 L × 2.79 kg CO₂/L = 2 790 kg CO₂
```

**Calcul 2 - Par kilomètre (voiture thermique moyenne) :**
```
Impact = 15 000 km × 0.192 kg CO₂/km = 2 880 kg CO₂
```

**Écart** : ~3% (différence due au fait que 0.192 est une moyenne tous carburants)

---

## 📋 Modèle de collecte des données

### Option 1 : Saisie par véhicule (détaillée)

Pour chaque véhicule de la flotte :

```python
{
    "immatriculation": "AB-123-CD",
    "type_vehicule": "Voiture",
    "motorisation": "Thermique",  # Thermique, Électrique, Hybride
    "carburant": "Essence",       # Essence, Gazole, Électrique, GNV
    "consommation_annuelle": {
        "essence_litres": 850,
        "gasoil_litres": 0,
        "distance_km": 12000
    },
    "service": "Services techniques"
}
```

**Calcul impact :**
```python
impact_carburant = (essence_L × 2.79) + (gasoil_L × 3.17)
# OU
impact_distance = distance_km × facteur_type_vehicule
```

### Option 2 : Saisie globale par carburant (simplifiée)

Pour l'ensemble de la flotte :

```python
{
    "annee": 2024,
    "total_essence_litres": 15000,
    "total_gasoil_litres": 8000,
    "total_distance_km": 250000  # Optionnel
}
```

**Calcul impact total :**
```python
impact_total = (15000 × 2.79) + (8000 × 3.17)
            = 41 850 + 25 360
            = 67 210 kg CO₂
            = 67.21 tonnes CO₂e
```

---

## 🎯 Recommandations pour l'application

### 1. Stockage en base de données

**Table `emission_factors_vehicles`**
```sql
CREATE TABLE emission_factors_vehicles (
    id SERIAL PRIMARY KEY,
    category VARCHAR(50),           -- 'carburant', 'vehicule_km'
    subcategory VARCHAR(100),       -- 'essence', 'gasoil', 'voiture_thermique', etc.
    unit VARCHAR(20),               -- 'L', 'km'
    factor_value DECIMAL(10, 6),    -- Valeur du facteur
    co2e_per_unit DECIMAL(10, 6),  -- kg CO₂e par unité
    source VARCHAR(100),            -- 'ADEME Base Carbone 2024'
    source_url TEXT,
    api_id INTEGER,                 -- ID dans API Impact CO₂ (si applicable)
    valid_from DATE,
    valid_to DATE,
    scope VARCHAR(50),              -- 'Scope 1', 'Scope 1+3'
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

**Données initiales à insérer :**
```sql
-- CARBURANTS
INSERT INTO emission_factors_vehicles (category, subcategory, unit, co2e_per_unit, source, scope, notes) VALUES
('carburant', 'essence_sp95_98', 'L', 2.79, 'ADEME Base Carbone 2024', 'Scope 1+3', 'Combustion + amont'),
('carburant', 'gasoil_routier', 'L', 3.17, 'ADEME Base Carbone 2024', 'Scope 1+3', 'Combustion + amont'),
('carburant', 'gasoil_non_routier', 'L', 3.17, 'ADEME Base Carbone 2024', 'Scope 1+3', 'Combustion + amont');

-- VÉHICULES PAR KM
INSERT INTO emission_factors_vehicles (category, subcategory, unit, co2e_per_unit, source, api_id) VALUES
('vehicule_km', 'voiture_thermique', 'km', 0.192, 'API Impact CO₂', 4),
('vehicule_km', 'voiture_electrique', 'km', 0.0198, 'API Impact CO₂', 5),
('vehicule_km', 'bus_thermique', 'km', 0.1135, 'API Impact CO₂', 9),
('vehicule_km', 'bus_electrique', 'km', 0.0095, 'API Impact CO₂', 16),
('vehicule_km', 'scooter_moto_legere', 'km', 0.0604, 'API Impact CO₂', 12);
```

### 2. Interface de saisie - Choix de méthode

**Écran initial du module Véhicules :**
```
┌─────────────────────────────────────────────────────┐
│  🚗 VÉHICULES - Méthode de calcul                   │
├─────────────────────────────────────────────────────┤
│  Choisissez votre méthode de saisie :               │
│                                                     │
│  ○ Méthode 1 : Consommation par carburant          │
│    └─ Saisir les litres d'essence et gasoil        │
│       consommés sur l'année                        │
│    └─ ✅ Rapide et simple                          │
│    └─ ✅ Facteurs ADEME officiels (2.79 / 3.17)   │
│                                                     │
│  ○ Méthode 2 : Distance parcourue                  │
│    └─ Saisir les km parcourus par type vehicle    │
│    └─ ⚠️  Moins précis (valeurs moyennes)          │
│                                                     │
│  ○ Méthode 3 : Inventaire détaillé de la flotte   │
│    └─ Saisir chaque véhicule avec ses données     │
│    └─ ✅ Le plus précis                            │
│    └─ ⏱️  Plus long à remplir                       │
│                                                     │
│  [Continuer]                                        │
└─────────────────────────────────────────────────────┘
```

### 3. Calculs automatiques

**Backend Python (exemple) :**
```python
# Facteurs ADEME
FACTEUR_ESSENCE = 2.79  # kg CO₂e/L
FACTEUR_GASOIL = 3.17   # kg CO₂e/L

def calculate_vehicle_emissions(data):
    """
    Calcule les émissions selon la méthode choisie
    """
    if data['method'] == 'carburant':
        essence = data.get('essence_litres', 0)
        gasoil = data.get('gasoil_litres', 0)
        
        impact_essence = essence * FACTEUR_ESSENCE
        impact_gasoil = gasoil * FACTEUR_GASOIL
        
        return {
            'total_kg_co2e': impact_essence + impact_gasoil,
            'detail': {
                'essence': impact_essence,
                'gasoil': impact_gasoil
            },
            'source': 'ADEME Base Carbone 2024'
        }
    
    elif data['method'] == 'distance':
        # Utiliser les facteurs par km
        distance = data.get('distance_km', 0)
        type_vehicule = data.get('type_vehicule', 'voiture_thermique')
        
        # Récupérer le facteur depuis la DB
        facteur = get_emission_factor(type_vehicule)
        
        return {
            'total_kg_co2e': distance * facteur,
            'detail': {
                'distance_km': distance,
                'facteur_km': facteur
            },
            'source': 'API Impact CO₂'
        }
```

### 4. Validation et cohérence

**Vérifications automatiques :**
- Si consommation ET distance saisies → comparer les 2 méthodes
- Alerte si consommation moyenne aberrante (< 3L/100km ou > 15L/100km)
- Alerte si écart > 20% entre les 2 méthodes

```python
def validate_consistency(essence_L, gasoil_L, distance_km):
    """
    Vérifie la cohérence entre consommation et distance
    """
    if distance_km > 0:
        conso_moyenne = ((essence_L + gasoil_L) / distance_km) * 100
        
        if conso_moyenne < 3 or conso_moyenne > 15:
            return {
                'warning': True,
                'message': f"Consommation moyenne de {conso_moyenne:.1f}L/100km semble inhabituelle"
            }
    
    return {'warning': False}
```

---

## 📡 Intégration API Impact CO₂

### Endpoint de base
```
GET https://impactco2.fr/api/v1/transport?km=1
```

### Exemple Python d'intégration

```python
import requests

def get_vehicle_emission_factors():
    """
    Récupère les facteurs d'émission depuis l'API Impact CO₂
    """
    url = "https://impactco2.fr/api/v1/transport"
    params = {"km": 1}  # Pour avoir le facteur par km
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Mapper les données
        factors = {}
        for item in data['data']:
            factors[item['id']] = {
                'name': item['name'],
                'value': item['value'],  # kg CO₂e/km
            }
        
        return factors
    
    return None

# Utilisation
factors = get_vehicle_emission_factors()
voiture_thermique_factor = factors[4]['value']  # 0.192 kg CO₂e/km
```

**⚠️ Note de l'API :**
> "La requête n'est pas authentifiée. Nous nous réservons le droit de couper cette API aux utilisateurs anonymes, veuillez nous contacter à impactco2@ademe.fr pour obtenir une clé d'API gratuite."

**Recommandation** : Demander une clé API gratuite pour sécuriser l'accès.

---

## ✅ Checklist d'implémentation

### Phase 1 : Configuration
- [ ] Créer la table `emission_factors_vehicles`
- [ ] Insérer les facteurs ADEME de référence
- [ ] Demander une clé API Impact CO₂ (optionnel mais recommandé)

### Phase 2 : Backend
- [ ] Créer les fonctions de calcul par méthode
- [ ] Implémenter la validation de cohérence
- [ ] Créer les endpoints API pour récupérer les facteurs
- [ ] Tester les calculs avec données de référence

### Phase 3 : Frontend
- [ ] Interface de choix de méthode
- [ ] Formulaire méthode carburant (simple)
- [ ] Formulaire méthode distance
- [ ] Formulaire inventaire flotte (détaillé)
- [ ] Affichage temps réel de l'impact calculé
- [ ] Alertes de cohérence

### Phase 4 : Validation
- [ ] Comparer résultats avec bilan existant
- [ ] Valider avec un échantillon de données réelles
- [ ] Documenter les choix méthodologiques

---

## 📚 Références

1. **Base Carbone ADEME**
   - https://base-empreinte.ademe.fr/

2. **API Impact CO₂**
   - https://impactco2.fr/doc/api
   - Contact : impactco2@ademe.fr

3. **Documentation ADEME Bilan GES**
   - https://www.bilans-ges.ademe.fr/

4. **Facteurs carburants (source gouvernementale)**
   - https://ecologie.gouv.fr (facteurs officiels 2024)

5. **Open Data ADEME**
   - https://data.ademe.fr/

---

## 🎯 Résumé des valeurs clés à utiliser

### Pour la flotte municipale d'Évry-Courcouronnes

| Poste | Valeur ADEME | Unité | À utiliser dans l'app |
|-------|--------------|-------|------------------------|
| **Essence (SP 95-98)** | **2.79** | kg CO₂e/L | ✅ OUI - Valeur de référence |
| **Gazole routier** | **3.17** | kg CO₂e/L | ✅ OUI - Valeur de référence |
| Voiture thermique | 0.192 | kg CO₂e/km | ⚠️ Optionnel (méthode alternative) |
| Voiture électrique | 0.0198 | kg CO₂e/km | ⚠️ Optionnel (si flotte électrique) |
| Bus thermique | 0.1135 | kg CO₂e/km | ⚠️ Optionnel (transport usagers) |

**Méthode prioritaire recommandée** : Consommation en litres (essence + gasoil) avec facteurs **2.79** et **3.17**.

---

*Document généré le 16 janvier 2026 - À mettre à jour lors des nouvelles versions de la Base Carbone*
