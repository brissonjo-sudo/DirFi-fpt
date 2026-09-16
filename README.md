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
# produit dist/dirfi-fpt-1.0.3.zip
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

**v1.0.3 — nommer le fichier, pas seulement la notion.**

Toute branche, tout objet, tout générateur réellement mobilisé est **nommé par
son chemin**, à l'endroit où sa règle est utilisée (`SKILL.md` §4, et point 16
de l'auto-vérification §7). Sans le chemin, l'utilisateur ne peut ni vérifier la
règle, ni la corriger, ni distinguer ce qui vient du skill de ce qui vient de la
mémoire du modèle.

**Dernier score de suite — campagne `claude-v1.0.3-r3`**, achevée le 2026-09-16
sur les 28 cas, **mesure la v1.0.3** (skill lu depuis le dépôt, non invoqué
nativement) : **27 RÉUSSITE / 1 DEMI-RÉUSSITE / 0 ÉCHEC**.

**Le seuil de release est atteint pour la première fois** : ≥ 25 sur 28 **et**
zéro échec sur les neuf cas critiques (13, 18, 22 à 28), tous en RÉUSSITE.

| Campagne | Version mesurée | RÉUSSITE | DEMI | ÉCHEC | Échecs critiques |
|---|---|---|---|---|---|
| `r1` | 1.0.0 | 16 | 5 | 7 | 3 (cas 24, 25, 26) |
| `r2` | 1.0.1 | 20 | 7 | 1 | 1 (cas 13) |
| `r3` | 1.0.3 | **27** | 1 | **0** | **0** |

Les trois campagnes portent la même empreinte de suite SHA-256 : elles sont
comparables.

**`r3` mesurait deux correctifs à la fois, et les deux effets se lisent
séparément.** Le **cas 13**, seul échec de `r2` et cas critique, passe en
RÉUSSITE : c'est le correctif de fond de la v1.0.2, qui a distingué l'effet de
la saisine de la chambre régionale des comptes selon son fondement —
dessaisissement de l'assemblée sur budget non voté (CGCT, art. L. 1612-2),
maintien de sa compétence sur déséquilibre réel (art. L. 1612-5). **Six des sept
demi-réussites** de `r2` passent en RÉUSSITE : c'est le correctif de traçabilité
de la v1.0.3. Le renvoi de fichier non nommé, cause dominante relevée par les
quatre juges de `r1` et de `r2`, n'est plus relevé sur aucun cas du run.

**Aucune régression** : tout cas classé RÉUSSITE en `r2` l'est encore en `r3`.

Enseignement central de cette version : **une exigence qui ne figure que dans le
jeu de test n'est pas une règle du skill.** Elle se mesure, mais rien ne la
produit. Elle a été mesurée deux campagnes durant avant d'être prescrite.

**Ce qui reste ouvert** : le cas 7 demeure en demi-réussite, pour trois attendus
métier manquants — caractère non budgétaire de la ligne de trésorerie,
interdiction de financer du fonctionnement par l'emprunt, renvoi à
`objets/emprunt.md`. Ni un défaut de traçabilité, ni un défaut de provenance.
Correctif candidat pour une v1.0.4, non bloquant. Détail dans
`tests/runs/claude-v1.0.3-r3/RAPPORT.md`.

## Licence

CC BY-SA 4.0 — voir `LICENSE`.
