# Spécifications Front-End - Bilan Carbone Automatisé
## Application Web Interne - Mairie d'Évry-Courcouronnes

---

## 📋 Vue d'ensemble

L'application permettra aux agents de chaque service municipal de saisir leurs données de consommation pour construire le bilan carbone de la ville. L'interface doit être **simple, éco-responsable et intuitive**.

---

## 🎯 Objectifs du Front-End

1. **Saisie par secteur** : Interface modulaire adaptée à 4 secteurs principaux
2. **Simplicité** : Design épuré, formulaires clairs et guidés
3. **Éco-conception** : CSS minimal, pas de frameworks lourds, optimisation des ressources
4. **Accessibilité** : Utilisable par tous les agents, peu importe leur niveau technique

---

## 📊 Structure des Modules par Secteur

### **1. Module ALIMENTATION (12%)**

#### Données à collecter :
- **Types de repas** :
  - Repas adultes
  - Repas petite enfance
  - Repas scolaires
  - Repas froids

- **Par type de repas** :
  - Catégorie alimentaire (référence)
    - Végétarien (0.51 kg CO2/repas)
    - Dominante poulet/poisson (1.5 kg CO2/repas)
    - Dominante bœuf (7.26 kg CO2/repas)
    - Dominante porc (~2 kg CO2/repas)
  
- **Détail par catégorie (2024)** :
  - Nombre de repas Bœuf/Veau par semaine
  - Nombre de repas Porc par semaine
  - Nombre de repas Poisson/Volaille par semane
  - Nombre de repas Végétarien par semaine
  - Répartition : petite enfance / scolaire / adulte

#### Interface suggérée :
```
┌─────────────────────────────────────────────┐
│  📋 ALIMENTATION - Saisie des repas         │
├─────────────────────────────────────────────┤
│  Année de référence : [2024 ▼]             │
│                                             │
│  Nombre total de repas 2024 :               │
│  ┌─────────────────────────────────────┐   │
│  │ Petite enfance : [_______]          │   │
│  │ Scolaire + CLS : [_______]          │   │
│  │ Adultes Sco+CLS: [_______]          │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  Répartition par type (repas/semaine) :    │
│  ┌─────────────────────────────────────┐   │
│  │ 🥩 Bœuf/Veau      : [___] /semaine  │   │
│  │ 🥓 Porc           : [___] /semaine  │   │
│  │ 🐔 Poisson/Volaille: [___] /semaine │   │
│  │ 🥗 Végétarien     : [___] /semaine  │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  [Calculer l'impact] [Sauvegarder]         │
└─────────────────────────────────────────────┘
```

---

### **2. Module VÉHICULES (Flotte municipale)**

#### Données à collecter :

