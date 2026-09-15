# ADR-0003 — Régime des valeurs chiffrées à deux vitesses

**Statut** : accepté
**Date** : 2026-09-15

## Contexte

Les skills frères ont mesuré que leur principale cause d'échec n'était pas
l'erreur de raisonnement mais le **sourcing** : une référence citée sans
provenance, dans une réponse par ailleurs correcte. `dpm-fpt` a dû porter la
jurisprudence à son socle vérifié après deux campagnes d'évaluation ; `drh-fpt`
a introduit un régime distinguant valeurs volatiles et plafonds réglementaires
datés.

Les finances locales aggravent ce risque d'un ordre de grandeur. Le métier est
saturé de nombres — taux, seuils, plafonds, montants de dotations, durées
d'amortissement, index de révision — et **la plupart changent au 1er janvier**.
Une valeur mémorisée par un modèle est statistiquement fausse, et elle est
d'autant plus dangereuse qu'elle est plausible.

## Décision

Instituer un régime explicite à **deux vitesses**, énoncé au `SKILL.md` §5.4
point 2 et détaillé dans `references/socle-sources-verification.md` §5 :

- **valeurs volatiles** — jamais citées de mémoire, jamais citées sans date
  d'effet. Vérifiées à la source ou absentes de la réponse ;
- **références structurelles stables** (nom d'un code, décret fondateur,
  architecture d'une nomenclature) — citables avec la réserve « à confirmer en
  version consolidée ».

Ce qui reste toujours transmissible : la **formule**, la **méthode**, la
**procédure**, la **liste des variables**. Un ratio se donne comme numérateur
sur dénominateur ; son seuil d'alerte ne se donne pas sans vérification — et se
qualifie comme relevant de la doctrine, non de la réglementation.

Deux fichiers séparent les responsabilités :

- `references/references-verifiees.md` — les **identifiants de textes**
  réellement vérifiés, datés. Seul fichier du dépôt autorisé à en contenir ;
- `references/cache-taux-seuils.md` — les **valeurs chiffrées** vérifiées, avec
  leur date. Artefact de maintenance, exclu du package d'exécution, jamais
  citable comme source.

## Conséquences

- Le cache naît **volontairement vide**. Une cellule « à renseigner » est l'état
  normal, pas une lacune à combler par plausibilité.
- `validate_repo.py` interdit tout identifiant Légifrance en dur hors du
  registre vérifié. C'est l'invariant anti-hallucination central du dépôt.
- Les branches sont rédigées sans valeurs. Elles perdent en confort de lecture
  immédiat et gagnent en durée de vie : une branche sans chiffre ne périme pas
  au 1er janvier.
- L'auto-vérification (`SKILL.md` §7 point 6) est un **test à charge** : le
  balayage part du corps du texte produit, pas d'un tableau récapitulatif, et
  porte sur les valeurs autant que sur les références.

## Alternatives écartées

- **Embarquer les valeurs de l'exercice en cours** — écarté : le skill serait
  faux dès le 1er janvier suivant, sans que rien ne le signale à l'utilisateur.
- **Laisser le modèle citer une valeur avec une réserve générique** — écarté :
  la réserve est lue comme une précaution de style, et la valeur est retenue.
  Une valeur non vérifiée doit être absente, pas atténuée.
