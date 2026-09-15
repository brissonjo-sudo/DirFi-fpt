# Changelog — `dirfi-fpt`

Versionnage sémantique **MAJEUR.MINEUR.PATCH**.

- **MAJEUR** — changement d'architecture ou de périmètre, rupture de compatibilité.
- **MINEUR** — nouvelle branche, nouvel objet, nouveau générateur, nouvelle frontière.
- **PATCH** — correctif de fond, précision, mise à jour de source.

---

## [1.0.2] — 2026-09-15 — l'effet de la saisine dépend de son fondement

Correctif issu de la campagne `claude-v1.0.1-r2` (28 cas, mesure de la v1.0.1) :
**20 RÉUSSITE / 7 DEMI-RÉUSSITE / 1 ÉCHEC**, contre 16 / 5 / 7 en `r1`.

### Confirmé par la mesure

Le correctif d'auto-attestation de la v1.0.1 **tient**. Les trois échecs
critiques de `r1` (cas 24, 25, 26) passent tous en réussite, comme les cas 1, 3,
5 et 20 qui relevaient du même mécanisme. Aucune auto-attestation nue n'est
relevée sur l'ensemble du run.

### Corrigé

- **Effet de la saisine de la chambre régionale des comptes**
  (`references/controle-budgetaire.md` §6.2, tableau §5 et piège §8 ;
  `references/references-verifiees.md` §2) — **erreur de fond**, révélée par
  l'unique échec de `r2` et vérifiée à la source avant correction.

  Le skill affirmait que la saisine « ne dessaisit pas immédiatement »
  l'assemblée et en faisait un piège à éviter. C'est l'inverse pour le cas le
  plus fréquent : en cas de **budget non voté**, l'organe délibérant ne peut
  adopter aucune délibération sur le budget de l'exercice en cours **à compter
  de la saisine** et jusqu'au règlement préfectoral (CGCT, art. L. 1612-2, al. 2
  — identifiant au registre, vérifié le 2026-09-15). Conséquence opérationnelle
  désormais opposable : **convoquer l'assemblée pour voter en urgence après la
  saisine est une fausse solution**, la délibération serait prise par une
  autorité dessaisie.

  En revanche, pour un **budget voté en déséquilibre réel** (art. L. 1612-5),
  aucune clause de dessaisissement n'existe : la chambre demande une nouvelle
  délibération et l'assemblée reste pleinement compétente.

  Le piège §8 devient donc l'inverse de ce qu'il était : ce n'est plus « croire
  que la saisine dessaisit » qui est faux, c'est **énoncer une règle unique**
  pour les deux cas.
- **`references/references-verifiees.md`** — L. 1612-5 passe de « non vérifié »
  à vérifié, avec son identifiant ; une note opposable consigne la règle
  différenciée.

### Non corrigé — assumé

Les **renvois de fichiers non nommés** restent la cause dominante des
7 demi-réussites, comme des 5 de `r1`. Toujours pas traité, pour la même
raison : isoler l'effet de chaque correctif d'une campagne à l'autre.

### À faire

Campagne `r3` requise pour scorer la v1.0.2. Le seuil de release reste non
atteint : il manque 5 réussites, et l'échec critique du cas 13 doit être
reverifié sur la version corrigée.

---

## [1.0.1] — 2026-09-15 — l'auto-attestation ne vaut plus provenance

Correctif issu de la **première campagne d'évaluation** (`claude-v1.0.0-r1`,
28 cas, skill lu depuis le dépôt) : **16 RÉUSSITE / 5 DEMI-RÉUSSITE / 7 ÉCHEC**,
dont 3 échecs sur les 9 cas critiques. Seuil de release non atteint.

### Corrigé

- **Auto-attestation de vérification** (`SKILL.md` §5.4,
  `references/socle-sources-verification.md` §8) — cause de **six des sept
  échecs**. Le skill exigeait « vérifié à la source ou réserve », mais rien ne
  distinguait une vérification réelle d'une affirmation du modèle disant l'avoir
  faite. Les réponses produisaient des formules — « vérifié ce jour », « source
  consultée », « vérifié en direct sur Légifrance » — qui miment la trace sans
  en provenir, puis livraient la valeur.

  Désormais, une provenance opposable porte **trois éléments** : la source
  nommée, le **point d'entrée obtenu** (URL ou identifiant), et la date de
  consultation. Les trois, ou la référence est marquée `⚠️ non vérifié`, ou
  elle est retirée. Et **sans outil de vérification disponible dans la session,
  aucune valeur ni aucun identifiant ne sort** : on livre la méthode et
  l'adresse où vérifier.
- **Frontière illustrée** (`SKILL.md` §5.6) — cause du septième échec. Le skill
  signalait correctement la passation des marchés hors périmètre, puis en
  donnait « quelques pistes » : axes d'allotissement, critères de sélection.
  L'illustration **était** la réponse que la frontière refusait. Signaler une
  limite n'autorise plus à l'illustrer, l'esquisser ou l'exemplifier.
- **Auto-vérification** (`SKILL.md` §7) — deux points ajoutés, portant la liste
  à 16 : le test d'auto-attestation (« ai-je réellement appelé une source, ou
  suis-je en train d'affirmer que je l'ai fait ? ») et le test de frontière non
  illustrée.
- **`scripts/eval_suite.py`** — accepte la note du juge sous `notes` ou sous
  `justification` : les deux intitulés ont circulé dans les consignes, et
  refuser l'un des deux invalidait un run complet pour une question de nommage.

### Précisé

- **`tests/bareme-cas-de-test.md` §3.3** — ce qui compte comme provenance est
  désormais explicite, après que deux juges ont buté sur le point. Une valeur
  portant les trois éléments n'est **pas** un échec, même si l'attendu du cas
  demandait qu'elle soit « marquée à vérifier » : le skill autorise la valeur
  réellement vérifiée. C'est l'auto-attestation qui est sanctionnée, pas le
  chiffre.

### Non corrigé — assumé pour cette version

- **Renvois de fichiers non nommés.** Les trois juges l'ont relevé
  indépendamment : les réponses décrivent le bon contenu mais ne citent pas le
  chemin du fichier mobilisé. C'est la cause dominante des 5 demi-réussites.
  Non éliminatoire, et corriger deux causes à la fois empêcherait d'attribuer
  l'effet de chacune à la campagne `r2`.

### À faire

Campagne `r2` requise pour scorer la v1.0.1 : cette version est **postérieure à
la mesure** et n'est couverte par aucune campagne.

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
