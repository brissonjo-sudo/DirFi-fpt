---
tags: [skill/dirfi-fpt, index]
version: 1.0.0
date: 2026-09-15
---

# Index — skill `dirfi-fpt`

> Hub de navigation du dépôt. **Aucun contenu métier ici** : uniquement des
> pointeurs. Le vault n'est pas packagé à l'exécution (`package_skill.py`
> l'exclut). Toute note du vault renvoie à cet index, et cet index les liste
> toutes.
>
> Principe : **1 besoin = 1 fichier**. Si un besoin mène à deux fichiers, c'est
> que le maillage est à revoir → [[maillage]].

---

## Couche 1 — routeur

| Besoin | Fichier repo |
|---|---|
| Qualifier une situation, détecter les garde-fous, orienter | `../references/analyse-situation.md` |

## Couche 2 — branches métier

| Besoin | Fichier repo |
|---|---|
| Voter, modifier, clôturer un budget ; DOB, DM, compte administratif, AP/CP | `../references/budget-cycle.md` |
| Imputer, amortir, provisionner, rattacher, inventorier | `../references/nomenclature-m57.md` |
| Engager, liquider, mandater ; service fait, délais de paiement | `../references/execution-depense.md` |
| Émettre un titre, recouvrer, admettre en non-valeur, tenir une régie | `../references/execution-recette.md` |
| Voter des taux, lire les états fiscaux, gérer exonérations et abattements | `../references/fiscalite-locale.md` |
| Comprendre la DGF, la péréquation, le FCTVA, les dotations d'investissement | `../references/dotations-perequation.md` |
| Emprunter, gérer la dette, mobiliser une ligne de trésorerie, garantir | `../references/dette-tresorerie.md` |
| Calculer l'épargne et les ratios, bâtir une prospective ou un PPI | `../references/prospective-analyse.md` |
| Verser ou percevoir une subvention, conventionner, contrôler | `../references/subventions.md` |
| Payer un marché : avance, acompte, révision, garantie, pénalité | `../references/commande-publique-financiere.md` |
| Organiser le contrôle interne, traiter un rejet, dématérialiser | `../references/controle-interne-financier.md` |
| Choisir et produire le bon écrit financier | `../references/ecrits-financiers.md` |

## Couche 2 bis — briques posture (transverses)

| Besoin | Fichier repo |
|---|---|
| Budget non voté, déséquilibre, déficit, dépense obligatoire, saisine CRC | `../references/controle-budgetaire.md` |
| Responsabilité financière, gestion de fait, juridictions financières | `../references/contentieux-financier.md` |
| Capitaliser un cas, alimenter le journal, préparer la revue annuelle | `../references/retex.md` |

## Socle de vérification

| Besoin | Fichier repo |
|---|---|
| Carte des sources, hiérarchie, régime des valeurs chiffrées, provenance | `../references/socle-sources-verification.md` |
| Registre des identifiants **réellement vérifiés** et datés | `../references/references-verifiees.md` |
| Cache de maintenance des valeurs chiffrées (non packagé, jamais citable) | `../references/cache-taux-seuils.md` |

## Couche 3 — objets métier

| Situation type | Fichier repo |
|---|---|
| Verser une subvention à une association | `../objets/subvention-association.md` |
| Créer et faire vivre une régie | `../objets/regie.md` |
| Contracter et gérer un emprunt | `../objets/emprunt.md` |
| Monter une opération d'investissement | `../objets/operation-investissement.md` |
| Clôturer l'exercice | `../objets/cloture-exercice.md` |
| Piloter un satellite (budget annexe, CCAS, SEM, SPL, DSP) | `../objets/satellites.md` |
| Gérer une immobilisation, de l'entrée à la sortie | `../objets/immobilisation.md` |
| Suivre le volet financier d'un marché | `../objets/marche-public.md` |

## Couche 4 — générateurs d'écrits

| Écrit | Fichier repo |
|---|---|
| Délibération budgétaire | `../references/templates/deliberation-budgetaire.md` |
| Rapport d'orientation budgétaire | `../references/templates/rapport-orientation-budgetaire.md` |
| Note d'impact financier | `../references/templates/note-impact-financier.md` |
| Convention de subvention | `../references/templates/convention-subvention.md` |
| Fiche de procédure financière | `../references/templates/fiche-procedure-financiere.md` |

## Gabarits (méta-documents, non métier)

| Besoin | Fichier repo |
|---|---|
| Structure imposée d'une branche (12 sections) | `../references/_gabarit-branche.md` |
| Structure imposée d'un objet (6 sections) | `../objets/_gabarit-objet.md` |

## Hors couches — gouvernance, outillage et tests

| Besoin | Fichier repo |
|---|---|
| Noyau : déclenchement, posture, garde-fous, frontières | `../SKILL.md` |
| Contraintes de contribution non négociables | `../AGENTS.md` |
| Décisions d'architecture | `../docs/adr/` |
| Historique des versions | `../CHANGELOG.md` |
| Cas remontés du terrain, anonymisés | `../JOURNAL.md` |
| Validation statique du dépôt | `../scripts/validate_repo.py` |
| Archive de portage déterministe | `../scripts/package_skill.py` |
| Préparation et dépouillement des campagnes d'évaluation | `../scripts/eval_suite.py` |
| Jeu de cas de test | `../tests/cas-de-test.json` |

---

## Notes du vault

- [[maillage]] — carte des liens croisés entre objets, branches et générateurs.

---

## Les deux garde-fous, en un coup d'œil

| Garde-fou | Déclencheur | Sortie | Fichier de traitement |
|---|---|---|---|
| **Ordonnateur / comptable** | Maniement de fonds hors circuit du comptable | `STOP` avant tout contenu | `../references/controle-interne-financier.md`, `../objets/regie.md` |
| **Budgétaire** | Budget non voté, déséquilibre, déficit, dépense obligatoire omise | `ALERTE BUDGÉTAIRE` avant tout contenu | `../references/controle-budgetaire.md` |
| **Frontière RH** | Droit individuel, régime indemnitaire, procédure statutaire | `BASCULE drh-fpt` avant tout contenu | skill `drh-fpt` |

Détail normatif → `../SKILL.md` §5.2, §5.3, §5.5.
