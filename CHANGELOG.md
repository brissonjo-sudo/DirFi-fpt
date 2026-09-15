# Changelog — `dirfi-fpt`

Versionnage sémantique **MAJEUR.MINEUR.PATCH**.

- **MAJEUR** — changement d'architecture ou de périmètre, rupture de compatibilité.
- **MINEUR** — nouvelle branche, nouvel objet, nouveau générateur, nouvelle frontière.
- **PATCH** — correctif de fond, précision, mise à jour de source.

---

## [1.0.0] — 2026-09-15 — socle initial

Première version du skill. Construit sur le pattern d'architecture de `dpm-fpt`,
lui-même dérivé de `drh-fpt` (voir `docs/adr/0001-adoption-pattern-dpm-fpt.md`).

### Ajouté

- **Noyau** `SKILL.md` en 9 sections : déclenchement, posture hybride avec
  matrice de vérification, routeur, tableau des branches, dispositifs
  transverses, écrits, auto-vérification en 14 points, limites, maintenance.
- **Couche 1** — routeur `references/analyse-situation.md`, portant en section 0
  les deux détecteurs prioritaires sur toute réponse métier.
- **Couche 2** — 12 branches métier : cycle budgétaire, nomenclature M57,
  exécution de la dépense, exécution de la recette, fiscalité locale, dotations
  et péréquation, dette et trésorerie, prospective et analyse, subventions,
  volet financier de la commande publique, contrôle interne financier, écrits
  financiers.
- **Couche 2 bis** — 3 briques posture : contrôle budgétaire, contentieux
  financier, retour d'expérience.
- **Couche 3** — 8 objets métier : subvention à une association, régie, emprunt,
  opération d'investissement, clôture d'exercice, satellites, immobilisation,
  marché public (volet financier).
- **Couche 4** — 5 générateurs d'écrits interactifs.
- **Double garde-fou** (`docs/adr/0002-double-garde-fou-financier.md`) :
  - `STOP` **ordonnateur / comptable** sur tout maniement de deniers publics
    hors du circuit du comptable, avec routeur en 4 points vers la voie
    régulière (régie, qualification du flux, satellites, abstention motivée) ;
  - `ALERTE BUDGÉTAIRE` sur tout acte budgétaire irrégulier, avec renvoi vers la
    procédure de contrôle budgétaire.
- **Frontière `drh-fpt`** opposable, avec bloc `BASCULE` prioritaire et règle de
  non-autorisation : la disponibilité du skill délégataire ne vaut pas
  autorisation de produire.
- **Socle de vérification** : carte des sources des finances locales, sept
  réflexes propres au métier, résolution des conflits de normes, règle de
  provenance des identifiants.
- **Régime des valeurs chiffrées à deux vitesses**
  (`docs/adr/0003-regime-des-valeurs-chiffrees.md`) : les valeurs volatiles ne
  se citent jamais de mémoire ; les références structurelles stables se citent
  sous réserve. Deux registres séparés — `references-verifiees.md` pour les
  identifiants de textes, `cache-taux-seuils.md` pour les valeurs.
- **Outillage** : `validate_repo.py` (frontmatter, invariants de garde-fou
  verbatim, cohérence des versions, complétude des couches, résolution des liens
  internes, interdiction des identifiants Légifrance en dur hors registre,
  contrôles anti-PII), `package_skill.py` (archive déterministe, cache de
  maintenance exclu), `eval_suite.py` (préparation et dépouillement des
  campagnes).
- **Intégration continue** : `validate.yml` exécute la validation à chaque push
  et pull request — les dépôts frères ne branchaient pas leurs scripts sur la
  CI ; `auto-review.yml` déclenche la relecture automatique des pull requests.
- **Distribution** : `.claude-plugin/` (plugin et marketplace mono-plugin) pour
  l'installation en une commande, en complément de l'archive de portage.
- **Vault Obsidian** : index de navigation et carte de maillage, non packagés,
  sans contenu métier dupliqué.

### À faire avant de scorer cette version

La v1.0.0 **n'est couverte par aucune campagne d'évaluation**. La campagne `r1`
reste à conduire avec `scripts/eval_suite.py` sur `tests/cas-de-test.json`.
Aucun score n'est annoncé tant que la mesure n'a pas eu lieu.

Le registre `references/references-verifiees.md` et le cache
`references/cache-taux-seuils.md` naissent **volontairement peu remplis** :
seule une vérification réelle à la source peut les alimenter. Une entrée
plausible mais non vérifiée y serait plus nuisible qu'une case vide.
