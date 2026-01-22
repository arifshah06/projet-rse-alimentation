# Stack Technique - Bilan Carbone Évry
## Django Full-Stack - Architecture détaillée

**Date** : 16 janvier 2026  
**Version** : 1.0  
**Projet** : Application web interne - Bilan Carbone automatisé

---

## 🎯 Choix d'architecture

### **Django Full-Stack** ✅

Application monolithique avec templates Django intégrés, adaptée pour :
- ✅ Application interne municipale
- ✅ Équipes techniques réduites
- ✅ Maintenance long-terme
- ✅ Principes d'éco-conception
- ✅ Sécurité et conformité RGPD

---

## 📦 Technologies

### Backend

| Composant | Technologie | Version | Rôle |
|-----------|-------------|---------|------|
| **Langage** | Python | 3.11+ | Langage principal |
| **Framework** | Django | 5.0+ | Framework web full-stack |
| **Base de données** | PostgreSQL | 15+ | Stockage données |
| **ORM** | Django ORM | Intégré | Gestion BD |
| **Auth** | Django Auth | Intégré | Authentification |
| **Admin** | Django Admin | Intégré | Interface admin |
| **Forms** | Django Forms | Intégré | Validation formulaires |

### Frontend

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| **Templates** | Django Templates | Intégré, server-side rendering |
| **CSS** | Vanilla CSS | Éco-conception, pas de build |
| **JavaScript** | Vanilla ES6+ | Minimal, calculs côté client |
| **Icons** | SVG inline | Pas de dépendance externe |

### Infrastructure

| Service | Production | Développement |
|---------|-----------|---------------|
| **Serveur web** | Nginx | Django runserver |
| **Serveur app** | Gunicorn | Django runserver |
| **Base de données** | PostgreSQL | PostgreSQL (Docker) |
| **Fichiers statiques** | WhiteNoise | Django dev server |
| **Cache** | Redis (optionnel) | - |

---

## 🏗️ Structure du projet

```
webapp/
│
├── manage.py                       # Script principal Django
├── requirements.txt                # Dépendances Python
├── requirements-dev.txt            # Dépendances développement
├── .env.example                    # Template variables d'environnement
├── .gitignore                      # Git ignore
├── pytest.ini                      # Configuration pytest
├── README.md                       # Documentation projet
│
├── config/                         # Configuration Django
│   ├── __init__.py
│   ├── settings.py                # Settings principal
│   ├── settings_dev.py            # Settings développement
│   ├── settings_prod.py           # Settings production
│   ├── urls.py                    # URLs principales
│   ├── wsgi.py                    # WSGI production
│   └── asgi.py                    # ASGI (async, futur)
│
├── apps/                           # Applications Django
│   │
│   ├── core/                      # Application principale
│   │   ├── __init__.py
│   │   ├── models.py             # User, Settings
│   │   ├── views.py              # Dashboard, login
│   │   ├── forms.py              # LoginForm
│   │   ├── admin.py              # Admin config
│   │   ├── urls.py               # Routes core
│   │   ├── middleware.py         # Middlewares custom
│   │   ├── context_processors.py # Context global
│   │   └── templates/
│   │       └── core/
│   │           ├── base.html                 # Template de base
│   │           ├── dashboard.html            # Tableau de bord
│   │           ├── login.html                # Page connexion
│   │           └── components/
│   │               ├── header.html
│   │               ├── footer.html
│   │               └── nav.html
│   │
│   ├── vehicles/                  # Module véhicules
│   │   ├── __init__.py
│   │   ├── models.py             # VehicleData, EmissionFactor
│   │   ├── views.py              # FormView, ListView
│   │   ├── forms.py              # VehicleFuelForm, VehicleDistanceForm
│   │   ├── admin.py              # Admin véhicules
│   │   ├── urls.py               # Routes module
│   │   ├── managers.py           # Custom managers
│   │   ├── utils.py              # Calculateurs CO2
│   │   ├── migrations/           # Migrations BD
│   │   └── templates/
│   │       └── vehicles/
│   │           ├── form.html              # Formulaire saisie
│   │           ├── list.html              # Liste données
│   │           ├── detail.html            # Détail
│   │           └── components/
│   │               ├── fuel_card.html
│   │               └── impact_display.html
│   │
│   ├── buildings/                 # Module bâtiments (futur)
│   │   ├── models.py             # BuildingData, EnergyConsumption
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── templates/
│   │
│   ├── alimentation/              # Module alimentation (futur)
│   │   ├── models.py             # MealData
│   │   └── ...
│   │
│   └── achats/                    # Module achats (futur)
│       ├── models.py             # PurchaseData
│       └── ...
│
├── static/                         # Fichiers statiques
│   ├── css/
│   │   ├── base.css              # Styles de base (reset, variables)
│   │   ├── layout.css            # Layout (grid, container)
│   │   ├── components.css        # Composants réutilisables
│   │   ├── forms.css             # Styles formulaires
│   │   └── modules/
│   │       ├── vehicles.css      # Styles module véhicules
│   │       ├── buildings.css
│   │       └── dashboard.css
│   │
│   ├── js/
│   │   ├── main.js               # JS principal
│   │   ├── vehicle-calculator.js # Calculateur véhicules
│   │   ├── form-validator.js     # Validation formulaires
│   │   └── utils.js              # Utilitaires
│   │
│   └── img/
│       ├── logo.svg
│       └── icons/
│           └── (SVG icons)
│
├── templates/                      # Templates globaux
│   ├── base.html                  # Template racine
│   ├── 404.html                   # Page 404
│   ├── 500.html                   # Page 500
│   └── emails/                    # Templates emails
│       └── notification.html
│
├── media/                          # Fichiers uploadés (git-ignored)
│   └── uploads/
│
└── tests/                          # Tests
    ├── conftest.py                # Configuration pytest
    ├── factories.py               # Factories pour tests
    └── test_vehicles/
        ├── test_models.py
        ├── test_views.py
        └── test_forms.py
```

