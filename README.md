# Projet_Fil_Rouge_IA
Construire une solution IA. 


# 🚀 Process Mise en Place de la Solution IA

## 📌 Description du Projet
Ce projet vise à concevoir et implémenter une solution d’intelligence artificielle (IA) pour améliorer la gestion des achats, de la logistique et des approvisionnements. Il repose sur la collecte des besoins des utilisateurs afin d'automatiser et optimiser les processus métiers.

## 🎯 Objectifs Principaux
- **Comprendre les besoins utilisateurs** à travers des questionnaires ciblés.
- **Développer un moteur IA** capable de prédire les retards et optimiser les stocks.
- **Automatiser les processus** liés aux achats, à la logistique et aux approvisionnements.
- **Créer une interface interactive** pour suivre les indicateurs et alertes en temps réel.
- **Faciliter l’intégration avec les outils existants** pour une adoption efficace.

## 🏗️ Structure du Projet
Le projet se décompose en plusieurs étapes :
1. **Analyse des besoins utilisateurs** → Identification des défis rencontrés.
2. **Développement d'un modèle IA** → Création d’algorithmes de prédiction et d’optimisation.
3. **Conception d’une interface utilisateur** → Tableaux de bord et visualisation des données.
4. **Déploiement et intégration** → Connexion avec les systèmes existants (ERP, CRM, BI).

## 📋 Besoins des Utilisateurs
Des questions ciblées ont été posées aux différents acteurs pour définir leurs attentes :
- **Chef de Projet Achat** : suivi des fournisseurs, négociation, gestion des retards.
- **Gestionnaire Logistique** : optimisation des itinéraires, suivi des expéditions.
- **Responsable Assurance Livraison** : évaluation des fournisseurs, audits et rapports.
- **Gestionnaire Approvisionnement** : gestion des stocks, anticipation des ruptures.

ℹ️ _Les détails des questionnaires sont disponibles dans le document_ **Process_Mise_Place_IA.docx**.

## 🛠️ Technologies Utilisées
- **Python** : Analyse des données et Machine Learning.
- **Power BI** : Création de tableaux de bord interactifs.
- **MongoDB / SQL** : Stockage des données et gestion des requêtes.
- **API & Intégrations** : Connexion aux outils tiers (ERP, CRM).

## 🚀 Contribution
Vous pouvez contribuer au projet en suivant ces étapes :
1. **Fork** ce dépôt.
2. **Clone** votre fork :
   ```sh
   git clone https://github.com/Purple-Manue/Projet_Fil_Rouge_IA.git
   git@github.com:Purple-Manue/Projet_Fil_Rouge_IA.git

3. **Schéma de l'application :**
Leadtime_IA/
│
├── controller/
│   └── project_controller.py  # Gère les interactions avec l'utilisateur
│
├── data/
│   ├── délai article.xlsx  # Fichier de données 1
│   ├── en tête commande.xlsx  # Fichier de données 2
│   ├── ligne commande en cours.xlsx  # Fichier de données 3
│   ├── ligne commande livrée.csv  # Fichier de données 4
│   └── livraison commande fournisseur.xlsx  # Fichier de données 5
│
├── img/
│   └── Logo_LeadtimeIA.webp  # Logo de l'application
│
├── model/
│   └── data_handler.py  # Gère le traitement des données
│
├── view/
│   └── display.py  # Affiche la page d'accueil et les éléments de l'interface
│
├── app.py  # Point d'entrée de l'application Streamlit
├── poetry.lock  # Fichier de gestion des dépendances de Poetry
├── pyproject.toml  # Fichier de configuration de Poetry
├── requirements.txt  # Liste des dépendances pour pip (facultatif)
├── README.md  # Documentation de l'application
├── .gitignore  # Fichier pour ignorer certains fichiers dans Git
└── desktop.ini  # Fichier Windows non nécessaire (à supprimer si inutile)
