## Sur quelle base juridique ?

Les intérêts moratoires sont dus **de plein droit** dès que le délai global de paiement est dépassé, **sans mise en demeure préalable** et sans que le fournisseur ait à démontrer un préjudice. C'est le principe stable ; ce qui ne l'est pas, c'est la durée exacte du délai et le taux applicable — je détaille plus bas pourquoi je ne vous donne aucun chiffre tout de suite.

Une précision utile avant de vérifier : le régime exact dépend de la nature de la dépense.

- **Si la facture se rattache à un marché public formalisé** (bon de commande sur accord-cadre compris) : c'est le régime propre à la commande publique qui s'applique — `references/commande-publique-financiere.md` §5.10 (délai global de paiement et intérêts moratoires propres aux marchés) et §6 (méthode de calcul), avec le pointeur opérationnel `objets/marche-public.md` §3.10.
- **Si c'est une dépense hors marché formalisé** (facture simple sur bon de commande courant) : c'est le régime général de la dépense publique — `references/execution-depense.md` §5.4 (délai global de paiement et intérêts moratoires) et §6.2 (méthode de calcul).

Les deux régimes suivent la même logique, mais les durées et les modalités de computation ne sont pas garanties identiques. Premier réflexe : identifiez de quel cas relève votre facture avant de trancher.

## Comment vérifier que le fournisseur a raison — la méthode, étape par étape

1. **Point de départ du délai.** C'est la date de réception de la demande de paiement (facture), ou la date du service fait si elle lui est postérieure. Vérifiez laquelle des deux s'applique à votre dossier — ne présumez pas que c'est la date de facture si le service fait est plus tardif.
2. **Décompte des jours.** Comptez du point de départ jusqu'à la date de paiement effectif (ou jusqu'à aujourd'hui si la facture n'est toujours pas payée).
3. **Déduction des suspensions régulières.** Si vous avez notifié une demande de pièces complémentaires régulière, ou signalé un litige sur le service fait, dans les formes et délais requis, la ou les périodes correspondantes se déduisent du décompte. Vérifiez que ces suspensions ont bien été notifiées dans les règles — une simple relance interne ou un blocage administratif non formalisé ne suspend rien.
4. **Répartition ordonnateur / comptable.** Le délai global se répartit entre le délai qui vous est imputable (jusqu'au mandatement) et celui du comptable (jusqu'au paiement) — utile si vous voulez situer où s'est produit le dépassement, mais cela ne change rien au montant dû au fournisseur.
5. **Comparaison à la durée maximale applicable.** C'est ici qu'il faut vérifier la valeur en vigueur (§ ci-dessous) plutôt que la tenir pour acquise.
6. **Si dépassement confirmé : calcul des intérêts.** La formule est : `montant dû (TTC) × taux applicable × durée du dépassement`, à laquelle s'ajoute, le cas échéant, une indemnité forfaitaire pour frais de recouvrement dont le montant est fixé par le texte (`references/commande-publique-financiere.md` §5.10 et §6).
7. **Contre-vérification du calcul du fournisseur, poste par poste.** Demandez-lui le détail de son calcul (date de départ retenue, nombre de jours, taux appliqué, indemnité forfaitaire incluse ou non) et comparez chaque poste à ce que vos propres dates (réception facture, service fait, mandatement, paiement) donnent. La contestation la plus fréquente porte sur le point de départ retenu ou sur l'oubli d'une suspension régulière — pas sur le principe du droit à intérêts.

## Ce que je ne peux pas vous donner maintenant, et pourquoi

La durée du délai global de paiement et le taux des intérêts moratoires (ainsi que le montant de l'indemnité forfaitaire de recouvrement) sont des **valeurs volatiles** : elles se vérifient à la source ou ne se citent pas (`references/socle-sources-verification.md` §5). Cette session ne me permet aucun appel à une source officielle pour les confirmer aujourd'hui. Je ne vous donne donc aucun chiffre — ni pour le délai, ni pour le taux — car une valeur non vérifiée énoncée comme un fait serait plus dangereuse qu'une absence de réponse.

À vérifier avant de conclure, et à consigner avec leur date d'effet :
- la **durée du délai global de paiement** applicable à votre cas (marché ou hors marché) ;
- le **taux des intérêts moratoires** en vigueur **à la date où le dépassement s'est produit** (pas nécessairement le taux d'aujourd'hui — ces taux évoluent périodiquement) ;
- le **montant de l'indemnité forfaitaire pour frais de recouvrement**, le cas échéant.

Sources à consulter : Légifrance pour le texte applicable (code de la commande publique si marché, régime général de la dépense publique sinon — à confirmer en version consolidée dans les deux cas), et le portail de la direction des affaires juridiques du ministère de l'économie pour les seuils et taux propres à la commande publique. Votre comptable public assignataire est aussi une ressource directe : c'est lui qui calcule et verse concrètement les intérêts moratoires en cas de dépassement confirmé, et il dispose généralement du taux à jour appliqué sur la période concernée.

## [Risque / Confiance]

**Risque : élevé** (créance d'un tiers, dépassement générant un droit automatique, montant potentiellement significatif si le retard est ancien) — **Confiance : stable sur le principe** (les intérêts sont dus de plein droit en cas de dépassement, sans mise en demeure), **à vérifier sur la durée du délai et le taux** avant tout chiffrage ou tout accord donné au fournisseur.

## En résumé, la marche à suivre

1. Qualifiez le dossier (marché formalisé ou non) pour situer le bon régime.
2. Reconstituez vos propres dates (réception facture, service fait, mandatement, paiement) et les éventuelles suspensions régulièrement notifiées.
3. Vérifiez à la source la durée du délai et le taux applicables à la période du dépassement.
4. Recalculez le montant selon la formule ci-dessus et comparez au calcul du fournisseur poste par poste.
5. Si un écart apparaît sur le principe (délai non dépassé une fois les suspensions déduites) ou sur le montant, répondez au fournisseur avec le détail chiffré du désaccord plutôt qu'un refus global — le droit à intérêts, lui, n'est pas discutable en cas de dépassement avéré.