---

## 📋 Modèles de données

### Application Vehicles

```python
# apps/vehicles/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class EmissionFactor(models.Model):
    """Facteurs d'émission ADEME"""
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('fuel', 'Carburant'),
        ('vehicle_km', 'Véhicule par km'),
    ])
    unit = models.CharField(max_length=20)  # 'L', 'km'
    factor_value = models.DecimalField(
        max_digits=10, 
        decimal_places=6,
        help_text="kg CO₂e par unité"
    )
    source = models.CharField(max_length=200, default="ADEME Base Carbone")
    verified_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Facteur d'émission"
        verbose_name_plural = "Facteurs d'émission"
    
    def __str__(self):
        return f"{self.name} ({self.factor_value} kg CO₂e/{self.unit})"


class VehicleData(models.Model):
    """Données de consommation véhicules"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField(default=2024)
    service = models.CharField(max_length=100, blank=True)
    
    # Méthode par carburant
    essence_liters = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        verbose_name="Essence (litres)"
    )
    gazole_liters = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        verbose_name="Gazole (litres)"
    )
    
    # Méthode par distance
    distance_km = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        verbose_name="Distance (km)"
    )
    
    # Résultats
    total_co2_kg = models.DecimalField(
        max_digits=12, 
        decimal_places=3,
        null=True,
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Donnée véhicule"
        verbose_name_plural = "Données véhicules"
        ordering = ['-created_at']
    
    def calculate_impact(self):
        """Calcule l'impact carbone total"""
        from .utils import calculate_fuel_impact
        
        self.total_co2_kg = calculate_fuel_impact(
            essence_liters=self.essence_liters or 0,
            gazole_liters=self.gazole_liters or 0
        )
        return self.total_co2_kg
    
    def save(self, *args, **kwargs):
        self.calculate_impact()
        super().save(*args, **kwargs)
```

---

## 🔧 Configuration

### requirements.txt

```txt
# Core
Django==5.0.1
python-decouple==3.8
django-environ==0.11.2

# Database
psycopg2-binary==2.9.9

# Production
gunicorn==21.2.0
whitenoise==6.6.0

# Development (requirements-dev.txt)
# pytest==7.4.3
# pytest-django==4.7.0
# black==23.12.1
# ruff==0.1.9
```

### settings.py

```python
# config/settings.py

import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Apps locales
    'apps.core',
    'apps.vehicles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Internationalisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---

## 🚀 Déploiement

### Développement

```bash
# 1. Cloner le repo
git clone https://github.com/Shazbg/Eco-Dashboard-Evry.git
cd webapp

# 2. Créer environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Installer dépendances
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. Configurer variables
cp .env.example .env
# Éditer .env avec vos valeurs

# 5. Créer base de données PostgreSQL
createdb evry_bilan_carbone

# 6. Migrations
python manage.py makemigrations
python manage.py migrate

# 7. Créer superuser
python manage.py createsuperuser

# 8. Charger données de référence (facteurs ADEME)
python manage.py loaddata emission_factors

# 9. Lancer serveur
python manage.py runserver
```

### Production

```bash
# Collecter fichiers statiques
python manage.py collectstatic --no-input

# Lancer avec Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

---

## ✅ Avantages de cette stack

| Critère | Bénéfice |
|---------|----------|
| **Simplicité** | Un seul langage (Python), stack cohérente |
| **Productive** | Django Admin, Forms, Auth intégrés |
| **Sécurisé** | Protection CSRF, XSS, injection SQL par défaut |
| **Maintenable** | Code Python lisible, documentation FR |
| **Éco-responsable** | Pas de build npm, server-side rendering |
| **Évolutif** | Facile d'ajouter modules (buildings, etc.) |
| **Standard** | Utilisé par admin publiques françaises |

---

## 📚 Ressources

- **Django Documentation** : https://docs.djangoproject.com/fr/5.0/
- **PostgreSQL** : https://www.postgresql.org/docs/
- **Python** : https://docs.python.org/fr/3/
- **ADEME Base Carbone** : https://base-empreinte.ademe.fr/

---

*Document créé le 16 janvier 2026 - Stack technique validée*
