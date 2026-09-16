Une décision modificative se rédige avec le même générateur qu'un budget primitif (`references/templates/deliberation-budgetaire.md`), mais je ne peux pas l'assembler à partir du seul intitulé « DM n°2 ». Avant toute rédaction, ce générateur est subordonné à `references/controle-budgetaire.md` : la compétence de l'organe, l'équilibre réel et les mentions obligatoires doivent être vérifiées, et aucun montant, aucune imputation, aucune date ne peut être déduit ou inventé.

## Vérification préalable (garde-fous)

Rien dans votre demande ne signale ni un maniement de fonds hors circuit du comptable (STOP `SKILL.md` §5.2), ni un budget déjà voté en déséquilibre, un compte administratif en déficit excessif ou une dépense obligatoire non inscrite (ALERTE BUDGÉTAIRE `SKILL.md` §5.3, procédure détaillée dans `references/controle-budgetaire.md`). Aucun des deux hard stops n'est donc déclenché en l'état — mais ce point est à reconfirmer une fois les données de la DM connues, en particulier l'équilibre réel section par section (`references/budget-cycle.md` §6.1).

Pour rappel de doctrine (`references/budget-cycle.md` §5.4) : une décision modificative suit le **même formalisme** que le budget primitif (compétence de l'assemblée délibérante, respect du niveau de vote retenu) et reste soumise aux **mêmes principes budgétaires** — équilibre réel et sincérité en particulier. Une DM ne peut ni masquer un déséquilibre, ni inscrire des recettes ou dépenses fictives pour rétablir un équilibre apparent.

## Informations nécessaires pour assembler l'acte

Le générateur `references/templates/deliberation-budgetaire.md` impose de lever ces champs avant assemblage (§1 à §3 du fichier) — merci de me les préciser, un point d'attention à la fois si vous préférez procéder par étapes :

1. **Organe compétent et délégation** — conseil municipal, communautaire, départemental, régional (autre) ? L'objet relève-t-il d'une délégation déjà consentie à l'exécutif, ou du conseil lui-même ?
2. **Date de la séance** et conditions de convocation (délai respecté, note de synthèse jointe).
3. **Visas** — quels textes souhaitez-vous viser (délibération du budget primitif de l'exercice, délibération antérieure sur le même objet, rapport ou avis préalable) ? Aucun visa générique de type « vu le CGCT » sans article précis.
4. **Exposé des motifs** — contexte et motif exact de cette DM n°2 (ajustement de crédits, recette nouvelle, dépense imprévue, régularisation…).
5. **Dispositif article par article** — le ou les mouvements précis : section concernée (fonctionnement/investissement), chapitre, article, montant exact de chaque ligne modifiée.
6. **Cohérence avec les annexes** — si un état annexé (état de la dette, tableau des effectifs, etc.) accompagne la DM, les montants du corps de l'acte devront lui être strictement identiques.
7. **Transmission au contrôle de légalité** — circuit de transmission (dématérialisé ou autre) ; je pars du principe que la DM figure parmi les actes transmissibles (`references/budget-cycle.md` §10), sauf indication contraire à vérifier.
8. **Acte faisant grief** — cette DM affecte-t-elle directement un tiers identifié (par exemple une subvention réduite ou supprimée) ? Si oui, les voies et délais de recours devront figurer dans l'acte.

Aucune de ces données ne figure de mémoire ni ne peut être estimée : montant, imputation, date de séance et organe sont des champs bloquants au sens de `references/templates/deliberation-budgetaire.md` §4.

## Brouillon `[INCOMPLET]`

En l'état des informations disponibles, voici le squelette de l'acte, conforme au gabarit de `references/templates/deliberation-budgetaire.md` §2 :

```
[COLLECTIVITÉ — en-tête]

DÉLIBÉRATION N° [INCOMPLET — préciser : numéro de délibération] / [INCOMPLET — préciser : année/exercice]
[INCOMPLET — préciser : organe délibérant] — Séance du [INCOMPLET — préciser : date de séance]

Objet : Décision modificative n° 2 au budget [primitif / annexe concerné — à préciser] de l'exercice [INCOMPLET — préciser : exercice]

Le [organe délibérant], convoqué le [INCOMPLET — préciser : date de convocation],

VU [le CGCT, article fondant la compétence de l'organe en matière budgétaire — à confirmer en version consolidée] ;
VU [la délibération du budget primitif de l'exercice concerné — INCOMPLET, référence à préciser] ;
VU [le rapport ou la note de synthèse annexée à la convocation — INCOMPLET] ;

CONSIDÉRANT [le contexte et le motif de la présente décision modificative — INCOMPLET — préciser : exposé des motifs] ;
CONSIDÉRANT [l'absence d'incidence sur l'équilibre réel du budget, ou le lien avec une procédure de régularisation en cours — à vérifier, renvoi references/controle-budgetaire.md] ;

Après en avoir délibéré,

DÉCIDE :

Article 1er — [INCOMPLET — préciser : dispositif exact de chaque mouvement de crédits (recettes et dépenses)].
Article 2 — Incidence financière : section [INCOMPLET], chapitre [INCOMPLET], article [INCOMPLET], montant [INCOMPLET — aucun chiffre ne peut être déduit ni arrondi].
Article 3 — [INCOMPLET — préciser si l'acte fait grief à un tiers identifié ; si oui, voies et délais de recours obligatoires ; si non, « Sans objet »].
Article 4 — [Autorité chargée de l'exécution] est chargé(e) de l'exécution de la présente délibération, qui sera publiée et transmise au représentant de l'État au titre du contrôle de légalité selon le circuit [INCOMPLET].

Fait à [lieu], le [date].
[Signature de l'autorité exécutive]

Annexes le cas échéant : [état de crédits modifiés — vérifier la cohérence des montants avec le corps de l'acte].
```

---
## CHAMPS MANQUANTS — DÉLIBÉRATION NON FINALISABLE EN L'ÉTAT

Les informations suivantes sont requises avant inscription à l'ordre du jour et vote :
- organe délibérant compétent et existence éventuelle d'une délégation
- date de la séance et conditions de convocation
- exercice budgétaire concerné
- visas précis (délibération du budget primitif, texte spécial le cas échéant)
- exposé des motifs de la DM n°2
- dispositif chiffré, ligne par ligne (section, chapitre, article, montant)
- caractère faisant grief ou non de l'acte
- circuit et confirmation de la transmission au contrôle de légalité
- numéro de délibération et lieu/date de signature

Cette délibération ne doit être ni présentée en séance, ni transmise au contrôle de légalité, tant que ces champs ne sont pas renseignés (`references/templates/deliberation-budgetaire.md` §4).

## Point de vigilance sourcing

Aucun numéro d'article de CGCT, aucun délai de transmission au contrôle de légalité et aucun seuil n'ont été cités : ce sont des lignes « Oui » de la matrice de vérification (`SKILL.md` §2.2) et la session ne permet aucun appel à une source officielle pour les confirmer. Ils sont donc marqués « à confirmer en version consolidée » plutôt qu'énoncés (`SKILL.md` §5.4). Dès que vous aurez confirmé l'organe et le calendrier, faites vérifier via `recherche-juridique` : la référence exacte de compétence (CGCT) et le délai de transmission applicable à une décision modificative.

**[Risque : Élevé / Confiance : à vérifier systématiquement]** — toute délibération budgétaire est un acte soumis au contrôle de légalité ; la compétence de l'organe, l'imputation et l'équilibre réel doivent être vérifiés avant tout vote (`references/controle-budgetaire.md`, `references/budget-cycle.md` §5.4).

Dites-moi l'organe compétent et l'exercice concerné pour commencer, je poursuis ensuite avec les autres champs un à un.
