---
tags: [skill/dirfi-fpt, maillage]
version: 1.0.4
date: 2026-09-15
---

# Maillage — carte des liens croisés

> Complément de [[index-dirfi-fpt]]. L'index répond à « où est-ce ? ». Ce
> fichier répond à « qu'est-ce que ça touche ? ». Aucun contenu métier :
> uniquement la topologie.
>
> Usage : avant de modifier une branche, vérifier ici ce qui pointe vers elle.
> Avant d'ajouter un objet, vérifier qu'il agrège des branches existantes
> plutôt qu'il n'en duplique une.

---

## 1. Nœuds transverses

Trois nœuds traversent presque tout le graphe. Une modification qui les touche
se répercute partout.

### Garde-fou ordonnateur / comptable

**Source normative** : `../SKILL.md` §5.2 · **Détecteur** :
`../references/analyse-situation.md` §0 détecteur A.

Branches qui peuvent le déclencher : `execution-recette.md` (encaissement hors
régie), `execution-depense.md` (mandat sans service fait, avance irrégulière),
`subventions.md` (subvention rémunérant une prestation, association
transparente), `controle-interne-financier.md` (prévention, cas typiques).

Objets concernés : [[#objet-regie]], [[#objet-subvention-association]],
[[#objet-satellites]].

Traitement de fond : `../references/contentieux-financier.md` (conséquences
juridictionnelles).

### Garde-fou budgétaire

**Source normative** : `../SKILL.md` §5.3 · **Détecteur** :
`../references/analyse-situation.md` §0 détecteur B.

Branches qui peuvent le déclencher : `budget-cycle.md` (vote, équilibre,
calendrier), `execution-depense.md` (dépense sans crédit, dépense obligatoire),
`nomenclature-m57.md` (provision obligatoire absente),
`prospective-analyse.md` (déséquilibre structurel détecté).

Traitement de fond : `../references/controle-budgetaire.md`.

### Frontière `drh-fpt`

**Source normative** : `../SKILL.md` §5.5 · **Détecteur** :
`../references/analyse-situation.md` §3.

Branche la plus exposée : `prospective-analyse.md` (pilotage de la masse
salariale). Exposition secondaire : `budget-cycle.md` (chapitre 012 au budget),
`execution-depense.md` (imputation d'une dépense de personnel).

Règle : l'enveloppe, le coût et l'imputation restent ici ; le droit individuel
et la procédure statutaire basculent.

### Socle de vérification

`../references/socle-sources-verification.md` est appelé par **toutes** les
branches via leur section 7 (« Déclencheurs de vérification ») et leur section 9
(« Données / valeurs à vérifier »). Ses deux registres
(`references-verifiees.md`, `cache-taux-seuils.md`) ne sont jamais cités
directement dans une réponse.

---

## 2. Objets → branches mobilisées

<a id="objet-subvention-association"></a>
### Subvention à une association

`../objets/subvention-association.md`

| Dimension | Renvoi |
|---|---|
| Règles de fond | `subventions.md` |
| Qualification du flux (subvention vs achat) | `subventions.md`, `commande-publique-financiere.md` |
| Inscription et imputation | `budget-cycle.md`, `nomenclature-m57.md` |
| Versement | `execution-depense.md` |
| Reversement en cas de non-exécution | `execution-recette.md` |
| Garde-fou applicable | §5.2 (association transparente, prestation déguisée) |
| Générateur | `templates/convention-subvention.md` |

<a id="objet-regie"></a>
### Régie

`../objets/regie.md`

| Dimension | Renvoi |
|---|---|
| Règles de fond (recettes) | `execution-recette.md` |
| Règles de fond (avances) | `execution-depense.md` |
| Contrôles, responsabilité du régisseur | `controle-interne-financier.md` |
| Conséquences d'une irrégularité | `contentieux-financier.md` |
| Garde-fou applicable | §5.2 — **la régie est la seule voie régulière** de maniement de fonds par un agent |
| Générateur | `templates/fiche-procedure-financiere.md` |

<a id="objet-emprunt"></a>
### Emprunt

`../objets/emprunt.md`

| Dimension | Renvoi |
|---|---|
| Règles de fond | `dette-tresorerie.md` |
| Compétence et délégation | `budget-cycle.md` |
| Soutenabilité, ratios | `prospective-analyse.md` |
| Imputation et annexes | `nomenclature-m57.md` |
| Générateur | `templates/deliberation-budgetaire.md` |

<a id="objet-operation-investissement"></a>
### Opération d'investissement

`../objets/operation-investissement.md`

| Dimension | Renvoi |
|---|---|
| AP/CP, inscription | `budget-cycle.md` |
| Programmation, plan de financement | `prospective-analyse.md` |
| Financement externe | `subventions.md`, `dotations-perequation.md` (FCTVA) |
| Financement par emprunt | `dette-tresorerie.md` |
| Exécution financière du marché | `commande-publique-financiere.md` |
| Entrée du bien à l'actif | `nomenclature-m57.md` |
| Générateur | `templates/note-impact-financier.md` |

<a id="objet-cloture-exercice"></a>
### Clôture de l'exercice

`../objets/cloture-exercice.md`

| Dimension | Renvoi |
|---|---|
| Calendrier, compte administratif, affectation du résultat | `budget-cycle.md` |
| Rattachement, restes à réaliser, provisions | `nomenclature-m57.md` |
| Mandatements de fin d'exercice | `execution-depense.md` |
| Titres et non-valeurs | `execution-recette.md` |
| Risque de déficit | `controle-budgetaire.md` |

<a id="objet-satellites"></a>
### Satellites

`../objets/satellites.md`

| Dimension | Renvoi |
|---|---|
| Budgets annexes, autonomie financière | `nomenclature-m57.md`, `budget-cycle.md` |
| Subventions et participations versées | `subventions.md` |
| Contrôle des organismes | `controle-interne-financier.md` |
| Garanties d'emprunt accordées | `dette-tresorerie.md` |
| Garde-fou applicable | §5.2 — association transparente, para-administration |

<a id="objet-immobilisation"></a>
### Immobilisation

`../objets/immobilisation.md`

| Dimension | Renvoi |
|---|---|
| Règles de fond | `nomenclature-m57.md` |
| Acquisition | `execution-depense.md`, `commande-publique-financiere.md` |
| Cession | `execution-recette.md` |
| Éligibilité FCTVA | `dotations-perequation.md` |

<a id="objet-marche-public"></a>
### Marché public (volet financier)

`../objets/marche-public.md`

| Dimension | Renvoi |
|---|---|
| Règles de fond | `commande-publique-financiere.md` |
| Engagement comptable, imputation | `nomenclature-m57.md` |
| Paiement, délais, pièces | `execution-depense.md` |
| Pluriannualité | `budget-cycle.md` |
| Frontière | **passation hors périmètre** (`SKILL.md` §5.6) |

---

## 3. Générateurs → branches pilotes

| Générateur | Piloté par | Branches de fond |
|---|---|---|
| `templates/deliberation-budgetaire.md` | `ecrits-financiers.md` | `budget-cycle.md`, `controle-budgetaire.md` |
| `templates/rapport-orientation-budgetaire.md` | `ecrits-financiers.md` | `budget-cycle.md`, `prospective-analyse.md`, `dette-tresorerie.md` |
| `templates/note-impact-financier.md` | `ecrits-financiers.md` | `prospective-analyse.md`, `nomenclature-m57.md` |
| `templates/convention-subvention.md` | `ecrits-financiers.md` | `subventions.md` |
| `templates/fiche-procedure-financiere.md` | `ecrits-financiers.md` | `controle-interne-financier.md` |

---

## 4. Couverture du maillage

| Contrôle | État |
|---|---|
| Objets rattachés à au moins deux branches | 8 / 8 |
| Objets couverts par un générateur | 6 / 8 (`cloture-exercice`, `satellites` : pas d'écrit dédié) |
| Branches atteintes par au moins un objet | 11 / 12 (`fiscalite-locale` : aucun objet dédié en v1.0.0) |
| Garde-fous rattachés à leur branche de traitement | 3 / 3 |
| Générateurs pilotés par une branche | 5 / 5 |

**Lacunes assumées en v1.0.0**, à réexaminer au fil du `JOURNAL.md` :

- pas d'objet « vote des taux » rattaché à `fiscalite-locale.md` ;
- pas de générateur pour la clôture d'exercice ni pour le suivi des satellites.
