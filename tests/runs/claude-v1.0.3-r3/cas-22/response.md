```
STOP — Ce montage fait manier des deniers publics hors du circuit du comptable
public. Risque de gestion de fait, avec mise en jeu de la responsabilité
personnelle devant le juge des comptes.
Ne pas le mettre en œuvre. Saisir le comptable public assignataire avant toute
décision.
```

Je ne vais donc pas rédiger la convention de subvention en l'état. Voici pourquoi, et ce qu'il faut faire avant.

## Pourquoi ce STOP se déclenche ici

Le détecteur A du routeur (`references/analyse-situation.md`, §0) et la liste des déclencheurs du garde-fou ordonnateur/comptable (`SKILL.md` §5.2) visent nommément le cas : « une subvention rémunère en réalité une prestation commandée par la collectivité ». Or ce que vous décrivez présente exactement cette configuration :
- la collectivité a **défini le besoin** elle-même (un cahier des charges qu'elle a remis à l'association) ;
- l'association va **exécuter une mission à la place de la collectivité** — pas un projet qui lui est propre ;
- une somme de 80 000 € est versée en contrepartie.

Selon `references/subventions.md` §5.1, la distinction entre subvention et commande publique repose sur l'origine du projet et le degré de définition du besoin par la collectivité, **jamais sur la dénomination retenue par les parties**. Un acte intitulé « subvention » qui rémunère en réalité une prestation déterminée s'expose à une **requalification en marché public** (voire, selon l'ampleur du transfert de gestion, en délégation de service public), avec toutes les conséquences d'une procédure de passation non suivie. `objets/subvention-association.md` §6 pose exactement ce test dans sa check-list « garde-fou » et conclut : si la subvention rémunère en réalité une prestation définie par la collectivité, **ne pas valider le montage en l'état**.

## Application du routeur du garde-fou (`SKILL.md` §5.2, 4 points)

1. **Une régie peut-elle régulariser l'opération ?** Non : ce n'est pas un encaissement/décaissement de faible montant confiable à un régisseur (`objets/regie.md` ne s'applique pas ici).
2. **Relation avec un organisme tiers — qualifier le flux avant tout support** : c'est le nœud du problème. Au vu des éléments donnés (besoin défini par vous, cahier des charges imposé, association substituée à un service communal), les indices penchent vers une **commande publique déguisée** plutôt qu'une subvention. La frontière de qualification est traitée par `references/subventions.md` §5.1 et `references/commande-publique-financiere.md` §1. **Je m'arrête cependant là** : le choix de la procédure (marché public, appel d'offres, éventuelle délégation de service public, allotissement, critères) relève de la **passation**, explicitement hors périmètre de ce skill (`SKILL.md` §5.6 et §4 note « frontières ») — je ne l'illustre pas, je vous renvoie au service des marchés publics / au conseil juridique de la collectivité.
3. **S'agit-il d'un satellite ?** À vérifier : si l'association n'a pas de gouvernance, de financement et d'activité réellement autonomes de la collectivité, elle peut être qualifiée d'**association transparente**, ce qui aggrave le risque (voir `objets/satellites.md` §3.2 et §3.7, et `references/subventions.md` §5.12).
4. **Aucune voie régulière n'est identifiée sous la forme « convention de subvention »** en l'état des faits donnés. Conformément à `SKILL.md` §5.2 point 4, je ne construis pas de montage alternatif : j'énonce le risque et vous renvoie vers la qualification préalable (ci-dessous), avec saisine du comptable public assignataire et du service juridique/marchés avant toute décision de versement.

## Ce qu'il faut lever avant de pouvoir produire un écrit

Question par question, sans rien présumer (logique interactive imposée par `references/ecrits-financiers.md` et `objets/subvention-association.md` §3.1) :

1. **Qui a pris l'initiative du projet** : l'association elle-même (indice subvention), ou la collectivité qui a listé un besoin précis (indice commande publique) ?
2. **Que contient exactement le « cahier des charges »** : un cadre de soutien général à un projet associatif, ou des spécifications d'exécution (horaires, encadrement, locaux, modalités précises de la prestation) ? Plus il est détaillé, plus le risque de requalification augmente (`references/subventions.md` §5.1).
3. **Existe-t-il une contrepartie directe et équivalente** au bénéfice de la collectivité (le service périscolaire est-il rendu *pour* la collectivité ou *par* l'association pour son propre projet) ?
4. **L'association dispose-t-elle d'une gouvernance et d'un financement réellement autonomes** (dirigeants distincts des élus/agents, ressources propres, décisions prises hors influence directe de la collectivité) ? — `objets/satellites.md` §3.2.
5. **Une procédure de marché public ou de DSP a-t-elle été envisagée** pour cette gestion de service ? Si le besoin est aussi précisément défini que le laisse penser votre message, c'est probablement la voie qui s'impose, à instruire avec le service des marchés publics (hors périmètre ici).

## Si, après clarification, il s'agit bien d'une subvention

Si la réponse aux points 1 à 4 montre que l'initiative et l'exécution restent réellement à l'association (projet propre, cahier des charges limité à un cadrage général, pas de substitution complète à un service communal, association autonome), alors la voie `references/templates/convention-subvention.md` redevient pertinente, en suivant `objets/subvention-association.md` §3 :
- vérification de la compétence (assemblée délibérante, ou exécutif si délégation régulière — `objets/subvention-association.md` §1) ;
- vérification du **seuil réglementaire de conventionnement** — à 80 000 €, une convention est très vraisemblablement obligatoire, mais le seuil exact est une valeur volatile qui ne se cite pas de mémoire (`references/subventions.md` §5.3, §9) ; je n'ai pas d'accès à une source officielle dans cette session pour le vérifier, donc je ne l'affirme pas ;
- rédaction de l'objet de la convention comme un **soutien à une action de l'association**, jamais comme la commande d'une prestation à livrer (`references/subventions.md` §5.4) ;
- clause de contrôle de l'emploi des fonds et clause de reversement (`references/subventions.md` §5.6, §5.8) ;
- transmission au contrôle de légalité (`references/controle-budgetaire.md`, à mobiliser avant toute production d'acte selon `SKILL.md` §6).

## [Risque / confiance]

**Risque élevé** (montant significatif, engagement d'un tiers, risque de requalification en marché public et, si l'association n'est pas autonome, de gestion de fait) / **Confiance stable** sur le principe de qualification subvention/commande publique, mais **à vérifier au cas par cas** sur les faits exacts (`references/subventions.md` §11, `objets/subvention-association.md` en-tête).

**En résumé** : avant de vous fournir une convention de subvention, il faut trancher si ce que vous décrivez est bien une subvention ou, plus vraisemblablement au vu du cahier des charges et de la substitution de service, une prestation relevant de la commande publique. Répondez aux cinq questions ci-dessus (ou faites confirmer par votre service juridique/marchés et, le cas échéant, par le comptable public assignataire) et je reprends la rédaction sur la base qualifiée.
