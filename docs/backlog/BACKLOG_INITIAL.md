# CollectionLens — Backlog Initial

## 1. Objectif du backlog

Ce backlog a pour objectif de structurer progressivement le développement de CollectionLens à travers une approche modulaire et évolutive.

Le projet est organisé autour de plusieurs grands domaines fonctionnels permettant de :

• Prioriser les fonctionnalités
• Structurer les phases POC et MVP
• Identifier les dépendances techniques
• Faciliter le suivi du projet
• Préparer l’organisation des futures issues GitHub et sprints Agile

Le backlog est volontairement organisé à un niveau fonctionnel afin de conserver une vision claire du projet avant le découpage détaillé des tâches techniques.

---

# 2. EPIC — DATA

## DATA-01 — Collecte des métadonnées culturelles

### Objectif

Mettre en place la récupération automatique des informations d’œuvres via APIs et sources externes.

### Fonctionnalités attendues

• Recherche d’œuvres
• Récupération des métadonnées
• Récupération des synopsis
• Récupération des genres et tags
• Récupération des informations de séries et volumes
• Gestion des couvertures

---

## DATA-02 — Structuration et nettoyage des données

### Objectif

Construire un pipeline permettant de nettoyer, standardiser et structurer les données récupérées.

### Fonctionnalités attendues

• Standardisation des formats
• Gestion des doublons
• Nettoyage des métadonnées
• Structuration des séries et volumes
• Validation des données récupérées

---

## DATA-03 — Évaluation de la qualité des données

### Objectif

Mesurer la qualité et l’exploitabilité des données utilisées dans le cadre du POC.

### Fonctionnalités attendues

• Analyse de complétude
• Analyse de cohérence
• Détection des données manquantes
• Évaluation des APIs utilisées
• Identification des limites des sources externes

---

# 3. EPIC — COLLECTION

## COLLECTION-01 — Gestion de collection utilisateur

### Objectif

Permettre à un utilisateur de créer et gérer sa collection culturelle.

### Fonctionnalités attendues

• Ajout d’œuvres
• Suppression d’œuvres
• Suivi des séries
• Gestion des volumes possédés
• Recherche dans la collection

---

## COLLECTION-02 — Analyse et visualisation de collection

### Objectif

Proposer des outils d’analyse et de visualisation des préférences utilisateur.

### Fonctionnalités attendues

• Statistiques utilisateur
• Visualisation des genres favoris
• Analyse des habitudes de lecture
• Dashboard simplifié

---

# 4. EPIC — RECOMMENDATION

## REC-01 — Premier moteur de recommandation par contenu

### Objectif

Construire un premier système de recommandation basé sur les métadonnées des œuvres.

### Fonctionnalités attendues

• Analyse des genres
• Exploitation des tags
• Analyse des synopsis et descriptions
• Calcul de similarité entre œuvres
• Recommandation à partir d’un titre sélectionné

### Objectif du POC

Valider la faisabilité d’un premier système de recommandation basé sur les contenus culturels disponibles.

---

## REC-02 — Explication et contextualisation des recommandations

### Objectif

Utiliser des modèles de langage afin de reformuler et contextualiser les recommandations proposées.

### Fonctionnalités attendues

• Explication des recommandations
• Reformulation utilisateur
• Génération de suggestions contextualisées

---

## REC-03 — Évaluation des recommandations

### Objectif

Évaluer la pertinence des recommandations produites.

### Fonctionnalités attendues

• Analyse qualitative des recommandations
• Comparaison des approches
• Évaluation de similarité
• Suivi des performances du moteur

---

# 5. EPIC — IA / NLP / RAG

## IA-01 — Premières expérimentations NLP

### Objectif

Expérimenter l’exploitation des données textuelles des œuvres.

### Fonctionnalités attendues

• Nettoyage de texte
• Prétraitement NLP
• Analyse de similarité textuelle
• Préparation des futurs embeddings

---

## IA-02 — Embeddings vectoriels

### Objectif

Tester des approches de représentation vectorielle des œuvres culturelles.

### Fonctionnalités attendues

• Génération d’embeddings
• Similarité sémantique
• Recherche de contenus proches

---

## IA-03 — Recherche conversationnelle et RAG

### Objectif

Intégrer progressivement des fonctionnalités conversationnelles basées sur le RAG.

### Fonctionnalités attendues

• Recherche conversationnelle
• Retrieval de contenus
• Génération de réponses contextualisées
• Exploration conversationnelle des collections

---

# 6. EPIC — FRONTEND

## FRONT-01 — Interface Streamlit

### Objectif

Construire une première interface utilisateur simple pour le POC.

### Fonctionnalités attendues

• Recherche d’œuvres
• Affichage des collections
• Affichage des recommandations
• Dashboard simplifié

---

## FRONT-02 — Expérience utilisateur

### Objectif

Améliorer progressivement l’expérience utilisateur de la plateforme.

### Fonctionnalités attendues

• Navigation améliorée
• Visualisations enrichies
• Personnalisation de l’interface
• Optimisation UX

---

# 7. EPIC — MLOPS / EXPÉRIMENTATION

## MLOPS-01 — Suivi des expérimentations

### Objectif

Structurer le suivi des expérimentations liées aux systèmes de recommandation et IA.

### Fonctionnalités attendues

• Historisation des tests
• Comparaison des approches
• Suivi des performances
• Tracking des expérimentations

---

## MLOPS-02 — Évaluation des performances

### Objectif

Mesurer les performances des différents mécanismes IA et recommandation.

### Fonctionnalités attendues

• Évaluation des recommandations
• Analyse des temps de réponse
• Comparaison des modèles
• Analyse de pertinence

---

# 8. EPIC — DEVOPS / ARCHITECTURE

## DEVOPS-01 — Structuration du projet

### Objectif

Mettre en place une architecture projet claire et maintenable.

### Fonctionnalités attendues

• Organisation du repository
• Gestion Git et branches
• Structuration documentaire
• Gestion des environnements

---

## DEVOPS-02 — Industrialisation progressive

### Objectif

Préparer progressivement le projet à une architecture plus avancée.

### Fonctionnalités attendues

• Configuration des environnements
• Préparation au déploiement
• Modularisation du code
• Préparation des futurs pipelines

---

# 9. Priorisation globale

| Phase         | Priorité          |
| ------------- | ----------------- |
| DATA-01       | Très haute        |
| DATA-02       | Très haute        |
| COLLECTION-01 | Haute             |
| REC-01        | Très haute        |
| FRONT-01      | Haute             |
| REC-02        | Moyenne           |
| IA-01         | Moyenne           |
| IA-02         | Moyenne           |
| IA-03         | Faible à ce stade |

---

# 10. Vision d’évolution du backlog

Le backlog a vocation à évoluer progressivement selon :

• Les résultats obtenus lors du POC
• La qualité des données disponibles
• Les retours utilisateurs
• Les contraintes techniques identifiées
• Les expérimentations réalisées autour de la recommandation et de l’IA

Cette approche permet de conserver un projet évolutif tout en maîtrisant progressivement la complexité technique de CollectionLens.
