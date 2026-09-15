# Règles de relecture du dépôt

Ce dépôt est le skill `dirfi-fpt`. `scripts/validate_repo.py` s'exécute
automatiquement via `.github/workflows/validate.yml` : la relecture porte
donc sur ce que la validation statique ne peut pas mesurer (justesse du
contenu, provenance, respect des gabarits), pas sur ce qu'elle vérifie déjà
(inventaire de fichiers, liens, schéma des cas de test).

## À vérifier en priorité, dans cet ordre

1. **Aucune valeur chiffrée ni aucun identifiant Légifrance introduits sans
   provenance.** Toute donnée volatile (taux, seuil, plafond, montant,
   délai) et tout identifiant officiel (`LEGIARTI`, `JORFTEXT`, `CETATEXT`,
   `NOR`) ajoutés dans le diff doivent porter une date de vérification
   traçable dans `references/references-verifiees.md`, ou la réserve
   explicite « à confirmer en version consolidée ». Une valeur ou un
   identifiant qui apparaît de mémoire, sans l'une ou l'autre, est un
   problème bloquant — c'est l'invariant anti-hallucination central de ce
   skill (§5.4 du `SKILL.md`).
2. **Respect strict des gabarits.** Toute branche modifiée ou ajoutée dans
   `references/` suit les **12 sections** imposées par
   `references/_gabarit-branche.md` ; tout objet modifié ou ajouté dans
   `objets/` suit les **6 sections** imposées par
   `objets/_gabarit-objet.md`. Un écart de structure (section manquante,
   renommée ou réordonnée sans raison) est à signaler.
3. **Les deux garde-fous du `SKILL.md` restent intacts et prioritaires.**
   Le hard stop **gestion de fait** (§5.2, bloc `STOP — Ce montage fait
   manier des deniers publics...`) et le hard stop **budgétaire** (§5.3,
   bloc `ALERTE BUDGÉTAIRE...`) doivent rester verbatim, et rester le
   **premier livrable affiché**, avant tout contenu métier, dans toute
   branche ou tout objet qui les mobilise. Toute reformulation qui affaiblit
   ces blocs, les déplace après du contenu métier, ou en fait une simple
   recommandation, est bloquante.
4. **Frontière `drh-fpt` respectée (§5.5).** Aucun contenu ajouté ne doit
   introduire un montant de régime indemnitaire, un plafond réglementaire
   par groupe de fonctions, une condition individuelle d'attribution, ou un
   délai/une instance de procédure statutaire — même sourcé, même sous
   réserve. Ce qui reste permis : nommer l'étape sans la dérouler, chiffrer
   l'impact budgétaire, signaler un enjeu de calendrier. Un contenu qui
   franchit cette ligne doit être supprimé, pas seulement assorti d'un
   renvoi.
5. **Cohérence version et mise à jour conjointe.** Si le diff change la
   version en tête de `SKILL.md`, `README.md`, `CHANGELOG.md` et
   `vault/index-dirfi-fpt.md` doivent tous porter la même version. Toute
   correction de fond sur une branche doit mettre à jour ensemble la
   branche, `JOURNAL.md` (si présent) et `CHANGELOG.md`.

## À ne pas signaler

- Le style d'écriture d'une branche ou d'un objet.
- La longueur d'une branche, tant qu'elle reste dans la fourchette usuelle
  de 300 à 450 lignes.
