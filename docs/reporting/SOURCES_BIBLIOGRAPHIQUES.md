# Sources bibliographiques complémentaires — POC Data

## Objectif

Identifier les sources complémentaires pouvant améliorer la couverture et la qualité des métadonnées pour CollectionLens.

## Contexte

Les premiers benchmarks réalisés sur Google Books et OpenLibrary montrent une couverture cumulée limitée sur l’échantillon testé.

Ces résultats justifient l’évaluation de sources complémentaires plus adaptées aux mangas, BD et comics, notamment pour les éditions françaises.

## État des sources bibliographiques

| Source | Type | Couverture observée | Qualité métadonnées | Statut | Commentaires |
|---|---|---|---|---|---|
| Google Books | API généraliste | ~50 % | Moyenne | Testé | Bonne couverture relative mais métadonnées parfois incomplètes et quotas journaliers limitants |
| OpenLibrary | API généraliste | ~20 % | Faible | Testé | Couverture limitée sur mangas, BD et comics français |
| BNF | API catalogue national | Non évaluée | Non évaluée | À tester | Potentiel fort pour les éditions françaises |
| Nudger | Source spécialisée | Non évaluée | Non évaluée | À tester | Potentiel intéressant pour l’enrichissement culturel |
| LOC | API catalogue international | Non évaluée | Non évaluée | À tester | Potentiel complémentaire pour comics et ouvrages anglophones |
| WorldCat | Catalogue mondial | Non évaluée | Non évaluée | Faisabilité à étudier | Accès API et contraintes techniques à clarifier |

## Critères d’évaluation

Les sources seront évaluées selon :

- taux de couverture ISBN ;
- complétude des métadonnées ;
- présence des descriptions ;
- qualité des auteurs/éditeurs ;
- présence des séries/volumes ;
- facilité d’accès ;
- contraintes techniques ;
- intérêt pour la recommandation.

## Conclusion attendue

L’objectif est de déterminer quelles sources peuvent être intégrées dans une stratégie multi-sources pour CollectionLens.