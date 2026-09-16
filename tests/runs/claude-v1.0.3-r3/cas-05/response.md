Avant de parler taux, un point de compétence à ne pas laisser passer : le maire ne peut pas décider seul une hausse du taux de taxe foncière. Le vote des taux des impositions directes locales relève du **conseil municipal**, par une délibération fiscale **distincte** de la délibération budgétaire (`references/fiscalite-locale.md` §5.2). Le maire peut porter le projet et le présenter, mais l'acte de décision est celui de l'assemblée délibérante.

Cela posé, voici les contraintes à sécuriser, dans l'ordre où elles doivent être levées.

## 1. Qualifier ce qui est réellement voté

La taxe foncière recouvre deux impositions distinctes — TFPB (propriétés bâties) et TFPNB (propriétés non bâties) — assises sur la valeur locative cadastrale, à la charge du propriétaire, perçues par le bloc communal (`references/fiscalite-locale.md` §5.1). Premier point à clarifier avec le maire : s'agit-il de l'une, de l'autre, ou des deux ? Le taux se vote imposition par imposition.

## 2. Le calendrier — deux dates à ne pas confondre

- La délibération fiscale fixant les taux a sa **propre date limite**, fixée chaque année par le calendrier budgétaire et fiscal. Cette date n'est **pas automatiquement celle du budget** et je ne peux pas vous la donner de mémoire — elle relève d'une valeur volatile à vérifier chaque exercice (`references/fiscalite-locale.md` §5.2, §7 ; `references/socle-sources-verification.md` §5). ⚠️ non vérifié dans cette session : à confirmer auprès des services fiscaux ou sur Légifrance avant toute annonce de délai.
- Pour mémoire, et à titre de repère seulement : la date limite de vote du **budget primitif** (15 avril, 30 avril l'année de renouvellement de l'assemblée) est une donnée déjà vérifiée et consignée dans `references/references-verifiees.md` §1 (CGCT, art. L. 1612-2, vérifié le 2026-09-15). Mais c'est une date **budgétaire**, pas la date de la délibération fiscale elle-même — ne pas les confondre. La règle veut seulement que les taux soient en principe arrêtés avant ou concomitamment au budget, pour permettre l'inscription du produit attendu (`references/fiscalite-locale.md` §5.2) ; l'articulation précise entre les deux calendriers est, elle aussi, à vérifier pour l'exercice concerné.
- Un vote hors délai ou une absence de délibération entraîne en principe la reconduction des taux de l'exercice antérieur, mais le mécanisme exact est à vérifier avant d'être annoncé comme certain (`references/fiscalite-locale.md` §5.2, §8 piège 2).

## 3. La règle de lien entre les taux

Si l'intention du maire ne se limite pas au foncier et touche aussi, à terme, la cotisation foncière des entreprises (CFE), sachez que la hausse des taux « ménages » (dont la taxe foncière) conditionne le plafond de hausse autorisé pour la CFE (méthode de plafonnement de la variation relative). Un assouplissement de ce lien est possible mais suppose une délibération spécifique, dans des conditions à vérifier (`references/fiscalite-locale.md` §5.3). Pour une hausse limitée au seul foncier, ce point n'est qu'un point de vigilance pour l'avenir, pas un obstacle immédiat — mais il doit être testé avant toute présentation d'un scénario de hausse différenciée.

## 4. Un plafond légal existe, mais aucun chiffre ne peut être avancé ici

Le code général des impôts encadre le taux votable (plafonds, écarts avec la moyenne nationale ou départementale selon le mécanisme applicable à la TFPB/TFPNB). C'est une **valeur volatile** : je ne dispose d'aucun accès à une source officielle dans cette session pour la vérifier, donc je ne vous donne aucun chiffre de plafond — ce serait risquer de vous transmettre une valeur fausse ou obsolète (`SKILL.md` §5.4 ; `references/socle-sources-verification.md` §5, §8). Avant toute simulation chiffrée, faites vérifier ce plafond par vos services (CGI, ou BOFiP-Impôts) ou via `recherche-juridique`.

## 5. La méthode de simulation, elle, est stable

`produit attendu = base nette × taux`, imposition par imposition (`references/fiscalite-locale.md` §6). Pour construire le scénario de hausse :
1. récupérer l'état fiscal notifié par les services fiscaux (bases prévisionnelles, taux de l'exercice précédent, simulation à taux constant) ;
2. simuler le produit à taux constant puis à taux modifié ;
3. tester la règle de lien (§3 ci-dessus) si une variation différenciée d'autres taux est envisagée en parallèle ;
4. délibérer dans le délai applicable (à vérifier, §2) ;
5. transmettre la délibération au contrôle de légalité et aux services fiscaux.

Je n'ai ni le montant des bases, ni le taux actuellement voté, ni la date limite de cet exercice : ce sont des données à demander explicitement à vos services, jamais à déduire (`references/fiscalite-locale.md` §6).

## 6. La délibération est un acte soumis au contrôle de légalité

Compétence de l'organe, mentions obligatoires et transmission au représentant de l'État sont à vérifier avant toute production de l'acte (`references/controle-budgetaire.md` §6.4 ; `references/fiscalite-locale.md` §10). Si vous voulez, je peux construire le brouillon de cette délibération fiscale ou une note d'impact financier chiffrant l'effet de la hausse — sur la base du gabarit `references/templates/deliberation-budgetaire.md` (adapté à l'objet fiscal) ou `references/templates/note-impact-financier.md` : dans les deux cas, je vous poserai les questions une à une (bases, taux actuel, taux envisagé, exercice, date de délibération prévue) et je ne compléterai aucun champ par hypothèse.

## Synthèse des points à faire vérifier avant toute annonce au maire

- Date limite de la délibération fiscale pour cet exercice.
- Plafond légal du taux de TFPB/TFPNB applicable.
- Montant des bases notifiées et taux actuellement en vigueur.
- Effet exact d'un vote hors délai (reconduction ou autre règle).
- Le cas échéant, conditions d'assouplissement de la règle de lien si la CFE est aussi concernée.

**[Risque : élevé — un vote hors délai ou contraire au plafond expose à la nullité de la délibération ou à la reconduction des taux antérieurs / Confiance : stable sur le principe et la procédure, mais chaque valeur chiffrée et chaque date sont à revérifier pour cet exercice]** (`references/fiscalite-locale.md` §11).
