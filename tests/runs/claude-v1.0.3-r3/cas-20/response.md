## Qualification de l'opération

La vente d'un bâtiment communal est une **cession d'immobilisation**. Deux flux distincts s'y superposent et ne doivent pas être confondus (`references/nomenclature-m57.md` §5.9) :

- une **opération réelle** : l'encaissement du prix de vente (flux de trésorerie effectif) ;
- une **opération d'ordre** : la sortie du bien de l'actif pour sa **valeur nette comptable** (VNC), sans flux de trésorerie, avec constatation de la **plus ou moins-value** de cession (différence entre le prix de vente et la VNC).

C'est exactement la situation type couverte par `objets/immobilisation.md` §3.5 (« Sortie — Cession ») : *« constater la recette de cession, sortir le bien de l'actif pour sa valeur nette comptable, et passer l'écriture de sortie correspondante (plus ou moins-value) »*.

### Point de vigilance préalable — domanialité

Avant toute écriture, il faut qualifier le régime du bien : **domaine public** ou **domaine privé** de la commune (`references/execution-recette.md` §5.8, qui traite les « produits du domaine » et rappelle que *« le régime distinct selon que le bien relève du domaine public ou du domaine privé »* est **à qualifier avant toute recommandation**). Un bâtiment communal affecté à un service public ou à l'usage direct du public relève en principe du domaine public, **inaliénable** en l'état : sa cession suppose au préalable sa **désaffectation** puis son **déclassement** par délibération, avant toute délibération autorisant la vente elle-même. Le régime exact et le texte applicable relèvent du code général de la propriété des personnes publiques, hors du périmètre `dirfi-fpt` sur le fond domanial : à faire confirmer par le service compétent (juridique/patrimoine) avant d'engager la procédure. Si le bâtiment relève déjà du domaine privé, cette étape ne se pose pas.

## Compétence

La décision de céder un bien du patrimoine communal est un acte de disposition qui relève, en principe, de l'**assemblée délibérante** (le conseil municipal autorise la vente, fixe ou valide les conditions — prix, acquéreur), l'exécutif signant l'acte de vente sur cette autorisation. C'est une question de **compétence d'une autorité**, qui figure en ligne « Oui » de la matrice de vérification (`SKILL.md` §2.2) : à confirmer précisément (existence d'une délégation éventuelle à l'exécutif, seuil au-delà duquel un avis de l'autorité domaniale de l'État est requis avant la délibération) — je ne dispose d'aucun outil de vérification dans cette session, donc je ne cite aucun seuil ni aucune référence d'article : à vérifier sur Légifrance / auprès du service juridique avant toute délibération (`references/socle-sources-verification.md` §8, « sans outil, rien »).

## Écritures et impact budgétaire

Sur la base de `references/nomenclature-m57.md` §5.5 (sortie de l'inventaire) et §5.9 (opérations réelles / opérations d'ordre), le schéma est le suivant, **sans qu'aucun numéro de compte ou de chapitre ne soit cité ici de mémoire** (`nomenclature-m57.md` §9 : « liste et numéros exacts des classes et comptes du plan de comptes M57 — à vérifier — jamais reconstitués de mémoire pour une imputation réelle ») :

1. **Constatation et encaissement du prix de vente** : émission d'un titre de recettes par l'ordonnateur (`references/execution-recette.md` §5.1) — recette réelle, avec flux de trésorerie effectif transitant par le comptable public.
2. **Sortie du bien de l'actif** pour sa valeur nette comptable : opération d'ordre, sans flux de trésorerie, qui mouvemente à la fois le compte d'immobilisation concerné et le cumul des amortissements déjà constatés sur le bien.
3. **Constatation de la plus ou moins-value de cession** (écart entre le prix de vente et la VNC) : opération d'ordre budgétaire entre sections, dont l'imputation exacte (comptes concernés, sens de l'écriture selon que la cession dégage une plus-value ou une moins-value) est une donnée technique de l'instruction M57 à vérifier au moment de l'écriture, pas à présumer par analogie.

**Impact budgétaire résumé** : le produit de la vente constitue une **recette**, la sortie du bien et la plus/moins-value se traduisent par des **opérations d'ordre** qui n'améliorent ni ne dégradent la trésorerie mais affectent le résultat et l'équilibre entre sections. La qualification précise de la section concernée par chacune de ces trois écritures (fonctionnement / investissement) dépend de l'imputation exacte fixée par l'instruction M57 en vigueur — à vérifier avant toute écriture réelle, conformément à `nomenclature-m57.md` §5.9 et à la matrice §2.2 du `SKILL.md` (ligne « imputation comptable / règle M57 »).

**Concordance inventaire / état de l'actif** : la sortie doit être répercutée simultanément dans l'inventaire physique et comptable tenu par l'ordonnateur et signalée au comptable pour ajustement de l'**état de l'actif** (`objets/immobilisation.md` §3.5 et §1 ; `nomenclature-m57.md` §5.10) — une divergence non régularisée avant la clôture fragilise la fiabilité du bilan et du compte financier unique.

## Écrits associés

- **Délibération de déclassement** (si domaine public) puis **délibération autorisant la cession**, fixant le prix et l'acquéreur.
- **Décision de sortie** de l'ordonnateur, à archiver avec la fiche d'inventaire (`objets/immobilisation.md` §4).
- Si un chiffrage détaillé de l'impact sur le résultat et sur l'équilibre du budget est utile pour éclairer la décision, une **note d'impact financier** peut être produite via `references/templates/note-impact-financier.md` (montant de cession, VNC, plus/moins-value, exercice de rattachement — aucune de ces données n'étant à inventer si elles ne sont pas encore connues : brouillon `[INCOMPLET]` dans ce cas).

## [Risque / Confiance]

**Risque élevé** : acte de disposition du patrimoine communal, engageant un tiers acquéreur, potentiellement soumis au contrôle de légalité, avec effet sur l'équilibre entre sections. **Confiance** : stable sur l'architecture générale de l'écriture (opération réelle + opération d'ordre, VNC, plus/moins-value) ; **à vérifier** sur trois points précis avant toute exécution — qualification domaniale du bien (public/privé), compétence exacte et seuil d'avis domanial éventuel, imputation comptable précise (comptes et chapitres de l'instruction M57 en vigueur).

## Points à vérifier avant d'engager la procédure

- Régime domanial du bâtiment (public/privé) et, le cas échéant, désaffectation + déclassement préalables.
- Compétence exacte pour autoriser la cession et seuil éventuel déclenchant un avis de l'autorité domaniale de l'État.
- Imputation comptable précise des trois écritures (comptes et sections) dans l'instruction M57 en vigueur pour la collectivité.
- Rattachement de l'opération à l'exercice concerné (date de l'acte authentique de vente).

Aucune de ces quatre valeurs n'a été vérifiée dans cette session faute d'accès à une source officielle : elles ne doivent pas être tenues pour acquises avant confirmation.
