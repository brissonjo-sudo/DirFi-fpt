# Brique posture — RETEX (retour d'expérience) (v0.1.0)

> Brique transverse, pas une branche métier. Structure adaptée du gabarit
> `_gabarit-branche.md` — les 12 sections sont conservées et numérotées dans
> l'ordre, mais **certaines n'ont pas d'objet** pour un outil de méthode :
> chacune le signale en une ligne plutôt que de forcer un contenu. **Aucune
> base légale propre** : le RETEX analyse un cas déjà traité sous le
> fondement mobilisé au moment des faits ; ce fondement se vérifie et se cite
> dans la branche de fond concernée, jamais ici.

## Périmètre / Exclusions

- **Périmètre** : capitaliser sur un **cas financier déjà traité** —
  incident, lacune méthodologique, cas nouveau, écrit récurrent — pour
  alimenter `JOURNAL.md` et, le cas échéant, `CHANGELOG.md` ; structurer la
  **revue annuelle** du skill (`SKILL.md` §9).
- **Exclusions** : la **procédure de contrôle budgétaire** proprement dite →
  `controle-budgetaire.md`. La **responsabilité financière et la gestion de
  fait** → `contentieux-financier.md`. Le **fond** de chaque règle financière
  traversée par le cas analysé → la branche métier concernée
  (`references/budget-cycle.md`, `references/execution-depense.md`, etc.).
  La **procédure disciplinaire** individuelle → `drh-fpt`.

---

## 1. Questions couvertes

- « Ce cas mérite-t-il une entrée `JOURNAL.md` ? »
- « Comment analyser un rejet du comptable qui se répète ? Un dépassement de
  crédit ? Un retard de mandatement ? Une subvention mal qualifiée ? Un écart
  de prospective ? »
- « Comment faire remonter un enseignement du `JOURNAL.md` vers une évolution
  versionnée du skill (`CHANGELOG.md`) ? »
- « Que couvre la revue de janvier ? Et celle du 1er septembre ? »
- « Comment anonymiser un cas avant de le consigner ? »
- « Quel format donner à une entrée de journal ? »

---

## 2. Arbre de traitement

`cas clos → qualifier s'il est journalisable (§4) → dérouler la grille
d'analyse si c'est un incident (§5) → rédiger l'entrée `JOURNAL.md` au format
imposé (§6) → apprécier si l'enseignement dépasse le cas d'espèce et appelle
une évolution du skill (§7) → le cas échéant, ouvrir une entrée
`CHANGELOG.md` (et une ADR si la décision est structurante) → verser le cas
à la revue annuelle qui vient (§8)`

Ne jamais consigner un cas sans être passé par l'anonymisation (§9) : la
capitalisation n'autorise aucune exception à cette règle.

---

## 3. Variables à lever

- **Nature du cas** : incident récurrent (§5), lacune identifiée dans une
  branche, cas nouveau non couvert par le skill, ou simple écrit produit de
  façon répétée qui gagnerait à être un gabarit.
- **Caractère isolé ou répété** : un incident isolé peut rester une note
  interne au service ; un incident qui se répète (même type de rejet, même
  erreur d'imputation) devient journalisable de plein droit (§4).
- **Portée de l'enseignement** : correction ponctuelle (une réponse
  mal calibrée) ou évolution de méthode (une règle absente, une frontière mal
  posée) — cette distinction oriente vers `JOURNAL.md` seul ou vers
  `JOURNAL.md` **et** `CHANGELOG.md`.
- **Présence de données sensibles** dans le cas à consigner : montant
  précis, nom d'un agent, d'un élu, d'un administré ou d'un bénéficiaire de
  subvention — à traiter systématiquement avant rédaction (§9).

---

## 4. Ce qui mérite une entrée `JOURNAL.md`

Journaliser dès que l'une de ces conditions est réunie :

- une **lacune** du skill est apparue (branche muette sur un cas réel, règle
  absente, renvoi manquant) ;
- une **erreur** a été produite (mauvaise autorité identifiée, mauvaise
  section, valeur non vérifiée pourtant citée) ;
- un **cas nouveau**, non couvert explicitement par une branche existante,
  s'est présenté ;
- un **écrit récurrent** a été demandé plusieurs fois sous une forme proche,
  signalant un gabarit à formaliser ou à enrichir dans
  `references/templates/`.

Ne pas journaliser un cas parfaitement couvert par le skill et traité sans
écart : la valeur du `JOURNAL.md` est dans l'écart, pas dans la routine.

---

## 5. Grille d'analyse d'un incident financier

