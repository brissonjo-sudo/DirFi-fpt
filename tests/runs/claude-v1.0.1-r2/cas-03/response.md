## Qualification rapide

Pas de garde-fou déclenché : aucun maniement de fonds hors circuit du comptable, aucun acte budgétaire irrégulier en cause. On reste dans la branche **exécution de la dépense**, sur le sujet **délai global de paiement / intérêts moratoires**. C'est une question à valeur chiffrée et à base légale précise (matrice de vérification : « Oui ») — je l'ai donc vérifiée avant de vous répondre, pas de mémoire.

**[Risque : Élevé / Confiance : vérifiée sur le principe et le plafond, à confirmer sur le taux exact]** — le fournisseur peut agir en recouvrement, et le versement d'intérêts non dus (ou d'un montant erroné) est une dépense à justifier devant le comptable comme devant le juge des comptes.

---

## 1. Base juridique (vérifiée ce jour, 15/09/2026, via Légifrance)

| Point | Référence | Identifiant | Statut |
|---|---|---|---|
| Délai global de paiement fixé à 30 jours pour les pouvoirs adjudicateurs (dont les collectivités) | Code de la commande publique, art. **L2192-10** | LEGIARTI000037703779 (en vigueur depuis le 01/04/2019) | vérifié — Légifrance, ce jour |
| Confirmation du délai de 30 jours | Code de la commande publique, art. **R2192-10** | LEGIARTI000037729711 (en vigueur depuis le 01/04/2019) | vérifié — Légifrance, ce jour |
| Le retard de paiement est constitué de plein droit au seul dépassement du délai, sans mise en demeure | Code de la commande publique, art. **L2192-12** | LEGIARTI000037703785 (en vigueur depuis le 01/04/2019) | vérifié — Légifrance, ce jour |
| Le dépassement déclenche automatiquement : intérêts moratoires + indemnité forfaitaire pour frais de recouvrement + indemnisation complémentaire possible si les frais réels dépassent l'indemnité forfaitaire | Code de la commande publique, art. **L2192-13** | LEGIARTI000037703787 (en vigueur depuis le 01/04/2019) | vérifié — Légifrance, ce jour |
| Toute clause qui écarterait le versement d'intérêts moratoires est réputée non écrite | Code de la commande publique, art. **L2192-14** | LEGIARTI000037703789 (en vigueur depuis le 01/04/2019) | vérifié — Légifrance, ce jour |
| Taux des intérêts moratoires = taux BCE (opérations principales de refinancement) en vigueur au 1er jour du semestre au cours duquel les intérêts ont commencé à courir, **majoré de 8 points** | Code de la commande publique, art. **R2192-31** | LEGIARTI000037729653 (en vigueur depuis le 01/04/2019) | vérifié — Légifrance, ce jour |
| Indemnité forfaitaire pour frais de recouvrement fixée à 40 € | Code de la commande publique, art. **D2192-35** | LEGIARTI000037729645 (en vigueur depuis le 01/04/2019) | vérifié — Légifrance, ce jour |

**Point non tranché ici, à vérifier avant tout calcul** : la répartition interne du délai de 30 jours entre le délai de l'ordonnateur (mandatement) et celui du comptable (paiement) — des sources spécialisées citent 20 jours / 10 jours, historiquement rattachés au décret n° 2002-232 du 21 février 2002, mais l'article 19 du décret n° 2012-1246 du 7 novembre 2012 (GBCP) que j'ai consulté directement ne fixe pas cette répartition (il porte sur les contrôles du comptable, pas sur des délais). Cette répartition n'a **pas** valeur de fait acquis dans cette réponse : `⚠️ non vérifié` sur le texte exact actuellement applicable — à confirmer avant de s'en servir pour discuter avec le fournisseur de la part de responsabilité de chaque maillon.

**Taux numérique** : d'après plusieurs sources spécialisées de la commande publique convergentes (cf. sources en fin de document), le taux BCE de référence pour le second semestre 2026 serait de 2,40 %, soit un taux d'intérêts moratoires de **10,40 %** (2,40 + 8) pour les retards dont les intérêts courent entre le 1er juillet et le 31 décembre 2026. Ces sources ne sont pas le communiqué officiel de la BCE ni Légifrance : marquez ce chiffre `⚠️ à confirmer` auprès de la Banque de France ou de la fiche DAJ du ministère de l'économie avant de l'opposer au fournisseur ou de l'inscrire dans un mandat, en particulier si les intérêts ont commencé à courir avant le 1er juillet 2026 (auquel cas c'est le taux du 1er semestre qui s'applique, et non celui-ci).

