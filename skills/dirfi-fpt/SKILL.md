---
name: dirfi-fpt
description: >-
  Système expert d'aide à la décision pour un Directeur des Finances (DirFi) en
  collectivité territoriale française. Activer pour toute question de finances
  publiques locales : cycle budgétaire et vote du budget, nomenclature M57,
  exécution de la dépense et de la recette, régies, fiscalité locale, dotations
  et péréquation, dette et trésorerie, prospective et analyse financière,
  subventions, volet financier de la commande publique, contrôle interne
  financier et écrits budgétaires. Activer aussi lorsqu'un montage fait manier
  des deniers publics hors du circuit du comptable public, afin d'opposer le
  garde-fou gestion de fait, ou lorsqu'un acte budgétaire paraît irrégulier,
  afin d'opposer le garde-fou budgétaire avant toute recommandation
  d'exécution. Vérifier toute règle de droit et toute valeur chiffrée sur une
  source officielle avant conclusion. Ne pas activer pour le RH statutaire des
  agents (carrière, paie, régime indemnitaire : drh-fpt), pour la passation des
  marchés publics, ni pour le droit étranger.
---

# Adaptateur plugin

Ce point d'entrée rend le skill disponible dans le paquet plugin sans le
dupliquer ni modifier son mode d'installation autonome.

Avant toute analyse financière, lire intégralement
[`../../SKILL.md`](../../SKILL.md) et appliquer ses instructions — en
particulier ses deux garde-fous (§5.2 ordonnateur/comptable, §5.3 budgétaire)
et son régime des valeurs chiffrées (§5.4). Résoudre ensuite ses références
relativement à la racine du dépôt : `references/`, `references/templates/` et
`objets/`, qui restent l'unique source de vérité.

Si le fichier cible est absent ou illisible, signaler que l'installation du
plugin est incomplète. **Ne pas improviser** de règle budgétaire, de valeur
chiffrée ni d'identifiant officiel pour compenser : c'est exactement ce que le
skill existe pour empêcher.
