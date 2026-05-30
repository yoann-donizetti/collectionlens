# Modèle de données de collection utilisateur

## Objectif

Définir le modèle de données permettant de gérer une collection utilisateur dans CollectionLens.

Ce modèle doit permettre :

- de stocker les œuvres issues du dataset maître ;
- de rattacher des volumes à une collection utilisateur ;
- de gérer les statuts de possession et de lecture ;
- de stocker les notes et avis ;
- de préparer les futures recommandations.

## Principes

Le dataset maître contient les métadonnées ouvrage.

La collection utilisateur contient les informations personnelles liées à l’utilisateur.

Il faut donc séparer :

- les données bibliographiques ;
- les données de possession ;
- les données d’usage utilisateur.

## Entités principales

### User

Représente un utilisateur de CollectionLens.

Champs pressentis :

- id
- username
- email
- created_at

### Series

Représente une série culturelle.

Champs pressentis :

- id
- title
- media_type
- description
- publisher
- created_at

### Volume

Représente un ouvrage ou volume rattaché à une série.

Champs pressentis :

- id
- series_id
- isbn
- title
- volume_number
- authors
- publisher
- published_date
- description
- page_count
- format
- cover_url
- bnf_ark

### CollectionEntry

Représente le fait qu’un utilisateur possède ou suit un volume.

Champs pressentis :

- id
- user_id
- volume_id
- owned
- read
- favorite
- added_at
- purchase_price
- condition
- notes

### Rating

Représente une note ou un avis utilisateur.

Champs pressentis :

- id
- user_id
- volume_id
- rating
- review
- created_at

## Relations

```text
User 1 ── N CollectionEntry
Volume 1 ── N CollectionEntry

Series 1 ── N Volume

User 1 ── N Rating
Volume 1 ── N Rating
```


## Rôle pour la recommandation

Le moteur de recommandation pourra utiliser :

les volumes possédés ;
les volumes lus ;
les notes utilisateur ;
les avis utilisateur ;
les métadonnées enrichies du dataset maître.

## Décision POC

Pour le POC, le modèle sera volontairement simple.

Priorité :

séries ;
volumes ;
collection utilisateur ;
notes utilisateur.

Les fonctionnalités avancées seront traitées dans une phase ultérieure.