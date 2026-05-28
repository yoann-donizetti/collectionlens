# CollectionLens — Architecture Globale

## 1. Objectif de l’architecture

L’architecture de CollectionLens est pensée dans une logique :

• Modulaire
• Évolutive
• Maintenable
• Progressive

L’objectif est de permettre le développement progressif du projet depuis un POC orienté récupération de données et recommandation jusqu’à une plateforme plus complète intégrant des fonctionnalités avancées d’intelligence artificielle.

L’architecture doit notamment permettre :

• La centralisation des collections utilisateur
• L’exploitation de métadonnées culturelles
• L’intégration de mécanismes de recommandation
• L’ajout progressif de fonctionnalités IA et RAG
• La séparation claire des différentes responsabilités techniques

---

## 2. Vue d’ensemble de l’architecture

CollectionLens repose sur plusieurs briques principales :

| Composant                | Rôle principal                         |
| ------------------------ | -------------------------------------- |
| Interface utilisateur    | Interaction avec la plateforme         |
| Backend applicatif       | Gestion logique métier                 |
| APIs externes            | Récupération des métadonnées           |
| Pipeline Data            | Nettoyage et structuration des données |
| Base de données          | Stockage des œuvres et collections     |
| Moteur de recommandation | Analyse de similarité et suggestions   |
| Modules IA               | NLP, embeddings et RAG                 |
| Dashboard analytique     | Visualisation des données utilisateur  |

Le projet adopte une architecture progressive permettant d’intégrer progressivement les fonctionnalités avancées sans remettre en cause les fondations initiales.

---

## 3. Architecture fonctionnelle

### 3.1 Interface utilisateur

L’interface utilisateur permettra :

• La gestion des collections
• La recherche d’œuvres
• L’affichage des recommandations
• La consultation des statistiques
• L’interaction avec les futures fonctionnalités conversationnelles

Dans le cadre du POC et du MVP, une interface Streamlit sera privilégiée afin de faciliter le prototypage rapide.

---

### 3.2 Backend applicatif

Le backend centralisera :

• La logique métier
• Les traitements applicatifs
• Les appels APIs
• Les mécanismes de recommandation
• Les traitements IA

Cette couche permettra de séparer clairement :

• Les traitements de données
• La logique de recommandation
• L’interface utilisateur

---

### 3.3 APIs et récupération des données

CollectionLens exploitera plusieurs APIs et sources de données externes afin de récupérer :

• Les informations d’œuvres
• Les métadonnées
• Les synopsis
• Les genres
• Les couvertures
• Les informations de séries et volumes

Le POC permettra notamment d’évaluer :

• La qualité des données disponibles
• La cohérence des métadonnées
• Les limites des APIs utilisées

---

### 3.4 Pipeline de traitement des données

Le pipeline Data aura pour rôle :

• Le nettoyage des données
• La standardisation des formats
• La gestion des doublons
• La structuration des œuvres
• La préparation des données pour les recommandations

Cette étape constitue une brique essentielle pour assurer :

• La qualité des recommandations
• La cohérence des collections
• La fiabilité des futures fonctionnalités IA

---

### 3.5 Base de données

La base de données permettra de stocker :

• Les œuvres
• Les séries
• Les volumes
• Les métadonnées enrichies
• Les collections utilisateur
• Les futurs résultats d’analyse et recommandations

Dans un premier temps, le projet pourra s’appuyer sur SQLite dans le cadre du POC avant une éventuelle évolution vers PostgreSQL.

---

### 3.6 Moteur de recommandation

Le moteur de recommandation constitue le cœur fonctionnel du projet.

Dans le cadre du POC, les premières recommandations reposeront principalement sur :

• Les genres
• Les tags
• Les descriptions
• Les synopsis
• Les similarités entre œuvres

L’objectif est de tester la capacité du système à proposer des recommandations pertinentes à partir d’un titre sélectionné par l’utilisateur.

Cette première approche reposera principalement sur une logique de recommandation par contenu.

Les modèles de langage pourront être utilisés en complément afin de :

• Reformuler les recommandations
• Contextualiser les suggestions
• Générer des explications utilisateur

---

### 3.7 Modules IA et RAG

Les fonctionnalités IA avancées seront intégrées progressivement après validation des fondations du projet.

Ces modules pourront inclure :

• NLP
• Embeddings vectoriels
• Similarité sémantique
• Recherche conversationnelle
• Architectures RAG

L’intégration de ces fonctionnalités dépendra notamment :

• De la qualité des données disponibles
• Des résultats obtenus lors du POC
• De la pertinence des recommandations générées

---

## 4. Architecture des données

Les principales catégories de données manipulées par CollectionLens seront :

| Type de données     | Exemples                  |
| ------------------- | ------------------------- |
| Métadonnées œuvres  | Titres, synopsis, genres  |
| Informations séries | Volumes, éditions         |
| Données utilisateur | Collections, préférences  |
| Données analytiques | Statistiques, similarités |
| Données IA          | Embeddings, résultats NLP |

Ces données devront être :

• Structurées
• Standardisées
• Nettoyées
• Exploitables pour les recommandations

---

## 5. Architecture du POC

Le POC reposera sur une architecture simplifiée permettant de valider :

• La récupération des données
• La structuration des œuvres
• La gestion de collection
• Les premiers mécanismes de recommandation

Le flux principal sera le suivant :

1. Sélection d’une œuvre par l’utilisateur
2. Récupération des métadonnées via APIs
3. Nettoyage et structuration des données
4. Calcul de similarité entre œuvres
5. Génération des recommandations
6. Restitution via interface utilisateur

Cette architecture permettra de tester progressivement la faisabilité technique du projet avant l’intégration de fonctionnalités plus avancées.

---

## 6. Évolutivité de l’architecture

L’architecture de CollectionLens est pensée pour évoluer progressivement vers :

• Une meilleure scalabilité
• Une séparation plus avancée des services
• L’intégration de fonctionnalités IA complexes
• L’ajout de bases vectorielles
• Des mécanismes conversationnels avancés
• Une personnalisation plus poussée

Cette approche progressive permet de :

• Limiter la complexité initiale
• Sécuriser les choix techniques
• Faciliter la maintenance
• Garantir l’évolutivité du projet

---

## 7. Architecture cible à long terme

À long terme, CollectionLens pourrait évoluer vers une architecture plus avancée intégrant :

• API backend dédiée
• Base relationnelle PostgreSQL
• Base vectorielle pour embeddings
• Services NLP spécialisés
• Systèmes RAG conversationnels
• Frontend plus avancé
• Déploiement cloud

Cette évolution dépendra des résultats du POC, des besoins utilisateurs et de la maturité progressive du projet.