---

## 2. Comment vérifier que le fournisseur a raison — méthode, pas à pas

1. **Identifier le point de départ du délai** : date de réception de la demande de paiement (facture, via Chorus Pro le cas échéant) — ou date du service fait si elle est postérieure. Ne pas confondre avec la date d'émission de la facture par le fournisseur.
2. **Écarter les causes de suspension régulières** : demande de pièces complémentaires effectivement adressée au fournisseur, litige documenté sur le service fait. Une suspension invoquée a posteriori sans trace écrite contemporaine ne tient pas.
3. **Compter les jours calendaires** écoulés entre le point de départ et la date du paiement effectif (ou d'aujourd'hui si le paiement n'a pas encore eu lieu), déduction faite des périodes de suspension régulières.
4. **Comparer au délai de 30 jours** (vérifié ci-dessus). Si le total dépasse 30 jours : le retard est constitué de plein droit, sans qu'il soit besoin que le fournisseur ait mis en demeure la collectivité au préalable (L2192-12).
5. **Déterminer la date à laquelle les intérêts ont commencé à courir** (le 31ᵉ jour) : c'est cette date qui fixe le semestre de référence pour le taux (R2192-31), pas la date du calcul ni celle du paiement.
6. **Calculer le montant dû** : intérêts moratoires (taux du semestre concerné × montant TTC dû × nombre de jours de retard / 365) **+** indemnité forfaitaire de 40 € **+** indemnisation complémentaire si le fournisseur justifie des frais de recouvrement réels supérieurs à 40 € (L2192-13) — n'accordez ce complément que sur justificatifs produits, ce n'est pas automatique contrairement au forfait de 40 €.
7. **Vérifier qu'aucune clause du marché** ne prétend exclure ou plafonner ces intérêts : une telle clause serait réputée non écrite (L2192-14), donc inopposable au fournisseur.

Si vous me donnez la date de réception de la facture, la date du service fait et la date du paiement effectif (ou son absence), je fais le calcul avec vous.

---

## 3. Volet interne

- **Imputation** : les intérêts moratoires et l'indemnité forfaitaire s'imputent en section de fonctionnement (charges financières), sur un compte distinct du principal de la dépense — l'imputation exacte relève de la nomenclature M57 (`references/nomenclature-m57.md`) : ne pas la présumer ici sans vérification du plan de comptes en vigueur.
- **Contrôle interne** : si ce type de réclamation revient régulièrement de la part de fournisseurs, c'est un signal à faire remonter en contrôle interne financier (délai global de paiement dépassé de façon récurrente), indépendamment du traitement de ce dossier.
- **Registre interne** : votre fichier `references/cache-taux-seuils.md` a ces trois valeurs marquées « à renseigner » (délai global de paiement, taux des intérêts moratoires, taux de l'intérêt légal). Les références légales ci-dessus peuvent y être consignées avec leur date de vérification ; le taux numérique du semestre, lui, reste à confirmer sur source primaire avant consignation.

---

## Sources consultées ce jour (15/09/2026)

- [Article L2192-10 — Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037703779) — délai de 30 jours
- [Section « Délais de paiement » L2192-10 à L2192-15 — Légifrance](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000037701019/LEGISCTA000037703775/)
- [Section réglementaire R2192-10 à R2192-36 — Légifrance](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000037701019/LEGISCTA000037724987/)
- [Article 19 — Décret n° 2012-1246 du 7 novembre 2012 — Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000026602813/2022-04-12) (consulté pour vérifier la répartition ordonnateur/comptable — ne la confirme pas)
- Sur le taux numérique du second semestre 2026 (non primaire, à confirmer) : [Le Moniteur](https://www.lemoniteur.fr/article/marches-publics-et-prives-les-interets-moratoires-en-baisse.2332049), [Stratt](https://stratt.fr/blog/interets-moratoires-marche-public), [fiche taux APGL64](https://apgl64.fr/index.php?eID=dumpFile&f=13036&t=f&token=4a088386aa9f38538c126c5af74630bde25bf46a)
