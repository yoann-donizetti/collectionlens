# Stratégie de normalisation des métadonnées

## Objectif

Définir un modèle de métadonnées unique permettant d'unifier les informations provenant des différentes sources bibliographiques utilisées par CollectionLens.

Sources concernées :

- Nudger
- Google Books
- BNF
- OpenLibrary

---

# Principes

## Source indépendante

Le modèle CollectionLens ne doit dépendre d'aucune API spécifique.

Chaque source doit être convertie vers un format commun.

---

## Normalisation avant agrégation

Les données sont normalisées avant l'application des règles de priorité multi-sources.

Pipeline :

Source brute
↓
Normalisation
↓
Agrégation
↓
Fiche CollectionLens

---

# Modèle cible

## Identifiants

| Champ |
|---------|
| isbn |
| source_id |

---

## Informations bibliographiques

| Champ |
|---------|
| title |
| subtitle |
| authors |
| publisher |
| published_date |
| language |

---

## Informations descriptives

| Champ |
|---------|
| description |
| categories |
| subjects |

---

## Informations physiques

| Champ |
|---------|
| page_count |
| format |
| cover_url |

---

## Informations métier

| Champ |
|---------|
| price |
| currency |
| offers_count |

---

## Informations de traçabilité

| Champ |
|---------|
| source |
| raw_data |
| status_code |
| found |
| error |

---

# Règles de normalisation

## Texte

- suppression des espaces inutiles ;
- conversion des chaînes vides en NULL ;
- conservation des accents.

## Dates

Format unique :

YYYY-MM-DD

Exemples :

2009
→ 2009

2009-01
→ 2009-01

2009-01-15
→ 2009-01-15

## Auteurs

Toujours sous forme de liste :

["Makoto Yukimura"]

## Catégories

Toujours sous forme de liste.

## Descriptions

Conserver le texte brut.

Aucune réécriture automatique.

## Couvertures

Conserver uniquement l'URL principale.

---

# Champs spécifiques

Certaines données restent propres à une source :

## BNF

- bnf_ark

## OpenLibrary

- subject_people
- subject_places
- subject_times

## Nudger

- min_price
- offers_count

Ces champs peuvent être conservés pour enrichissement futur.

---

# Objectif final

Produire un objet standard unique utilisable par :

- l'agrégateur multi-sources ;
- le moteur de recommandation ;
- le pipeline RAG ;
- les analyses de collection ;
- les futurs services CollectionLens.