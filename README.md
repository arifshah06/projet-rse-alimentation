# Bilan Carbone - Mairie d'Évry-Courcouronnes

Application web interne pour la construction automatisée du bilan carbone municipal.

## 📋 Description

Cette application Django permet aux différents services de la mairie de saisir leurs données de consommation (véhicules, bâtiments, alimentation, achats) et de calculer automatiquement l'impact carbone avec les facteurs d'émission officiels ADEME.

## 🛠️ Stack Technique

- **Backend** : Django 6.0.1
- **Base de données** : PostgreSQL 15+
- **Frontend** : Django Templates + Vanilla CSS + JavaScript ES6
- **Serveur** : Gunicorn + Nginx (production)

## 🚀 Installation

### Prérequis

- Python 3.12+
- PostgreSQL 15+
- Git

### Étapes

```bash
# 1. Cloner le repository
git clone https://github.com/Shazbg/Eco-Dashboard-Evry.git
cd webapp

# 2. Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos valeurs

# 5. Créer la base de données PostgreSQL
createdb evry_bilan_carbone

# 6. Appliquer les migrations
python manage.py migrate

# 7. Créer un superutilisateur
python manage.py createsuperuser

# 8. Lancer le serveur de développement
python manage.py runserver
```

L'application sera accessible sur http://127.0.0.1:8000

## 📂 Structure du projet

```
webapp/
├── manage.py              # Script Django principal
├── requirements.txt       # Dépendances
├── config/                # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/                  # Applications Django
│   ├── core/             # App principale (auth, dashboard)
│   └── vehicles/         # Module véhicules
├── static/                # Fichiers statiques (CSS, JS, images)
├── templates/             # Templates Django globaux
└── venv/                  # Environnement virtuel (git-ignored)
```

## 🎯 Modules

### Module Véhicules (En cours)
- Saisie consommation carburant (essence, gazole)
- Calcul automatique émissions CO₂
- Facteurs ADEME : 2.79 kg CO₂e/L (essence), 3.16 kg CO₂e/L (gazole)

### Modules à venir
- Bâtiments & Énergies
- Alimentation
- Achats

## 📊 Données ADEME

Les facteurs d'émission sont issus de la **Base Carbone® ADEME** (version vérifiée janvier 2026).

Documentation : [ADEME_VERIFIED_VALUES.md](ADEME_VERIFIED_VALUES.md)

## 🧪 Tests

```bash
# Lancer les tests
pytest

# Avec couverture
pytest --cov=apps
```

## 📝 Licence

Projet interne - Mairie d'Évry-Courcouronnes

---

**Éco-conçu avec ❤️ pour la transition écologique**

