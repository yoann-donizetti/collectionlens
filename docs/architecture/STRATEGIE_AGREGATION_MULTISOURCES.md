# Stratégie d’agrégation multi-sources — CollectionLens

## Objectif

Définir les règles de priorité entre les sources bibliographiques afin de produire une fiche ouvrage enrichie, cohérente et exploitable par CollectionLens.

Cette stratégie s’appuie sur le benchmark étendu réalisé sur 1036 séries issues de la collection réelle.

## Sources retenues

| Source | Rôle |
|---|---|
| Nudger | Source principale de couverture et de données spécialisées BD / Manga / Comics |
| Google Books | Source d’enrichissement bibliographique et descriptif |
| BNF | Source de validation bibliographique française |
| OpenLibrary | Source secondaire d’enrichissement ponctuel |

## Résultats de couverture

| Source | Couverture |
|---|---:|
| Nudger | 96.14 % |
| Google Books | 84.36 % |
| BNF | 71.53 % |
| OpenLibrary | 17.18 % |

## Principe général

Aucune source ne répond seule à tous les besoins de CollectionLens.

La stratégie retenue consiste donc à combiner les sources selon leur point fort :

- Nudger pour identifier les ouvrages et récupérer les métadonnées spécialisées ;
- Google Books pour enrichir les descriptions et les métadonnées générales ;
- BNF pour fiabiliser les données bibliographiques françaises ;
- OpenLibrary comme source secondaire lorsque des couvertures ou informations complémentaires sont disponibles.

## Priorité par champ

| Champ | Priorité retenue |
|---|---|
| ISBN | Nudger |
| Titre | Nudger → Google Books → BNF |
| Auteurs | Google Books → BNF |
| Éditeur | Nudger → BNF → Google Books |
| Date de publication | Google Books → BNF |
| Description | Google Books → BNF |
| Catégories | Nudger → Google Books → OpenLibrary |
| Nombre de pages | Nudger → Google Books → BNF |
| Format | Nudger → BNF |
| Couverture | Google Books → OpenLibrary |
| Prix | Nudger |
| Identifiant officiel | BNF |
| Données sémantiques | OpenLibrary si disponible |

## Gestion des conflits

Lorsqu’un champ est disponible dans plusieurs sources :

1. la source prioritaire est utilisée ;
2. les autres valeurs peuvent être conservées pour audit ;
3. la source retenue doit être tracée.

Exemple :

| Champ | Valeur retenue | Source |
|---|---|---|
| title | Vinland Saga | Nudger |
| description | Résumé issu de Google Books | Google Books |
| bnf_ark | Notice officielle BNF | BNF |

## Traçabilité

Chaque champ agrégé devra conserver son origine.

Exemples de champs de traçabilité :

- title_source
- authors_source
- publisher_source
- description_source
- categories_source
- page_count_source
- cover_source

## Rôle dans le futur pipeline

La stratégie multi-sources servira de base pour :

- le pipeline de récupération ISBN ;
- la normalisation des métadonnées ;
- la construction du dataset maître ;
- le futur moteur de recommandation ;
- le futur pipeline RAG ;
- la stratégie de cache local ISBN.

## Conclusion

La stratégie retenue privilégie une approche pragmatique :

- Nudger comme source principale ;
- Google Books comme source d’enrichissement ;
- BNF comme source de validation bibliographique ;
- OpenLibrary comme source secondaire.

Cette approche permet de maximiser la couverture tout en conservant une bonne qualité des métadonnées.


## Règles de fallback

Le pipeline d'agrégation applique une stratégie de fallback séquentielle.

Pour chaque champ :

1. recherche dans la source prioritaire ;
2. si valeur absente, passage à la source suivante ;
3. répétition jusqu'à obtention d'une valeur ;
4. si aucune valeur n'est disponible, le champ reste vide.

Exemple :


Titre :

Nudger
↓
Google Books
↓
BNF
↓
NULL

Description :

Google Books
↓
BNF
↓
NULL

Couverture :

Google Books
↓
OpenLibrary
↓
NULL


## Exemple de fiche agrégée

ISBN : 9782351423554

Titre : Vinland Saga
Source : Nudger

Auteur : Makoto Yukimura
Source : Google Books

Éditeur : Kurokawa
Source : Nudger

Description : ...
Source : Google Books

Nombre de pages : 213
Source : Google Books

BNF ARK : cb41404031j
Source : BNF

