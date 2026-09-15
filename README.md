# dirfi-fpt — Système expert d'aide à la décision pour une Direction des Finances

Skill Claude/Codex destiné à un **Directeur des Finances** en collectivité
territoriale française. Il cadre le besoin, oriente vers la bonne base légale et
le bon écrit, et sécurise les frontières de compétence (ordonnateur / comptable
public, assemblée / exécutif, finances / RH).

## Périmètre

Finances publiques locales : cycle budgétaire, nomenclature M57, exécution de la
dépense et de la recette, régies, fiscalité locale, dotations et péréquation,
dette et trésorerie, prospective et analyse financière, subventions, volet
financier de la commande publique, contrôle interne financier, écrits
budgétaires.

**Hors périmètre** : RH statutaire des agents (→ `drh-fpt`), **passation** des
marchés publics, conformité RGPD d'un traitement (→ `dpo-ct`), droit étranger.

## Posture

**Hybride** : opérationnelle par défaut (rapide, orientée décision, écrit et
calendrier), **vérifiée sur déclencheur** (matrice métier/juridique du
`SKILL.md` §2.2). Toute règle reposant sur un texte et **toute valeur chiffrée**
sont vérifiées à la source officielle ou marquées « à confirmer en version
consolidée ».

## Les deux garde-fous

Ce skill en porte deux, prioritaires sur toute réponse métier :

1. **Ordonnateur / comptable** — un montage qui fait manier des deniers publics
   hors du circuit du comptable public déclenche un `STOP` (risque de gestion de
   fait) avant tout autre contenu, puis un routeur vers la seule voie régulière.
2. **Budgétaire** — un acte budgétaire irrégulier (budget non voté, déséquilibre
   réel, déficit, dépense obligatoire omise) déclenche une `ALERTE BUDGÉTAIRE`
   et le renvoi vers la procédure de contrôle budgétaire.

S'y ajoute la frontière `BASCULE drh-fpt` dès que la question touche le droit
individuel ou indemnitaire d'un agent. Détail : `SKILL.md` §5.2, §5.3, §5.5 et
`docs/adr/0002-double-garde-fou-financier.md`.

## Architecture (4 couches)

1. **Decision Engine** — `references/analyse-situation.md` (routeur, appelé en
   premier, porte les deux détecteurs).
2. **Branches métier** — 12 branches + 3 briques posture dans `references/`.
3. **Objets métier** — 8 fiches système expert dans `objets/`.
4. **Générateurs** — modèles interactifs dans `references/templates/`.

## Le régime des valeurs chiffrées

Particularité de ce skill : les finances locales sont saturées de nombres qui
changent, pour la plupart, **au 1er janvier**. Le skill applique donc un régime
à deux vitesses (`SKILL.md` §5.4, `docs/adr/0003-regime-des-valeurs-chiffrees.md`) :

- **valeurs volatiles** (taux, seuils, plafonds, montants, index) — jamais
  citées de mémoire, jamais sans date d'effet. Vérifiées ou absentes ;
- **références structurelles stables** (code, décret fondateur, nomenclature) —
  citables avec la réserve « à confirmer en version consolidée ».

Ce qui reste toujours transmissible : la formule, la méthode, la procédure. Les
branches sont donc rédigées **sans chiffres** — elles ne périment pas au
changement d'exercice.

## Structure

```
dirfi-fpt/
├── SKILL.md                 # noyau : posture, garde-fous, frontières
├── AGENTS.md                # contraintes de contribution non négociables
├── agents/openai.yaml       # métadonnées d'interface Codex
├── .claude-plugin/          # plugin + marketplace (installation en 1 commande)
├── references/              # couches 1 et 2 (routeur + branches + postures + socle)
│   └── templates/           # couche 4 (générateurs d'écrits)
├── objets/                  # couche 3 (fiches système expert)
├── scripts/                 # validation, packaging et évaluation reproductibles
├── tests/                   # cas de test + cas de co-activation
├── docs/adr/                # décisions d'architecture (ADR)
├── vault/                   # index Obsidian et maillage (non packagé)
├── CHANGELOG.md
├── JOURNAL.md
└── README.md
```

## Dépendances

- **`recherche-juridique`** (recommandé) — validateur de fond : vigueur des
  textes, format de citation traçable, triangulation des sources.
- **`drh-fpt`** (recommandé) — volet RH statutaire et indemnitaire.
- **`dpm-fpt`**, **`dpo-ct`** (optionnels) — métiers voisins pour les
  frontières.

## Installation

**Comme plugin Claude Code** :

```
claude plugin marketplace add brissonjo-sudo/DirFi-fpt
```

**Comme archive de portage** (Codex, autre LLM) :

```
python3 scripts/package_skill.py
# produit dist/dirfi-fpt-1.0.0.zip
```

## Validation

```
python3 scripts/validate_repo.py
```

Contrôle le frontmatter, la présence verbatim des garde-fous, la cohérence des
versions, la complétude des couches, la résolution de tous les liens internes,
l'absence d'identifiant Légifrance en dur hors du registre vérifié, et l'absence
de données personnelles. Exécuté en intégration continue à chaque push et
pull request (`.github/workflows/validate.yml`).

## Apprentissage et versioning

Boucle `JOURNAL.md` (cas anonymisés) → `CHANGELOG.md` (versions), décisions
tracées dans `docs/adr/`. Deux revues annuelles : **revue de loi de finances**
en janvier, **revue de rentrée** au 1er septembre.

## Version

**v1.0.0 — socle initial.** 12 branches métier, 3 briques posture, 8 objets,
5 générateurs, double garde-fou et régime des valeurs chiffrées à deux vitesses.

Cette version **n'a pas encore été mesurée** par une campagne d'évaluation : le
jeu de cas est en place (`tests/cas-de-test.json`) et la campagne `r1` reste à
conduire avec `scripts/eval_suite.py`. Les scores ne seront reportés ici qu'une
fois la campagne achevée — aucun chiffre de performance n'est annoncé avant
mesure.

## Licence

CC BY-SA 4.0 — voir `LICENSE`.
