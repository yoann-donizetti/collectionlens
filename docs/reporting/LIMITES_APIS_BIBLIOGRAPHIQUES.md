# Limites des APIs bibliographiques généralistes

## Contexte

Dans le cadre du POC CollectionLens, plusieurs sources bibliographiques ont été évaluées afin d'alimenter la future base de données du projet.

Les sources étudiées sont :

* Google Books
* OpenLibrary
* BNF
* Nudger

L'objectif était d'évaluer leur capacité à couvrir les besoins de CollectionLens sur les univers :

* Manga
* Bande dessinée
* Comics

Les analyses ont été réalisées à travers plusieurs étapes :

* benchmark initial ;
* benchmark étendu sur 1036 séries ;
* construction du pipeline ISBN multi-sources ;
* sauvegarde des données brutes ;
* analyse de couverture ;
* analyse de qualité des métadonnées.

---

# Résultats de couverture

| Source       | Couverture |
| ------------ | ---------: |
| Nudger       |    96.14 % |
| Google Books |    84.75 % |
| BNF          |    71.53 % |
| OpenLibrary  |    16.89 % |

Ces résultats montrent qu'aucune source ne couvre seule l'ensemble des besoins du projet.

---

# Limites observées

## Google Books

### Points forts

* Bonne couverture ISBN
* Présence fréquente de descriptions
* Métadonnées facilement exploitables
* API simple à intégrer

### Limites

* Quotas d'utilisation pouvant bloquer les traitements massifs
* Couverture incomplète de certains mangas, BD et comics
* Métadonnées parfois hétérogènes
* Informations éditeur souvent absentes ou incomplètes
* Dépendance à un service tiers

### Impact pour CollectionLens

Google Books constitue une excellente source d'enrichissement mais ne peut pas être utilisée comme source unique.

---

## OpenLibrary

### Points forts

* API ouverte
* Présence de couvertures
* Métadonnées complémentaires ponctuelles

### Limites

* Très faible couverture sur les mangas, BD et comics
* Descriptions rarement disponibles
* Nombreux ISBN absents
* Timeouts observés lors des benchmarks
* Qualité inégale selon les ouvrages

### Impact pour CollectionLens

OpenLibrary doit être considérée comme une source secondaire d'enrichissement.

---

## BNF

### Points forts

* Métadonnées bibliographiques fiables
* Informations auteurs complètes
* Informations éditeurs complètes
* Dates de publication de qualité
* Grande stabilité des résultats

### Limites

* Couverture inférieure à Google Books et Nudger
* Descriptions principalement orientées catalogage
* Peu d'informations directement exploitables pour la recommandation

### Impact pour CollectionLens

La BNF constitue une excellente source de validation bibliographique.

---

## Nudger

### Points forts

* Meilleure couverture observée
* Données spécialisées Manga / BD / Comics
* Métadonnées métier adaptées au projet
* Présence d'informations de pagination, format et prix

### Limites

* Dépendance à un dataset externe
* Qualité dépendante des données sources
* Peu de contenu descriptif exploitable pour le RAG ou la recommandation

### Impact pour CollectionLens

Nudger constitue la source principale du projet.

---

# Complémentarité des sources

L'un des principaux enseignements du benchmark est la forte complémentarité entre les différentes sources.

Chaque source apporte une valeur spécifique :

| Source       | Apport principal                      |
| ------------ | ------------------------------------- |
| Nudger       | Couverture métier Manga / BD / Comics |
| Google Books | Descriptions et enrichissement        |
| BNF          | Validation bibliographique            |
| OpenLibrary  | Compléments ponctuels et couvertures  |

Cette complémentarité justifie pleinement la mise en place d'une stratégie multi-sources.

Les résultats montrent également que l'utilisation combinée des différentes sources permet d'obtenir une couverture quasi complète du dataset étudié.

---

# Ouverture sur l'écosystème du livre

L'analyse des APIs bibliographiques a conduit à une réflexion plus large sur le fonctionnement des métadonnées du livre en France.

Cette démarche a notamment permis d'identifier plusieurs acteurs majeurs du secteur :

* Dilicom ;
* Electre ;
* réseaux de libraires spécialisés ;
* flux ONIX ;
* diffuseurs et distributeurs.

Cette exploration a permis de mieux comprendre :

* la circulation des métadonnées ;
* les standards bibliographiques utilisés ;
* les mécanismes de diffusion des nouveautés ;
* les limites des APIs publiques.

Ces éléments constituent des pistes d'évolution intéressantes pour les futures versions de CollectionLens.

---

# Enseignements

Les travaux réalisés montrent qu'aucune API bibliographique généraliste ne permet à elle seule de répondre aux besoins du projet.

Les principales limites observées concernent :

* la couverture ISBN ;
* la qualité variable des métadonnées ;
* les quotas d'utilisation ;
* l'hétérogénéité des données ;
* l'absence de certaines nouveautés ou éditions spécialisées.

Les résultats valident donc la nécessité :

* d'une stratégie multi-sources ;
* d'un cache local ISBN ;
* d'une normalisation des métadonnées ;
* d'un futur agrégateur de données.

---

# Perspectives d'évolution

Les résultats obtenus lors du POC ouvrent plusieurs pistes d'amélioration.

## Intégration de nouvelles sources spécialisées

Les benchmarks ont montré les limites des APIs généralistes sur les univers Manga, BD et Comics.

De futures évaluations pourront être menées sur des sources plus spécialisées afin d'améliorer :

* la couverture ISBN ;
* la qualité des descriptions ;
* les métadonnées de séries ;
* les informations d'auteurs et d'éditeurs.

## Mise en place du cache local ISBN

Les limitations observées, notamment sur Google Books, confirment l'intérêt d'un système de cache local permettant de :

* réduire les appels externes ;
* améliorer les performances ;
* limiter les dépendances aux services tiers.

## Construction du dataset maître CollectionLens

Les résultats valident l'approche multi-sources retenue.

La prochaine étape consiste à fusionner les données provenant des différentes sources afin de produire une fiche unique par ouvrage.

## Amélioration continue de la qualité des données

L'architecture retenue permettra d'intégrer progressivement de nouvelles règles de normalisation, de résolution des conflits et d'enrichissement des métadonnées.

---

# Conclusion

Les benchmarks réalisés dans le cadre du POC confirment la pertinence de l'approche retenue pour CollectionLens.

La stratégie actuellement privilégiée est :

1. Nudger
2. Google Books
3. BNF
4. OpenLibrary

Cette approche permet :

* d'améliorer la couverture ISBN ;
* d'augmenter la complétude des métadonnées ;
* de réduire la dépendance à une source unique ;
* de préparer la constitution d'un dataset maître indépendant des APIs externes.

Les résultats obtenus constituent une étape importante dans la construction des futures briques du projet :

* agrégateur multi-sources ;
* cache local ISBN ;
* dataset maître CollectionLens ;
* moteur de recommandation ;
* pipeline RAG.
