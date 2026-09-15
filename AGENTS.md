# Consignes de contribution — dépôt `dirfi-fpt`

Ce dépôt porte un **skill d'aide à la décision**, pas une documentation. Ce qui
y est écrit est lu par un modèle et devient une réponse donnée à un directeur
des finances. Les contraintes ci-dessous ne sont pas des préférences de style.

## Contraintes non négociables

1. **Français** partout : contenu, commentaires de code, messages de commit.
2. **Aucune valeur chiffrée de mémoire.** Taux, seuil, plafond, montant, barème,
   délai, durée d'amortissement : ils se vérifient à la source ou ne s'écrivent
   pas. Voir `SKILL.md` §5.4 et `references/socle-sources-verification.md` §5.
3. **Aucun identifiant Légifrance en dur** (`LEGIARTI`, `JORFTEXT`, `CETATEXT`)
   hors de `references/references-verifiees.md`, qui est le seul registre
   autorisé — et seulement pour des identifiants **réellement vérifiés**, datés.
4. **Les deux garde-fous sont intouchables.** Le hard stop gestion de fait
   (`SKILL.md` §5.2) et l'alerte budgétaire (§5.3) s'affichent **avant** tout
   contenu métier. Toute modification qui les affaiblit ou les rend
   conditionnels est un régression bloquante.
5. **La frontière `drh-fpt` est opposable** (§5.5). Aucun montant de régime
   indemnitaire, aucune procédure statutaire, aucun délai d'instance dans ce
   dépôt — même sourcé, même sous réserve.
6. **Aucune donnée nominative** : ni agent, ni élu, ni administré, ni
   bénéficiaire, nulle part, y compris dans `JOURNAL.md`.
7. **Gabarits respectés** : 12 sections pour une branche
   (`references/_gabarit-branche.md`), 6 sections pour un objet
   (`objets/_gabarit-objet.md`).
8. **Pas de duplication** : les branches pointent les unes vers les autres, les
   objets pointent vers les branches. Le même contenu n'existe qu'à un endroit.

## Avant toute livraison

```
python3 scripts/validate_repo.py
python3 scripts/package_skill.py
```

Le premier doit sortir en code 0. Le second produit l'archive de portage dans
`dist/` (non versionnée).

## Mise à jour conjointe

Une modification de fond touche **trois** fichiers, pas un :

1. la branche ou l'objet concerné ;
2. `JOURNAL.md` si un cas réel est à l'origine de la modification ;
3. `CHANGELOG.md` avec la montée de version.

La version doit rester cohérente dans `SKILL.md`, `README.md`, `CHANGELOG.md` et
`vault/index-dirfi-fpt.md` — `validate_repo.py` le vérifie.

## Décisions structurantes

Toute décision d'architecture (ajout d'une couche, déplacement d'une frontière,
changement de gabarit) fait l'objet d'une ADR dans `docs/adr/`.