**Pour chaque véhicule** :
- Immatriculation
- Modèle (voiture, utilitaire, camion, véhicule d'entretien)
- Poids à vide (tonnes)
- Année de construction/acquisition
- Durée d'amortissement (5 ans par défaut)
- Direction/service d'affectation
- Motorisation (thermique, électrique, hybride)
- Chevaux fiscaux

**Consommations annuelles** :
- Essence (ES) en litres → Impact : **2.79 kg CO₂e/L** (ADEME Base Carbone)
- Gasoil (GO) en litres → Impact : **3.16 kg CO₂e/L** (ADEME Base Carbone)
- Distance parcourue annuellement (km)

#### Interface suggérée :
```
┌─────────────────────────────────────────────────────────────┐
│  🚗 VÉHICULES - Gestion de la flotte                        │
├─────────────────────────────────────────────────────────────┤
│  Année : [2024 ▼]  Direction : [____________ ▼]            │
│                                                             │
│  Liste des véhicules :                                      │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ Immat.     Modèle       Motorisation    [Actions]    │ │
│  │ AB-123-CD  Renault...   Diesel          [✏️] [🗑️]   │ │
│  │ EF-456-GH  Peugeot...   Électrique      [✏️] [🗑️]   │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  [+ Ajouter un véhicule]                                   │
│                                                             │
│  OU Saisie globale par carburant :                         │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ Total Essence 2024  : [________] litres               │ │
│  │ Total Gasoil 2024   : [________] litres               │ │
│  │ Impact calculé : _____ kg CO2                         │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  [Sauvegarder]                                             │
└─────────────────────────────────────────────────────────────┘
```

**Formulaire d'ajout véhicule** :
```
┌─────────────────────────────────────────────┐
│  Immatriculation      : [__________]        │
│  Modèle               : [__________]        │
│  Type                 : [Voiture ▼]         │
│  Poids à vide (tonnes): [__________]        │
│  Année acquisition    : [2020 ▼]           │
│  Motorisation         : [Diesel ▼]          │
│  Chevaux fiscaux      : [__________]        │
│  Service              : [__________ ▼]      │
│                                             │
│  Consommation 2024:                         │
│  • Essence (L)  : [__________]              │
│  • Gasoil (L)   : [__________]              │
│  • Distance (km): [__________]              │
│                                             │
│  [Annuler]  [Enregistrer]                  │
└─────────────────────────────────────────────┘
```

---

### **3. Module BÂTIMENTS & ÉNERGIES (12%)**

#### Données à collecter :

**Pour chaque site/bâtiment** :
- Nom du site
- Surface (m²) - Information essentielle
- Année de construction (ou période)
- Direction ou service utilisateur
- Remarques/précisions

**Consommations d'énergie 2024** :
- **Électricité** (kWh) → Impact : 0.052 kg CO2/kWh
- **Gaz naturel** (kWh PCI ou L) → Impact : 0.24 kg CO2/kWh
- **Chaleur réseau** (kWh) → Impact : 0.146 kg CO2/kWh
- **Climatisation** (puissance installée en kW)
- **Production d'électricité** (filière et énergie en kWh)

#### Interface suggérée :
```
┌─────────────────────────────────────────────────────────────┐
│  🏢 BÂTIMENTS - Inventaire patrimoine                       │
├─────────────────────────────────────────────────────────────┤
│  Année : [2024 ▼]                                           │
│                                                             │
│  Liste des sites :                                          │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ Site                  Surface   Service    [Actions]  │ │
│  │ Mairie principale     1200 m²   Admin      [✏️] [📊]│ │
│  │ Gymnase A. Thoison    800 m²    Sports     [✏️] [📊]│ │
│  │ Crèche F. Dolto       500 m²    Enfance    [✏️] [📊]│ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  [+ Ajouter un bâtiment]                                   │
└─────────────────────────────────────────────────────────────┘
```

**Formulaire détail bâtiment** :
```
┌─────────────────────────────────────────────────────┐
│  🏢 Site : [Nom du bâtiment_______________]        │
├─────────────────────────────────────────────────────┤
│  Informations générales :                          │
│  • Surface (m²)        : [__________] *obligatoire │
│  • Année construction  : [__________]              │
│  • Service utilisateur : [__________ ▼]            │
│  • Consommation/m²     : [__________]              │
│                                                     │
│  Consommations 2024 :                              │
│  ┌─────────────────────────────────────────────┐   │
│  │ ⚡ Électricité      : [______] kWh         │   │
│  │                      Impact: _____ kg CO2  │   │
│  │                                             │   │
│  │ 🔥 Gaz naturel      : [______] kWh (PCI)   │   │
│  │                      Impact: _____ kg CO2  │   │
│  │                                             │   │
│  │ 🌡️  Chaleur réseau   : [______] kWh         │   │
│  │                      Impact: _____ kg CO2  │   │
│  │                                             │   │
│  │ ❄️  Climatisation    : [______] kW          │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  Production d'électricité :                        │
│  • Filière : [Photovoltaïque ▼]                   │
│  • Énergie : [__________] kWh                      │
│                                                     │
│  Précisions : [_____________________________]      │
│                                                     │
│  [Annuler]  [Calculer impact]  [Sauvegarder]      │
└─────────────────────────────────────────────────────┘
```

---

### **4. Module ACHATS (30%)**

#### Données à collecter :

**Services** (avec facteur d'émission en kg CO2/k€) :
- Restauration scolaire
- Travaux PPI
- Travaux investissements courants (360 kg CO2/k€)
- Nettoiement voirie (215 kg CO2/k€)
- Entretien espaces verts (215 kg CO2/k€)
- Nettoyage offices restauration (215 kg CO2/k€)
- Assurances (110 kg CO2/k€)
- etc.

**Fournitures** (par catégorie) :
- Électricité/Gaz
- Chauffage
- Carburant
- Végétaux, arbres, fleurs
- Eau et assainissement
- Location copieurs
- Fournitures petit équipement
- Équipements offices restauration
- Fournitures scolaires
- etc.

**Équipements** :
- Matériel de bureau et informatique
- Véhicules
- Mobilier de bureau
- Mobilier scolaire
- Mobilier offices restauration

**Produits** :
- Produits d'entretien
- Produits consommables

**Pour chaque ligne** :
- Catégorie (Service/Fourniture/Équipement/Produit)
- Désignation
- Facteur d'émission (kg CO2/k€)
- Montant 2024 (€)
- Impact calculé (kg CO2)
- Service concerné (optionnel)
- Précisions supplémentaires

#### Interface suggérée :
```
┌─────────────────────────────────────────────────────────────┐
│  🛒 ACHATS - Saisie des dépenses                            │
├─────────────────────────────────────────────────────────────┤
│  Année : [2024 ▼]   Service : [Tous ▼]                     │
│                                                             │
│  Catégorie : [○ Services ○ Fournitures ○ Équipements]      │
│                                                             │
│  [Rechercher : _______________] [🔍]                        │
│                                                             │
│  Marchés importants :                                       │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ Désignation              Impact    Montant   Actions  │ │
│  │ Travaux investissements  360 kg/k€ [____€] [✏️] [🗑️]│ │
│  │ Nettoiement voirie       215 kg/k€ [____€] [✏️] [🗑️]│ │
│  │ Entretien espaces verts  215 kg/k€ [____€] [✏️] [🗑️]│ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  [+ Ajouter une ligne]                                     │
│                                                             │
│  Total impact estimé : __________ kg CO2                   │
│  [Sauvegarder]                                             │
└─────────────────────────────────────────────────────────────┘
```

**Formulaire d'ajout/modification** :
```
┌─────────────────────────────────────────────────────┐
│  Catégorie    : [○ Service ○ Fourniture            │
│                  ○ Équipement ○ Produit]           │
│                                                     │
│  Désignation  : [__________________________]       │
│                 ou [Liste déroulante ▼]            │
│                                                     │
│  Facteur CO2  : [_______] kg CO2/k€                │
│  Montant 2024 : [_______] €                        │
│                                                     │
│  Service      : [____________ ▼] (optionnel)       │
│  Structure    : [____________ ▼] (optionnel)       │
│                                                     │
│  Précisions   : [__________________________]       │
│                                                     │
│  Impact calculé : _____ kg CO2                     │
│                                                     │
│  [Annuler]  [Enregistrer]                         │
└─────────────────────────────────────────────────────┘
```

---

## 🎨 Principes de Design

### Éco-conception
- **CSS Vanilla** : Pas de framework CSS lourd (Tailwind OK si version minimale)
- **JavaScript minimal** : Calculs côté client limités, validation simple
- **Images optimisées** : SVG pour les icônes, compression
- **Polices système** : Éviter Google Fonts si possible
- **Dark mode** : Optionnel mais économe en énergie (OLED)

### Palette de couleurs suggérée
```css
/* Thème clair éco-responsable */
:root {
  --primary: #2d6a4f;      /* Vert forêt - écologie */
  --secondary: #52796f;    /* Vert gris - neutre */
  --accent: #95d5b2;       /* Vert menthe - interactions */
  --warning: #f77f00;      /* Orange - alertes */
  --bg-main: #f8f9fa;      /* Gris très clair - fond */
  --bg-card: #ffffff;      /* Blanc - cartes */
  --text-dark: #212529;    /* Noir doux - texte */
  --text-light: #6c757d;   /* Gris - secondaire */
  --border: #dee2e6;       /* Bordures légères */
}
```

### Composants réutilisables

#### 1. **Header / Navigation**
```
┌─────────────────────────────────────────────────────┐
│  🌱 Bilan Carbone - Évry              👤 [Agent]   │
├─────────────────────────────────────────────────────┤
│  [🏠 Accueil] [📋 Secteurs ▼] [📊 Tableau de bord] │
└─────────────────────────────────────────────────────┘
```

#### 2. **Card module** (pour chaque secteur)
```
┌─────────────────────────────────────┐
│  🍽️  ALIMENTATION                   │
│  ────────────────────────────────   │
│  Représente 12% du bilan            │
│                                     │
│  Dernière saisie : 15/12/2024       │
│  Impact actuel : 1 234 kg CO2       │
│                                     │
│  [📝 Saisir les données]            │
└─────────────────────────────────────┘
```

#### 3. **Feedback visuel**
- Calcul en temps réel de l'impact CO2
- Barres de progression par secteur
- Badges de statut (✅ Complété, ⚠️ Incomplet, ❌ Non démarré)

#### 4. **Validation**
- Champs obligatoires clairement indiqués (*)
- Messages d'erreur explicites
- Confirmation avant suppression

---

## 📱 Responsive Design

### Desktop (≥1024px)
- Navigation latérale
- Formulaires sur 2 colonnes
- Tableaux complets

### Tablet (768px - 1023px)
- Navigation en haut
- Formulaires sur 1 colonne
- Tableaux scrollables horizontalement

### Mobile (≤767px)
- Menu hamburger
- Formulaires simplifiés
- Cartes empilées

---

## 🔐 Authentification & Rôles

### Page de connexion
```
┌─────────────────────────────────┐
│   🌱 Bilan Carbone              │
│   Mairie d'Évry-Courcouronnes   │
│                                 │
│   Email     : [______________]  │
│   Mot de passe: [______________]│
│                                 │
│   [Se connecter]                │
│                                 │
│   Mot de passe oublié ?         │
└─────────────────────────────────┘
```

### Rôles utilisateurs
1. **Agent** : Saisie pour son service uniquement
2. **Responsable de service** : Validation et vue d'ensemble du service
3. **Administrateur** : Accès complet, gestion utilisateurs, exports

---

## 📊 Tableau de bord

### Vue d'ensemble (Accueil après connexion)
```
┌─────────────────────────────────────────────────────────┐
│  Bonjour [Prénom Agent] 👋                              │
│  Service : [Nom du service]                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Progression globale du bilan carbone 2024              │
│  ████████████░░░░░░░░░░░░  48%                         │
│                                                         │
│  Par secteur :                                          │
│  ┌──────────────┬──────────────┬──────────────┬────┐   │
│  │ 🍽️ Aliment.  │ 🚗 Véhicules │ 🏢 Bâtiments │... │   │
│  │ ✅ 100%      │ ⚠️ 75%       │ ❌ 0%        │    │   │
│  │ 1234 kg CO2  │ 5678 kg CO2  │ - kg CO2     │    │   │
│  │ [Voir]       │ [Voir]       │ [Saisir]     │    │   │
│  └──────────────┴──────────────┴──────────────┴────┘   │
│                                                         │
│  Impact total estimé : 45 678 kg CO2                   │
│                                                         │
│  [📥 Exporter les données]  [📊 Rapports]              │
└─────────────────────────────────────────────────────────┘
```

---

## 💾 Gestion des données

### Fonctionnalités frontend requises

#### 1. **Sauvegarde automatique**
- Auto-sauvegarde toutes les 2 minutes (brouillon)
- Bouton "Sauvegarder" explicite
- Indicateur visuel "Dernière sauvegarde : il y a 1 min"

#### 2. **Validation**
- Validation côté client (JavaScript)
- Format des nombres (virgules/points)
- Champs obligatoires
- Cohérence des données (ex: total repas/semaine)

#### 3. **Calculs temps réel**
- Impact CO2 affiché instantanément
- Totaux par catégorie
- Comparaisons avec année précédente

#### 4. **Export**
- Format CSV
- Format Excel
- Format PDF (rapport)

#### 5. **Historique**
- Voir les saisies des années précédentes
- Comparer les années
- Évolution graphique

---

## 🚀 Fonctionnalités avancées (V2)

### Phase 1 - MVP
- ✅ Authentification simple
- ✅ 4 modules de saisie
- ✅ Calculs automatiques
- ✅ Dashboard basique
- ✅ Export CSV

### Phase 2 - Améliorations
- 📊 Graphiques interactifs (Chart.js léger)
- 📧 Notifications par email (rappels de saisie)
- 🔄 Import depuis fichiers Excel existants
- 📝 Commentaires et annotations
- 🎯 Objectifs de réduction

### Phase 3 - Avancé
- 🤖 Détection d'anomalies
- 📈 Prédictions basées sur historique
- 🏆 Gamification (badges services éco-responsables)
- 📱 Application mobile (PWA)
- 🔗 Intégration API (fournisseurs énergie)

---

## 🛠️ Stack Technique - Django Full-Stack

### Architecture retenue : **Django Full-Stack** ✅

**Décision** : Application monolithique Django avec templates intégrés, adaptée au contexte municipal et aux principes d'éco-conception.

### Backend

- **Python** : 3.11+ (LTS)
- **Framework** : Django 5.0+
  - Django Admin : Interface d'administration complète
  - Django Auth : Système d'authentification intégré
  - Django Forms : Validation et génération de formulaires
  - Django ORM : Gestion base de données
- **Base de données** : PostgreSQL 15+
- **Serveur de développement** : Django runserver
- **Serveur de production** : Gunicorn + Nginx

### Frontend

- **Templates** : Django Templates
  - Syntaxe : `{% %}` pour logique, `{{ }}` pour variables
  - Héritage de templates (`{% extends %}`, `{% block %}`)
  - Filtres et tags personnalisés
- **CSS** : Vanilla CSS avec variables CSS
  - Pas de preprocesseur (Sass/Less)
  - Design system avec variables CSS (`:root`)
  - Mobile-first responsive
- **JavaScript** : Vanilla ES6+ (minimal)
  - Calculs temps réel côté client
  - Validation formulaires
  - Interactions légères
  - **Pas de framework JS** (React/Vue/Angular)
- **Icons** : SVG inline (pas de font-icons)

### Base de données

```python
# PostgreSQL configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'evry_bilan_carbone',
        'USER': 'evry_user',
        'PASSWORD': '***',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Outils de développement

- **Gestion de paquets** : pip + requirements.txt
- **Environnement virtuel** : venv (Python natif)
- **Linter Python** : Ruff (rapide et moderne)
- **Formatter** : Black
- **Tests** : pytest + pytest-django
- **Migration BD** : Django migrations (intégré)
- **Fichiers statiques** : Django collectstatic

### Structure du projet

```
webapp/
├── manage.py                    # Script Django principal
├── requirements.txt             # Dépendances Python
├── .env                         # Variables d'environnement (git-ignored)
├── config/                      # Configuration Django
│   ├── __init__.py
│   ├── settings.py             # Settings principal
│   ├── urls.py                 # Routes principales
│   └── wsgi.py                 # WSGI pour production
├── apps/                        # Applications Django
│   ├── core/                   # App principale (auth, base)
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   └── templates/
│   │       └── core/
│   │           ├── base.html
│   │           ├── dashboard.html
│   │           └── login.html
│   ├── vehicles/               # Module véhicules
│   │   ├── models.py          # VehicleData, EmissionFactor
│   │   ├── views.py           # Vue formulaire, calculs
│   │   ├── forms.py           # Formulaires Django
│   │   ├── urls.py            # Routes du module
│   │   └── templates/
│   │       └── vehicles/
│   │           ├── form.html
│   │           └── list.html
│   ├── buildings/              # Module bâtiments (futur)
│   ├── alimentation/           # Module alimentation (futur)
│   └── achats/                 # Module achats (futur)
├── static/                      # Fichiers statiques
│   ├── css/
│   │   ├── base.css           # Styles de base
│   │   ├── components.css     # Composants réutilisables
│   │   └── modules/
│   │       └── vehicles.css
│   ├── js/
│   │   ├── main.js
│   │   └── vehicle-calculator.js
│   └── img/
│       └── (images optimisées)
└── templates/                   # Templates globaux
    └── base.html               # Template de base
```

### Avantages de cette stack

1. **Simplicité** : Un seul langage (Python), une seule stack
2. **Intégré** : Admin, auth, ORM inclus
3. **Mature** : Django = standard pour admin publique en France
4. **Sécurisé** : Protection CSRF, XSS, SQL injection par défaut
5. **Éco-responsable** : Pas de build step, pas de dépendances npm
6. **Maintenable** : Code lisible, documentation abondante en français

### Dépendances principales

```txt
# requirements.txt
Django==5.0.1
psycopg2-binary==2.9.9      # Driver PostgreSQL
python-decouple==3.8        # Variables d'environnement
django-environ==0.11.2      # Config ENV
gunicorn==21.2.0            # Serveur production
whitenoise==6.6.0           # Serveur fichiers statiques
```

### Commandes de développement

```bash
# Créer projet
django-admin startproject config .

# Créer app
python manage.py startapp vehicles

# Migrations
python manage.py makemigrations
python manage.py migrate

# Créer superuser
python manage.py createsuperuser

# Lancer serveur dev
python manage.py runserver

# Collecter fichiers statiques
python manage.py collectstatic

# Tests
pytest
```

---

## 📐 Architecture des Pages

```
/
├── index.html (Login)
├── dashboard.html (Tableau de bord)
├── /modules/
│   ├── alimentation.html
│   ├── vehicules.html
│   ├── batiments.html
│   └── achats.html
├── /admin/
│   ├── users.html
│   ├── settings.html
│   └── reports.html
├── /assets/
│   ├── /css/
│   │   ├── main.css
│   │   ├── forms.css
│   │   └── dashboard.css
│   ├── /js/
│   │   ├── app.js
│   │   ├── calculator.js
│   │   └── validation.js
│   └── /icons/
│       └── (SVG icons)
└── /api/ (si frontend séparé du backend)
```

---

## 🎯 Wireframes détaillés

### Page d'accueil (Dashboard)
![Dashboard mockup]
- Header avec logo et navigation
- Bandeau de progression globale
- 4 cards pour les modules principaux
- Graphique circulaire (répartition par secteur)
- Accès rapide aux actions courantes

### Page module Alimentation
![Alimentation form]
- Breadcrumb : Accueil > Modules > Alimentation
- Filtres : Année, Service
- Formulaire de saisie structuré
- Calculatrice d'impact en temps réel (sidebar)
- Boutons d'action : Annuler, Brouillon, Sauvegarder

### Page module Véhicules
![Véhicules list]
- Tableau récapitulatif de la flotte
- Boutons : Ajouter véhicule, Import Excel
- Modal pour ajout/édition véhicule
- Filtres : Service, Type de véhicule, Motorisation

### Page module Bâtiments
![Bâtiments detail]
- Liste des sites avec recherche
- Accordion pour détail par site
- Formulaire énergies par site
- Graphique consommation/m²

### Page module Achats
![Achats categories]
- Tabs : Services | Fournitures | Équipements | Produits
- Tableau de saisie dynamique
- Recherche dans référentiel pré-rempli
- Calcul automatique impact

---

## ✅ Checklist de développement

### Phase de design
- [ ] Créer les wireframes finaux
- [ ] Valider l'UX avec un échantillon d'agents
- [ ] Définir le design system complet
- [ ] Créer les composants CSS réutilisables

### Phase de développement
- [ ] Structure HTML des templates
- [ ] CSS responsive et éco-conçu
- [ ] JavaScript pour validation et calculs
- [ ] Intégration avec API backend
- [ ] Tests d'accessibilité (WCAG 2.1)
- [ ] Tests multi-navigateurs

### Phase de test
- [ ] Tests utilisateurs avec agents
- [ ] Vérification des calculs CO2
- [ ] Tests de charge (plusieurs users simultanés)
- [ ] Audit éco-conception (Green IT)

---

## 📏 Métriques Éco-conception

Objectifs à respecter :

| Métrique | Objectif | Justification |
|----------|----------|---------------|
| Poids page d'accueil | < 500 KB | Rapidité + économie bande passante |
| Poids CSS | < 50 KB | Minimalisme |
| Poids JS | < 100 KB | Performance |
| Nombre de requêtes HTTP | < 20 | Efficacité réseau |
| Score Lighthouse Perf | > 90 | Optimisation générale |
| Compatibilité | IE11, Chrome, Firefox, Safari | Accessibilité maximale |

---

## 🎨 Exemple de composants CSS

### Bouton éco-responsable
```css
.btn {
  background: var(--primary);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.btn:hover {
  background: var(--secondary);
}

.btn--secondary {
  background: var(--bg-card);
  color: var(--primary);
  border: 1px solid var(--primary);
}
```

### Card module
```css
.module-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.module-card__icon {
  font-size: 32px;
  margin-bottom: 10px;
}

.module-card__title {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 8px;
}

.module-card__stats {
  color: var(--text-light);
  font-size: 14px;
  margin-bottom: 16px;
}
```

---

## 📝 Notes importantes

### Données de référence (facteurs d'émission)
Ces valeurs doivent être stockées en base de données et configurables :

**Énergies** :
- Électricité : **0.052 kg CO₂/kWh**
- Gaz naturel : **0.24 kg CO₂/kWh**
- Chaleur réseau : **0.146 kg CO₂/kWh**

**Carburants** (ADEME Base Carbone - Combustion + Amont) :
- Essence (SP95-98) : **2.79 kg CO₂e/L** ✅ Valeur officielle vérifiée
- Gazole routier : **3.16 kg CO₂e/L** ✅ Valeur officielle vérifiée

**Alimentation** :
- Repas végétarien : **0.51 kg CO₂/repas**
- Repas poulet/poisson : **1.5 kg CO₂/repas**
- Repas bœuf : **7.26 kg CO₂/repas**
- Repas porc : **~2 kg CO₂/repas**

> ⚠️ **Note importante** : Les valeurs carburants incluent la combustion ET l'amont (extraction, raffinage, transport). Elles sont ~20% plus élevées que les valeurs "combustion seule" pour un bilan carbone complet et conforme (Scope 1+3).
> 
> 📄 **Source** : Base Carbone® ADEME - Vérifiée le 16/01/2026  
> 🔗 **Référence** : Voir `ADEME_VERIFIED_VALUES.md` pour la méthodologie de vérification

### Accessibilité
- ARIA labels pour les lecteurs d'écran
- Contraste de couleurs conforme WCAG AA (minimum)
- Navigation au clavier
- Messages d'erreur explicites

### Performance
- Lazy loading des images
- Minification CSS/JS en production
- Cache côté client (localStorage pour brouillons)
- Compression Gzip/Brotli

---

## 🎯 Priorités de développement

1. **Authentification** (Critique)
2. **Dashboard** (Essentiel - vue d'ensemble)
3. **Module Achats** (30% du bilan - prioritaire)
4. **Module Bâtiments** (12% - complexe)
5. **Module Alimentation** (12% - relativement simple)
6. **Module Véhicules** (gestion de flotte)
7. **Exports & Rapports** (validation finale)

---

## 💡 Suggestions d'amélioration UX

### Aide contextuelle
- **Tooltips** sur les champs complexes
- **FAQ** intégrée par module
- **Guide de démarrage** pour nouveaux agents

### Gamification légère
- Badge "Service éco-responsable"
- Comparaison avec moyenne (si pertinent)
- Objectifs de réduction visualisés

### Notifications
- Rappel de saisie mensuelle
- Alertes si incohérence détectée
- Confirmation envoi par email

---

**Ce document constitue la base pour développer le front-end de l'application. Prochaine étape : validation de ces spécifications avant de commencer le codage.**
