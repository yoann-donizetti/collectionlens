# Stratégie de cache local ISBN

## Objectif

Définir une stratégie de cache local afin de limiter les appels répétés aux sources externes lors de la récupération des métadonnées ISBN.

## Pourquoi un cache local ?

Le cache permet de :

- réduire les appels API ;
- limiter les risques liés aux quotas ;
- accélérer les traitements ;
- conserver les résultats déjà récupérés ;
- faciliter les benchmarks et les futures analyses qualité.

## Données mises en cache

Pour chaque ISBN, le cache devra conserver :

- l'ISBN recherché ;
- la source interrogée ;
- le statut de récupération ;
- les métadonnées normalisées ;
- les données brutes ;
- la date de récupération ;
- l'erreur éventuelle.

## Sources concernées

- Nudger ;
- Google Books ;
- BNF ;
- OpenLibrary.

## Principe de fonctionnement

Avant tout appel API :

1. vérifier si l'ISBN est déjà présent dans le cache ;
2. si la donnée existe, utiliser le cache ;
3. sinon, interroger la source externe ;
4. sauvegarder le résultat dans le cache ;
5. retourner le résultat normalisé.

## Structure proposée

```text
data/
└── cache/
    └── isbn/
        ├── google_books/
        ├── openlibrary/
        ├── bnf/
        └── nudger/
```


## Format de stockage

Pour le POC, le cache pourra être stocké en JSON ou JSONL.

Format recommandé :

```text
{
  "isbn_query": "9782351423554",
  "source": "google_books",
  "found": true,
  "status_code": 200,
  "retrieved_at": "2026-05-29T10:00:00",
  "normalized_data": {},
  "raw_data": {},
  "error": null
}
```

## Gestion des erreurs

Les erreurs doivent également être mises en cache afin d'éviter de répéter inutilement des appels infructueux.

Exemples :

no_result ;
timeout ;
quota_exceeded ;
request_error.

## Stratégie d'expiration

Pour le POC :

les résultats trouvés peuvent être conservés durablement ;
les erreurs temporaires comme timeout peuvent être relancées ;
les erreurs no_result peuvent être réévaluées plus tard.

## Rôle dans le pipeline

Le cache sera utilisé par :

le pipeline de récupération ISBN ;
les benchmarks ;
l'agrégateur multi-sources ;
les notebooks d'analyse qualité.
Conclusion

La stratégie de cache local est essentielle pour fiabiliser les traitements, réduire les appels API et préparer la construction du dataset maître CollectionLens.