Un rejet systématique et répété sur trois mois n'est pas un incident isolé : c'est un signal de dysfonctionnement de process qu'il faut traiter comme tel, pas dossier par dossier. Voici comment je structurerais la réponse.

## 1. Ce que ce n'est probablement pas (à vérifier quand même)

Avant tout diagnostic, deux tests rapides, issus du routeur `references/analyse-situation.md` :

- **Un service ou une association manie-t-il des fonds hors du circuit du comptable** dans ce dossier (encaissement direct, avance non prévue, subvention qui rémunère en réalité une prestation) ? Si oui, c'est le garde-fou `SKILL.md` §5.2 qui prime sur tout le reste, avant toute autre recommandation.
- **Le budget est-il irrégulier** sur ce point (dépense obligatoire non inscrite, absence de crédit ouvert) ? Si les subventions rejetées correspondent à une dépense obligatoire non couverte par des crédits, c'est l'alerte budgétaire `SKILL.md` §5.3, à traiter via `references/controle-budgetaire.md`.

Rien dans votre description n'indique l'un ou l'autre à ce stade — mais posez-vous la question dossier par dossier avant d'aller plus loin, car un rejet répété peut être le symptôme visible d'un de ces deux problèmes de fond.

## 2. Le vrai sujet : identifier le motif exact, pas contourner le rejet

D'après `references/controle-interne-financier.md` (§5.3, cycle rejet/régularisation) : chaque rejet du comptable doit être **motivé et précis**. S'il ne l'est pas, ou si les motifs varient sans que vous les ayez formellement recensés, la première action est de **reprendre avec le comptable la liste exacte des motifs de rejet, dossier par dossier**, plutôt que de chercher un moyen de passer outre.

Pour des mandats de subvention, les causes les plus fréquentes de rejet systématique (`references/subventions.md` §5.3-§5.6, `objets/subvention-association.md` §3.4-§3.6) sont typiquement :

- **absence ou insuffisance de délibération d'attribution**, ou attribution par l'exécutif sans délégation régulière et documentée ;
- **absence de convention obligatoire** lorsque le montant cumulé versé au même bénéficiaire franchit le seuil réglementaire de conventionnement (seuil qui est une valeur volatile — non citée ici sans vérification, cf. §4 ci-dessous) ;
- **convention incomplète** : objet insuffisamment précis, montant ou modalités de versement non conformes à la délibération ;
- **pièce justificative manquante** (RIB, compte rendu financier d'un exercice antérieur non produit alors qu'il conditionne le nouveau versement, etc.) ;
- **imputation comptable erronée** (section fonctionnement/investissement, compte M57 inadapté à l'objet de la subvention — voir `references/nomenclature-m57.md`) ;
- **avance versée sans base** dans la convention ou la délibération.

Le fait que le rejet soit *systématique* depuis trois mois suggère fortement une **cause structurelle unique** (un champ de la convention-type mal renseigné, une délégation expirée, un seuil récemment franchi, un changement de pratique du comptable) plutôt que des erreurs ponctuelles différentes à chaque fois. Objectif : remonter au motif générique, pas traiter chaque rejet isolément.

## 3. Ce qu'il ne faut pas faire par réflexe : la réquisition

La réquisition du comptable (`references/controle-interne-financier.md` §5.4) permet à l'ordonnateur de passer outre un rejet qu'il estime infondé. Mais **certains motifs sont exclus de son champ** — notamment l'absence de justification, le défaut de disponibilité des crédits, ou plus largement tout ce qui touche à la sincérité de la dépense — et la liste exacte, la forme et les délais de cet acte relèvent d'un texte à vérifier avant toute mise en œuvre. Si le motif de rejet est un de ces motifs d'exclusion, la réquisition n'est pas ouverte, et la tenter serait inopérant. Un usage répété de la réquisition sur un même motif est d'ailleurs lui-même un signal à faire remonter : il traduit soit une irrégularité récurrente côté ordonnateur, soit un désaccord de fond avec le comptable à clarifier directement avec lui.

**Ne pas envisager la réquisition avant d'avoir isolé le motif exact et vérifié qu'il n'entre pas dans les cas d'exclusion.**

## 4. Point de vigilance calendrier

Trois mois de rejets signifie, pour les associations bénéficiaires, trois mois sans versement. Deux conséquences à vérifier :
- un **délai de paiement** peut courir depuis la liquidation initiale, avec un risque d'intérêts moratoires si le retard est imputable à la collectivité plutôt qu'au bénéficiaire (taux d'intérêt moratoire : valeur volatile, à vérifier, jamais de mémoire) ;
- si une association compte sur ce versement pour sa trésorerie, l'enjeu dépasse le strict financier.

## 5. Démarche recommandée

1. Lister les rejets des trois derniers mois avec, pour chacun, le motif exact notifié par le comptable.
2. Vérifier s'il s'agit d'un motif unique récurrent ou de motifs différents.
3. Si motif unique (cas le plus probable) : corriger la cause à la racine — délibération, délégation, convention-type, imputation — puis représenter les dossiers.
4. Si le désaccord porte sur l'appréciation même du motif par le comptable (vous le jugez infondé) : l'évoquer directement avec le comptable assignataire avant tout acte formel, et seulement ensuite envisager une réquisition si le motif n'est pas exclu (§3 ci-dessus).
5. Formaliser le circuit dans une fiche de procédure interne, pour éviter la récidive : c'est l'objet du générateur `references/templates/fiche-procedure-financiere.md` (piloté par `references/controle-interne-financier.md`), qui documente qui fait quoi et qui contrôle quoi à chaque étape du circuit dépense/subvention. Je peux l'ouvrir avec vous si vous voulez producer cette fiche — la logique est interactive (question par question, aucune donnée inventée).
6. Un dysfonctionnement récurrent sur trois mois est un cas typiquement journalisable dans `JOURNAL.md` : je vous propose d'y consigner l'anomalie (motif, durée, résolution) une fois la cause isolée.

## 6. Ce qui reste à vérifier avant toute conclusion chiffrée

Cette session ne me permet pas d'appeler une source officielle (Légifrance, DGFiP) : je ne peux donc citer aucun seuil, taux ou délai comme acquis. À vérifier avant usage, par vous ou via `recherche-juridique` :
- le seuil réglementaire de conventionnement des subventions ;
- le taux des intérêts moratoires applicable en cas de retard de paiement imputable à la collectivité ;
- la forme, le délai et les motifs précis d'exclusion de la réquisition du comptable.

**[Risque / confiance]** : risque **moyen à élevé** (blocage récurrent d'un paiement, préjudice possible pour le bénéficiaire, pas d'atteinte à l'équilibre du budget en l'état) ; confiance **stable** sur la méthode de diagnostic et le principe (cycle rejet/motif/régularisation, exclusion de la réquisition), **à vérifier** sur les valeurs chiffrées et la procédure exacte de réquisition.

**Références internes mobilisées** : `references/analyse-situation.md` (routeur), `references/controle-interne-financier.md` (§5.3 rejet/régularisation, §5.4 réquisition, §5.6 cartographie), `references/subventions.md` (§5.3-§5.6), `objets/subvention-association.md` (§3.4-§3.6), `references/nomenclature-m57.md` (imputation), `references/templates/fiche-procedure-financiere.md` (écrit proposé).
