# ADR-0001 — Adopter le pattern d'architecture de `dpm-fpt`

**Statut** : accepté
**Date** : 2026-09-15

## Contexte

Deux skills métier territoriaux existaient déjà : `drh-fpt` (ressources
humaines) et `dpm-fpt` (police municipale). `dpm-fpt` avait lui-même été
construit en reprenant la structure de `drh-fpt` (voir
`Dpm-fpt/docs/adr/0001-adoption-pattern-drh-fpt.md`), et un troisième skill a
depuis suivi le même patron. Le pattern est donc éprouvé sur trois itérations.

Il manquait le volet **finances**, troisième pilier d'une direction générale de
collectivité. Deux architectures étaient disponibles :

- **`drh-fpt`** — sobre : `references/` (8 branches) + `assets/` + bundle
  mono-fichier pour le portage + CI de relecture ;
- **`dpm-fpt`** — riche : architecture en 4 couches (routeur, branches, objets,
  générateurs), `scripts/` de validation, packaging et évaluation, `vault/`
  Obsidian, `docs/adr/`.

## Décision

Adopter l'architecture **`dpm-fpt`**, complétée par les briques de gouvernance
que `dpm-fpt` n'a pas et que `drh-fpt` a : `LICENSE`, `.github/auto-review.*` et
le workflow de relecture automatique des pull requests.

Deux ajouts propres à ce dépôt :

1. un workflow `validate.yml` qui exécute réellement `validate_repo.py` en
   intégration continue — ni `drh-fpt` ni `dpm-fpt` ne branchaient leurs scripts
   de validation sur la CI ;
2. un `.claude-plugin/` (plugin + marketplace mono-plugin) sur le modèle de
   `droit-francais-skill`, pour que l'installation se fasse en une commande.

## Conséquences

- Le métier des finances se prête à la double taxonomie : des **branches**
  thématiques (budget, exécution, fiscalité, dette) et des **objets** qui sont
  des situations récurrentes traversant plusieurs branches (une régie, un
  emprunt, une subvention à une association). L'architecture riche est donc
  justifiée, pas décorative.
- Le coût de maintenance est plus élevé : 12 branches, 3 briques posture,
  8 objets, 5 générateurs, 3 scripts, un vault et un jeu de cas à tenir à jour.
- Le point 1 ci-dessus corrige une faiblesse observée : la copie déployée de
  `dpm-fpt` était restée deux versions en retard sur son dépôt, sans que rien ne
  le signale.

## Alternatives écartées

- **Architecture `drh-fpt` sobre** — écartée : sans couche « objets », une
  question comme « comment créer une régie » obligerait à dupliquer la même
  procédure dans trois branches.
- **Un skill unique « direction générale »** couvrant RH, finances et sécurité —
  écarté : la description d'activation deviendrait illisible et les frontières
  de délégation, qui sont le principal dispositif de sûreté de ces skills,
  disparaîtraient.