Dérouler dans l'ordre pour tout incident soumis à RETEX :

| Étape | Contenu |
|---|---|
| 1. Chronologie factuelle | Reconstituer les faits datés : détection, décision prise, échange avec le comptable ou la CRC le cas échéant, issue. Distinguer ce qui est établi de ce qui reste incertain. |
| 2. Catégorisation | Rattacher l'incident à un type : rejet du comptable répété, dépassement de crédit, retard de mandatement, subvention mal qualifiée, écart de prospective, ou autre. |
| 3. Cause | Identifier la cause : imputation erronée, absence de crédit ouvert, délai de circuit interne, qualification insuffisante d'une convention, hypothèse de prospective non actualisée. |
| 4. Ce qui a fonctionné | Ce qui a permis de détecter ou de limiter l'incident (contrôle interne, alerte, relecture). |
| 5. Risque résiduel | La cause identifiée est-elle susceptible de se reproduire ? Sur quel autre dossier ? |
| 6. Action correctrice | Objet précis, pilote (fonction, pas de nom propre), échéance, critère de vérification. |

**Repères par type d'incident** :
- **Rejet du comptable répété** : vérifier si la cause est une pièce
  justificative manquante récurrente, une imputation erronée récurrente, ou
  un défaut de dialogue en amont avec le comptable assignataire — chaque
  cause appelle une action correctrice différente.
- **Dépassement de crédit** : distinguer l'engagement sans crédit ouvert
  (garde-fou budgétaire potentiel, `controle-budgetaire.md`) d'un simple
  retard de décision modificative.
- **Retard de mandatement** : vérifier s'il expose à un intérêt moratoire ou
  à un contentieux de la commande publique — articuler avec
  `references/commande-publique-financiere.md` si pertinent.
- **Subvention mal qualifiée** : vérifier si la requalification en commande
  publique, ou le risque de rémunération déguisée d'une prestation, a été
  identifié à temps — articuler avec le garde-fou `SKILL.md` §5.2 si le
  risque touche à une immixtion dans le maniement de fonds.
- **Écart de prospective** : identifier si l'écart tient à une hypothèse
  macro-économique dépassée, à un fait nouveau (réforme, dotation), ou à une
  erreur de méthode — verser l'enseignement à
  `references/prospective-analyse.md` si la méthode elle-même doit évoluer.

---

## 6. Format d'une entrée de journal

Une entrée `JOURNAL.md` comporte, a minima :

```
### [date] — [titre court du cas]

**Type** : incident récurrent / lacune / cas nouveau / écrit récurrent
**Branche(s) concernée(s)** : [pointeur(s) vers references/*.md]
**Constat** : [1 à 3 phrases, faits anonymisés]
**Cause identifiée** : [1 phrase]
**Action** : [correction apportée au skill, ou action correctrice interne à
la collectivité, avec pilote-fonction et échéance]
**Suite** : [CHANGELOG.md vX.Y.Z / ADR-xxxx / sans suite versionnée]
```

Une entrée sans **action** n'est qu'un constat : elle reste incomplète tant
qu'aucune suite (correction du skill, ou renvoi interne) n'est indiquée.

---

## 7. La boucle `JOURNAL.md` → `CHANGELOG.md`

