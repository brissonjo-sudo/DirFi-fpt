# Rapport de campagne — `claude-v1.0.3-r3`

**Date** : 2026-09-16 · **Version mesurée** : **1.0.3** · **28 cas**

## Protocole

Identique à `r1` et `r2` : 28 répondants isolés (un agent par cas, ne recevant
que `prompt.md`), 4 juges recevant prompt, réponse, attendus et barème, sans le
skill. **Même empreinte de suite SHA-256 qu'en `r1` et `r2`**
(`07b7b4a1…65e6ce7`) — la comparaison des trois campagnes est valide.

**Limite déclarée** : skill **lu depuis le dépôt**, non invoqué nativement.

**Ce que mesure cette campagne** : deux correctifs à la fois, tous deux
postérieurs à `r2` — le correctif de fond de la **v1.0.2** sur l'effet de la
saisine de la chambre régionale des comptes, et le correctif de traçabilité de
la **v1.0.3**. Leurs effets se lisent sur des cas distincts, ce qui permet de
les attribuer séparément.

## Résultat

| Verdict | `r1` (v1.0.0) | `r2` (v1.0.1) | `r3` (v1.0.3) |
|---|---|---|---|
| RÉUSSITE | 16 | 20 | **27** |
| DEMI-RÉUSSITE | 5 | 7 | **1** |
| ÉCHEC | 7 | 1 | **0** |
| dont critiques | 3 | 1 | **0** |

**Le seuil de release est atteint pour la première fois** : ≥ 25 RÉUSSITE sur 28
**et** zéro échec sur les neuf cas critiques (13, 18, 22, 23, 24, 25, 26, 27,
28), tous en RÉUSSITE.

Seul le cas 7 reste en DEMI-RÉUSSITE.

## Aucune régression

Le tableau cas par cas est sans exception : **tout cas classé RÉUSSITE en `r2`
l'est encore en `r3`**, et tout cas qui ne l'était pas a progressé.

| Cas | `r2` | `r3` | Ce qui a changé |
|---|---|---|---|
| 13 | ÉCHEC | **RÉUSSITE** | correctif de fond v1.0.2 |
| 1, 2, 4, 10, 12, 17 | DEMI | **RÉUSSITE** | correctif de traçabilité v1.0.3 |
| 7 | DEMI | DEMI | trois attendus métier manquants |
| les 21 autres | RÉUSSITE | RÉUSSITE | — |

## Le correctif de fond a purgé le dernier échec

Le cas 13 était le seul échec de `r2`, et il portait sur un cas critique. Le
skill y affirmait que la saisine de la chambre régionale des comptes ne
dessaisit pas l'assemblée, ce qui est faux pour le cas le plus fréquent. La
**v1.0.2** a distingué les deux fondements — dessaisissement sur budget non voté
(CGCT, art. L. 1612-2), maintien de la compétence sur déséquilibre réel
(art. L. 1612-5). Le cas passe en RÉUSSITE.

C'est le second cas, après ceux de `r1`, où **seule la suite de tests a trouvé
l'erreur** : la branche était bien formée, tous les contrôles statiques
passaient, et elle était fausse.

## Le correctif de traçabilité a converti six demi-réussites sur sept

La cause dominante des demi-réussites de `r1` et de `r2` était la même, relevée
indépendamment par les quatre juges des deux campagnes : **les réponses
nommaient la notion, jamais le fichier**. Cette exigence ne figurait que dans le
jeu de test — elle était mesurée sans être prescrite.

La **v1.0.3** l'a portée dans le skill (`SKILL.md` §4, et point 16 de
l'auto-vérification §7). Six des sept demi-réussites de `r2` passent en
RÉUSSITE. Le renvoi de fichier n'est plus relevé comme manquant sur aucun cas
du run.

## Le seul cas restant : 7

Le cas 7 n'est **pas** un défaut de traçabilité ni de provenance. Le fond est
correct — la ligne de trésorerie est bien l'instrument désigné, la compétence et
la délégation sont traitées, aucune valeur n'est inventée, aucun critère
éliminatoire n'est déclenché. Trois attendus métier manquent :

1. le **caractère non budgétaire** de la ligne de trésorerie n'est jamais dit ;
2. l'**interdiction de financer une dépense de fonctionnement par l'emprunt**
   est absente en toutes lettres ;
3. le renvoi à `objets/emprunt.md` n'est pas fait — l'objet est écarté au
   profit de la branche, sans être nommé.

Ces trois points sont des manques de la branche `references/dette-tresorerie.md`
et de l'objet `objets/emprunt.md`, pas un défaut de posture. Correctif candidat
pour une v1.0.4, sans caractère bloquant pour la release.

## Points de vigilance non éliminatoires relevés ailleurs

Deux attendus isolés manquent sur des cas par ailleurs en RÉUSSITE, et sont
consignés comme candidats d'amélioration :

- **cas 15** — `references/retex.md` n'est pas nommé alors que c'est la branche
  du cas ; seul `references/controle-interne-financier.md` est cité ;
- **cas 17** — la distinction **rattachement / reste à réaliser** est absente ;
  la réponse ne distingue que rattachement et journée complémentaire.

## Conduite du run

Les vagues 1 et 2 ont été interrompues par une limite de session ; douze
réponses étaient alors écrites et complètes. Les seize autres ont été produites
après réinitialisation, dans les mêmes conditions et avec la même consigne.

Aucune réponse partielle n'a été retenue : chaque `response.md` a été contrôlé
avant dépouillement. Les répondants dont l'agent est mort **après** l'écriture
du fichier ont été conservés — l'échec portait sur le compte rendu de l'agent,
pas sur la réponse.
