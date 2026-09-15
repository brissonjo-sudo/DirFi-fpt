# Intérêts moratoires réclamés par un fournisseur

Aucun garde-fou ne se déclenche sur ce dossier (pas de maniement de fonds hors circuit du comptable, pas d'acte budgétaire irrégulier, pas de volet statutaire, pas de question de passation) : c'est un point classique d'exécution de la dépense, à la frontière avec le volet financier des marchés si le paiement s'adosse à un marché formalisé. Réponse directe, avec les valeurs vérifiées du jour.

## 1. Base légale et valeurs vérifiées ce jour (15/09/2026)

| Élément | Valeur | Texte | Statut |
|---|---|---|---|
| Délai global de paiement des pouvoirs adjudicateurs (donc de la collectivité), sauf délai contractuel différent | **30 jours** | Code de la commande publique, art. **L. 2192-10** (LEGIARTI000037703779, en vigueur depuis le 01/04/2019) et art. **R. 2192-10** (LEGIARTI000037729711, en vigueur depuis le 01/04/2019) | vérifié le 15/09/2026 sur Légifrance |
| Répartition du délai | Part comptable : **10 jours** — part ordonnateur : **20 jours** par complément arithmétique | Décret n° 2013-269 du 29 mars 2013, **art. 12** (JORFTEXT000027248487, article toujours en vigueur) | part comptable vérifiée ; part ordonnateur déduite par soustraction, **à confirmer précisément si le fournisseur conteste la répartition elle-même et non le seul dépassement global** |
| Taux des intérêts moratoires | Taux BCE (opérations principales de refinancement) en vigueur au 1er jour du semestre où le retard a **commencé à courir**, majoré de **8 points** | Décret n° 2013-269, **art. 8** | vérifié le 15/09/2026 sur Légifrance (formule) |
| Taux BCE applicable au 2nd semestre 2026 | 2,40 % → taux moratoire **10,40 %** pour un retard ayant commencé à courir entre le 01/07/2026 et le 31/12/2026 | Communiqué de politique monétaire de la BCE du 23/07/2026 (taux refi maintenu à 2,40 %) | vérifié le 15/09/2026, source primaire BCE |
| Indemnité forfaitaire pour frais de recouvrement | **40 €**, due de plein droit en plus des intérêts | Décret n° 2013-269, **art. 9** | vérifié le 15/09/2026 sur Légifrance |

**Point de vigilance : ces trois valeurs (délai, taux, indemnité) sont volatiles.** Le taux change chaque semestre et reste figé au niveau du semestre de départ du retard pendant toute sa durée — ne jamais appliquer le taux courant à un retard qui a commencé à courir un semestre antérieur. À revérifier à chaque nouveau dossier, jamais reconduites d'un cas à l'autre.

## 2. Comment vérifier que le fournisseur a raison — méthode

1. **Qualifier le support du paiement** : s'agit-il bien d'un contrat relevant de la commande publique (marché formalisé ou non, accord-cadre, simple bon de commande) ? Si oui, le délai de 30 jours de la CCP s'applique de plein droit sauf délai contractuel plus favorable au fournisseur inscrit au marché. Si le paiement ne relève d'aucun contrat de ce type, ne pas présumer 30 jours par défaut — identifier le texte spécifique applicable.
2. **Reconstituer le point de départ exact** : date de réception de la facture par la collectivité (tampon ou horodatage Chorus Pro), et non la date d'émission par le fournisseur, ni la date du service fait si celle-ci est postérieure à la réception de la facture.
3. **Identifier toute suspension régulière** du délai (demande de pièces complémentaires notifiée dans les formes, contestation motivée du service fait) et la déduire du décompte. Une suspension non notifiée dans les règles ne suspend rien — vérifier la trace écrite avant de l'opposer au fournisseur.
4. **Compter les jours calendaires** entre le point de départ (net des suspensions) et le paiement effectif (ou la date du jour si non encore payé) ; comparer au délai applicable.
5. **Si dépassement avéré** : les intérêts sont dus de plein droit dès le premier jour de retard, **sans mise en demeure préalable**. Calcul : `montant TTC dû en principal × taux applicable (figé au semestre de départ du retard) × nombre de jours de retard / 365`, plus l'indemnité forfaitaire de 40 €.
6. **Contrôler le calcul du fournisseur** sur deux pièges fréquents : (a) l'application du taux du semestre en cours au lieu du taux figé au semestre où le retard a commencé ; (b) une capitalisation des intérêts sur des intérêts déjà versés, qui n'est pas de droit commun sans texte le prévoyant expressément — à vérifier avant tout refus sur ce motif précis.
7. **Documenter l'écart** pièce par pièce si le décompte du fournisseur diverge, avant toute réponse. Une fois la créance reconnue, le paiement des intérêts moratoires ne nécessite pas de délibération et suit le circuit normal de mandatement, mais reste soumis au contrôle du comptable comme toute dépense.

## 3. Renvois

- Fond de la règle (délai global de paiement, intérêts moratoires, méthode) : `references/execution-depense.md` §5.4 et §6.2.
- Si le paiement s'adosse à un marché formalisé : `references/commande-publique-financiere.md` §5.10 et `objets/marche-public.md` §3.10 (même mécanique, mêmes réserves de vérification).

## 4. [Risque / confiance]

**Risque moyen à élevé** — créance de tiers, intérêts dus de plein droit, mais sans atteinte à l'équilibre budgétaire ni mise en jeu de la responsabilité personnelle si le calcul est correctement vérifié avant paiement. **Confiance** : taux et délais vérifiés ce jour sur sources primaires (Légifrance, communiqué de la BCE) — à revérifier au prochain dossier.

À signaler pour suivi : si ce type de réclamation revient de façon récurrente avec ce fournisseur ou ce service, c'est aussi un signal de contrôle interne sur le respect du délai global de paiement, indépendamment du traitement de ce cas — à envisager pour une entrée `JOURNAL.md`.

## Sources vérifiées le 15/09/2026

- [Article L2192-10 - Code de la commande publique](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037703779) — LEGIARTI000037703779
- [Article R2192-10 - Code de la commande publique](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037729711) — LEGIARTI000037729711
- [Décret n° 2013-269 du 29 mars 2013](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000027248487) — JORFTEXT000027248487 (art. 8, 9, 12)
- [Communiqué de politique monétaire de la BCE du 23 juillet 2026](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260723~29f24d99bc.fr.html)