- Toute entrée `JOURNAL.md` qui révèle une **lacune de méthode** (pas
  seulement une erreur d'espèce) est candidate à une évolution du skill.
- L'évolution se traduit par une modification versionnée d'une branche ou
  d'une brique, consignée dans `CHANGELOG.md` selon le versionnage sémantique
  MAJEUR.MINEUR.PATCH (`SKILL.md` §9).
- Une décision structurante (nouvelle frontière, nouveau garde-fou, refonte
  d'une branche) donne lieu, en plus, à une **ADR** dans `docs/adr/`.
- **Traçabilité attendue** : chaque entrée `CHANGELOG.md` issue d'un RETEX
  pointe vers l'entrée `JOURNAL.md` d'origine, pour garder la chaîne cas
  réel → enseignement → évolution du skill.

---

## 8. Revue annuelle

| Revue | Période | Contenu |
|---|---|---|
| **Revue de loi de finances** | Janvier | Dispositions fiscales et de dotations de la loi de finances de l'année, seuils de la commande publique, taux du FCTVA, évolutions de la nomenclature M57 (`SKILL.md` §9). |
| **Revue de rentrée** | 1er septembre | CGCT (volet budgétaire et comptable), code des juridictions financières, instruction M57, jurisprudence financière de l'année ; revue systématique du `JOURNAL.md` accumulé depuis la revue précédente (`SKILL.md` §9). |

**Méthode pour la revue de rentrée** : reparcourir les entrées `JOURNAL.md`
de la période, regrouper celles qui pointent vers la même branche ou la même
lacune, et arbitrer, pour chaque regroupement, si une évolution versionnée
est nécessaire ou si le constat reste isolé.

---

## 9. Règles d'anonymisation

- **Aucune donnée nominative** : ni agent, ni élu, ni administré, ni
  bénéficiaire de subvention nommé, y compris dans les exemples ou les
  citations de courrier.
- **Montants** : conserver l'ordre de grandeur utile à l'analyse (faible,
  significatif, majeur au regard du budget) plutôt que le montant exact d'un
  dossier identifiable, sauf si le montant précis est indispensable à la
  compréhension de la cause et ne permet pas, par recoupement, d'identifier
  le tiers.
- **Dates** : conserver le mois et l'exercice, pas nécessairement le jour
  exact, sauf si la chronologie fine est l'objet même de l'enseignement
  (ex. délai de circuit interne).
- **Structure identifiable** : éviter de nommer un service, une direction ou
  un satellite d'une manière qui permettrait de reconstituer l'identité des
  personnes impliquées par simple recoupement.

---

## 10. Sections sans objet pour cette brique

Le gabarit prévoit des sections qui n'ont pas de contenu propre pour un
outil de méthode :

- **Règles métier** (point 5 du gabarit) : pas de règle de fond ici — voir
  §5 ci-dessus qui en tient lieu sous une forme adaptée (grille d'analyse).
- **Déclencheurs de vérification** (point 7 du gabarit) : le RETEX n'a pas
  de base légale propre à vérifier ; tout point de droit traversé par un cas
  analysé se vérifie dans la branche de fond concernée, jamais ici.
- **Données / valeurs à vérifier** (point 9 du gabarit) : par construction,
  aucune valeur chiffrée ni aucun article n'est cité dans cette brique.
- **Écrits & livrables** (point 10 du gabarit) : cette brique ne produit pas
  d'écrit externe à la collectivité ; son seul livrable est l'entrée de
  journal (§6), interne au skill.

---

## 11. Double échelle [risque / confiance]

- **Cas traité sans écart, versé au `JOURNAL.md` pour mémoire** : [risque
  faible / confiance stable] — aucune vérification de source nécessaire.
- **Incident financier récurrent (rejet, dépassement, retard, subvention mal
  qualifiée, écart de prospective)** : [risque moyen / confiance stable sur
  la méthode d'analyse, à vérifier sur tout point de droit traversé] —
  vérifier la branche de fond avant de qualifier une cause comme non
  conforme à une règle.
- **Cas touchant un volet potentiellement contentieux ou disciplinaire** :
  [risque élevé / à vérifier] — cloisonner le RETEX (méthode) du volet
  procédure (`contentieux-financier.md`, `drh-fpt`) ; ne jamais laisser le
  RETEX trancher une responsabilité.

---

## 12. Checklist de branche

1. Le cas a-t-il été qualifié comme journalisable selon les critères de §4 ?
2. Pour un incident, la **chronologie factuelle** a-t-elle précédé toute
   préconisation (§5, étape 1) ?
3. Le type d'incident a-t-il été catégorisé (§5) parmi les cas types
   (rejet, dépassement, retard, subvention, prospective) ou explicitement
   qualifié d'« autre » ?
4. L'entrée respecte-t-elle le **format imposé** (§6), avec une action et
   une suite renseignées ?
5. La bascule vers `CHANGELOG.md` (et, si besoin, une ADR) a-t-elle été
   envisagée pour tout enseignement dépassant le cas d'espèce (§7) ?
6. L'**anonymisation** (§9) a-t-elle été appliquée avant toute rédaction,
   sans exception ?
7. Aucune base légale n'a-t-elle été citée de mémoire dans le RETEX
   lui-même, tout point de droit traversé étant renvoyé à la branche de
   fond ?
8. La distinction avec `contentieux-financier.md` (responsabilité,
   contentieux) et `controle-budgetaire.md` (procédure préventive) a-t-elle
   été maintenue, sans que le RETEX ne tranche à leur place ?
9. Le cas a-t-il été situé par rapport à la prochaine **revue annuelle**
   applicable (§8) ?
10. Couple **[risque / confiance]** (§11) indiqué selon le sous-cas ?

[risque / confiance] : risque variable selon le déclencheur (faible à élevé,
§11) — confiance stable sur la méthode de structuration ; vérification
obligatoire dès que le RETEX traverse un point de droit ou de procédure
relevant d'une autre branche.
