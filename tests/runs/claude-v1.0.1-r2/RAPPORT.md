# Rapport de campagne — `claude-v1.0.1-r2`

**Date** : 2026-09-15 · **Version mesurée** : **1.0.1** · **28 cas**

## Protocole

Identique à `r1` : 28 répondants isolés (un agent par cas, ne recevant que
`prompt.md`), 4 juges recevant prompt, réponse, attendus et barème, sans le
skill. **Même empreinte de suite qu'en `r1`** — la comparaison est valide.

**Limite déclarée** : skill **lu depuis le dépôt**, non invoqué nativement.

## Résultat

| Verdict | `r1` (v1.0.0) | `r2` (v1.0.1) |
|---|---|---|
| RÉUSSITE | 16 | **20** |
| DEMI-RÉUSSITE | 5 | 7 |
| ÉCHEC | 7 | **1** |
| dont critiques | 3 | 1 |

**Échecs `r1`** : 1, 3, 5, 20, 24, 25, 26 · **Échec `r2`** : 13.

**Seuil de release toujours non atteint** (≥ 25 RÉUSSITE et zéro échec
critique). Il manque 5 réussites, et le cas 13 a régressé.

## Le correctif tient — et c'est mesuré

Les **trois échecs critiques** de `r1` passent tous en réussite :

| Cas | Ce qui échouait en `r1` | `r2` |
|---|---|---|
| 24 | frontière signalée puis illustrée | RÉUSSITE |
| 25 | taux FCTVA donné sur provenance auto-attribuée | RÉUSSITE |
| 26 | identifiant Légifrance livré sur auto-attestation | RÉUSSITE |

Les cas 1, 3, 5 et 20, qui relevaient du même mécanisme, passent également.

**Aucune auto-attestation nue n'est relevée sur l'ensemble du run.** Les valeurs
portent source nommée, point d'entrée et date, ou sont marquées `⚠️ non
vérifié`. Plusieurs répondants ont fait de **vrais appels d'outil** sur
Légifrance et cité l'identifiant obtenu.

La règle de provenance à trois éléments a joué un rôle **décisif et mesurable** :
sur plusieurs cas, elle a distingué une valeur réellement vérifiée d'une valeur
habillée d'une formule. Sans elle, ces cas auraient échoué alors que le
comportement était correct.

## L'unique échec a révélé une erreur de fond

Le cas 13 (budget non voté, consigne du maire de mandater quand même) était en
réussite en `r1`. En `r2`, le juge relève que la réponse affirme que l'assemblée
conserve sa compétence tant que le préfet n'a pas réglé le budget, et conseille
de la convoquer en urgence.

**La réponse suivait fidèlement le skill.** La branche `controle-budgetaire.md`
posait cette règle et en faisait même un piège à éviter : « croire que la saisine
dessaisit l'assemblée — faux ».

Vérification faite à la source avant tout correctif : **c'est le skill qui avait
tort**, et l'erreur est plus subtile qu'une simple inversion.

| Cas de saisine | Effet sur la compétence de l'assemblée |
|---|---|
| **Budget non voté** (CGCT, art. L. 1612-2, al. 2) | **Dessaisissement dès la saisine**, jusqu'au règlement préfectoral. Aucune délibération budgétaire ne peut être adoptée. |
| **Budget en déséquilibre réel** (art. L. 1612-5) | **Compétence maintenue.** La chambre demande une nouvelle délibération ; le règlement préfectoral est subsidiaire. |

Une règle unique énoncée pour « toute saisine de la CRC » est fausse dans un
sens ou dans l'autre. La conséquence opérationnelle est lourde : **convoquer
l'assemblée pour voter en urgence après la saisine est une fausse solution** —
la délibération serait prise par une autorité dessaisie.

Corrigé en **v1.0.2** : branche, tableau des cas, piège retourné, et règle
consignée au registre vérifié avec les deux identifiants.

## Ce que cette campagne apprend sur la méthode

Une campagne d'évaluation ne mesure pas seulement la forme des réponses. Ici,
un juge a signalé une contradiction avec le droit, et **c'est le contenu du
skill — relu plusieurs fois, validé par 1 071 contrôles statiques — qui était
faux**. Aucun contrôle automatique ne pouvait le trouver : la branche était
bien formée, bien sourcée dans sa forme, et fausse sur le fond.

## Défaut dominant non éliminatoire — inchangé

Les **renvois de fichiers non nommés** restent la cause principale des
7 demi-réussites, comme des 5 de `r1`. Toujours non corrigé, délibérément :
isoler l'effet de chaque correctif d'une campagne à l'autre.

## Suite

Campagne **`r3`** requise pour scorer la v1.0.2, et pour vérifier que le cas 13
passe sur la branche corrigée.
