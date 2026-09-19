# Journal des cas — `dirfi-fpt`

> Matière première de l'amélioration du skill. Une entrée par cas significatif :
> lacune constatée, erreur produite, cas nouveau non couvert, écrit récurrent à
> modéliser.
>
> **Règle stricte — aucune donnée nominative.** Ni agent, ni élu, ni administré,
> ni bénéficiaire, ni nom d'association, ni nom de collectivité. Anonymiser à
> l'écriture, pas après.
>
> Les entrées traitées remontent vers `CHANGELOG.md` à la montée de version.

## Format d'une entrée

```
### AAAA-MM-JJ — [titre court]

- **Type** : lacune | erreur | cas nouveau | écrit récurrent
- **Branche** : [fichier de references/ ou objets/ concerné]
- **Contexte (anonymisé)** : [situation, sans aucun élément identifiant]
- **Constat** : [ce que le skill a fait, ou n'a pas su faire]
- **Action proposée** : [modification envisagée, et où]
- **Statut** : à traiter | intégré vX.Y.Z
```

---

## Entrées

### 2026-09-19 — Prime ponctuelle de départ : bonne conclusion, routage implicite

- **Type** : erreur
- **Branche** : `SKILL.md` §5.5, `references/analyse-situation.md`
- **Contexte (anonymisé)** : demande de mandatement immédiat d'une gratification
  individuelle avant le départ à la retraite d'un agent, avec crédits ouverts
  mais sans délibération ni décision individuelle.
- **Constat** : le plugin a correctement refusé le paiement et vérifié les
  sources, mais n'a pas matérialisé la bascule DirFi vers DRH, a cité un régime
  spécial sans avoir confirmé la filière et n'a pas assez nettement indiqué
  qu'une délibération ne peut créer librement une prime ad personam.
- **Action proposée** : expliciter la co-activation dans les agrégateurs,
  interdire le nom d'un régime avant qualification de l'agent et ajouter le cas
  réel à une suite plugin séparée.
- **Statut** : intégré v1.0.4

### 2026-09-15 — Création du skill

- **Type** : cas nouveau
- **Branche** : ensemble du dépôt
- **Contexte (anonymisé)** : besoin d'un troisième skill métier territorial, aux
  côtés des volets ressources humaines et police municipale.
- **Constat** : aucun outil ne couvrait les finances locales. Le risque
  spécifique du domaine — citer une valeur chiffrée périmée avec assurance —
  n'était traité par aucun dispositif existant.
- **Action proposée** : architecture en 4 couches reprise de `dpm-fpt`, double
  garde-fou propre au métier, régime des valeurs chiffrées à deux vitesses.
- **Statut** : intégré v1.0.0

### 2026-09-15 — Chaîne d'invariant cassée par un retour à la ligne

- **Type** : erreur
- **Branche** : `SKILL.md` §5.5
- **Contexte (anonymisé)** : mise en place de la validation statique du dépôt.
- **Constat** : l'invariant « ne vaut pas bascule » était cassé en deux par un
  retour à la ligne de mise en forme. Le contrôle verbatim échouait alors que le
  texte était présent et correct à la lecture humaine.
- **Action proposée** : reformuler pour que les chaînes figées par
  `validate_repo.py` tiennent sur une seule ligne. Enseignement général — une
  chaîne d'invariant ne doit jamais être coupée par le rehabillage du texte.
- **Statut** : intégré v1.0.0

### 2026-09-15 — Identifiants de cas numériques non supportés par la suite d'évaluation

- **Type** : erreur
- **Branche** : `scripts/eval_suite.py`
- **Contexte (anonymisé)** : premier essai de préparation d'une campagne.
- **Constat** : `eval_suite.py prepare` levait une `TypeError` parce que les
  identifiants de `tests/cas-de-test.json` sont numériques et qu'un chemin ne
  se construit pas avec un entier. Le script frère dont il dérive utilisait des
  identifiants textuels, l'incompatibilité était invisible à la lecture.
- **Action proposée** : normaliser le nom de dossier d'un cas dans une fonction
  dédiée, avec un zéro-padding pour que l'ordre alphabétique des dossiers suive
  l'ordre des cas. Enseignement général — un script repris d'un dépôt frère doit
  être **exécuté** sur les données du nouveau dépôt, pas seulement relu.
- **Statut** : intégré v1.0.0

### 2026-09-15 — Le modèle s'auto-atteste une vérification qu'il n'a pas faite

- **Type** : erreur
- **Branche** : `SKILL.md` §5.4, `references/socle-sources-verification.md` §8
- **Contexte (anonymisé)** : première campagne d'évaluation, 28 cas.
- **Constat** : six des sept échecs suivent le même mécanisme. Le modèle ne
  s'abstient pas de chiffrer — il chiffre, puis adosse la valeur à une
  provenance qu'il s'attribue lui-même (« vérifié ce jour », « source
  consultée »), sans appel d'outil réel. La règle de sourcing distinguait
  « valeur nue » et « valeur sourcée », mais pas « sourcée par un appel d'outil »
  de « sourcée par une affirmation du modèle ». La réserve servait alors de
  déguisement plutôt que de frein — et une valeur faussement attestée est plus
  dangereuse qu'une valeur nue, parce qu'elle désarme la vigilance du lecteur.
- **Action proposée** : provenance opposable à trois éléments obligatoires
  (source nommée, point d'entrée obtenu, date) ; interdiction de produire une
  valeur quand aucun outil de vérification n'est disponible ; test à charge
  ajouté à l'auto-vérification.
- **Statut** : intégré v1.0.1

### 2026-09-15 — Une frontière signalée puis illustrée

- **Type** : erreur
- **Branche** : `SKILL.md` §5.6
- **Contexte (anonymisé)** : cas critique portant sur la passation d'un marché,
  explicitement hors périmètre du skill.
- **Constat** : la réponse signale correctement la limite, puis livre « quelques
  pistes » — axes d'allotissement, triptyque de critères de sélection.
  L'illustration constitue exactement la réponse que la frontière refusait. Le
  préambule de refus n'y change rien.
- **Action proposée** : énoncer qu'une frontière ne s'illustre pas. Après le
  signalement : nommer l'interlocuteur compétent, puis s'arrêter.
- **Statut** : intégré v1.0.1

### 2026-09-15 — Renvois de fichiers non nommés

- **Type** : lacune
- **Branche** : transverse
- **Contexte (anonymisé)** : campagne d'évaluation, relevé indépendamment par
  les trois juges.
- **Constat** : les réponses décrivent le bon contenu mais ne citent pas le
  chemin du fichier mobilisé — « l'instruction M57 » au lieu de
  `references/nomenclature-m57.md`. Non éliminatoire pris isolément, mais c'est
  la cause dominante des cinq demi-réussites.
- **Action proposée** : à traiter après la campagne `r2`. Corriger deux causes
  en même temps empêcherait d'attribuer l'effet de chacune.
- **Statut** : à traiter

### 2026-09-15 — Le barème ne disait pas ce qui compte comme provenance

- **Type** : lacune
- **Branche** : `tests/bareme-cas-de-test.md` §3.3
- **Contexte (anonymisé)** : deux juges ont signalé la même tension sur des lots
  différents.
- **Constat** : les attendus de certains cas exigeaient qu'une valeur soit
  « marquée à vérifier », alors que le barème admettait par ailleurs une
  « provenance datée ». Un juge a dû arbitrer seul, et le verdict de deux cas en
  dépendait. Le barème décrivait ce qui était sanctionné sans définir ce qui
  était suffisant.
- **Action proposée** : expliciter les trois éléments d'une provenance opposable
  dans le barème, et poser qu'une valeur réellement vérifiée n'est pas un échec.
- **Statut** : intégré v1.0.1

### 2026-09-15 — Erreur de fond sur l'effet de la saisine de la CRC

- **Type** : erreur
- **Branche** : `references/controle-budgetaire.md` §6.2, §5, §8
- **Contexte (anonymisé)** : unique échec de la campagne `r2`, sur un cas
  critique portant sur un budget non voté dans les délais.
- **Constat** : la réponse affirmait que l'assemblée conserve sa compétence tant
  que le préfet n'a pas réglé le budget, et conseillait de la convoquer en
  urgence. Elle **suivait fidèlement le skill** : la branche posait cette règle
  et en faisait même un piège à éviter (« croire que la saisine dessaisit —
  faux »). Vérification faite à la source, c'est le skill qui avait tort pour ce
  cas de saisine : l'organe délibérant est dessaisi dès la saisine. La règle est
  en revanche inverse pour un budget voté en déséquilibre réel, où l'assemblée
  reste compétente.
- **Action proposée** : distinguer explicitement les deux cas de saisine, poser
  la conséquence opérationnelle (convoquer l'assemblée après la saisine est une
  fausse solution), retourner le piège §8, et consigner la règle au registre
  vérifié.
- **Enseignement général** : une campagne d'évaluation ne mesure pas seulement
  la forme des réponses. Ici, un juge a signalé une contradiction avec le droit,
  et c'est le contenu du skill — relu plusieurs fois — qui était faux. Un cas de
  test bien écrit trouve ce qu'aucune relecture ne trouve.
- **Statut** : intégré v1.0.2

### 2026-09-15 — Le correctif d'auto-attestation tient

- **Type** : cas nouveau
- **Branche** : `SKILL.md` §5.4
- **Contexte (anonymisé)** : campagne `r2`, mesure de la v1.0.1.
- **Constat** : les sept échecs de `r1` relevaient à six reprises de
  l'auto-attestation. En `r2`, tous passent, et aucune auto-attestation nue
  n'est relevée sur les 28 réponses. La règle de provenance à trois éléments a
  été décisive sur plusieurs cas, en distinguant une valeur réellement vérifiée
  d'une valeur habillée d'une formule.
- **Action proposée** : aucune. Conserver la règle en l'état et la mesurer à
  nouveau en `r3`.
- **Statut** : intégré v1.0.1, confirmé par `r2`

### 2026-09-15 — Les réponses ne nomment pas le fichier qu'elles mobilisent

- **Type** : lacune
- **Branche** : `SKILL.md` §4 et §7
- **Contexte (anonymisé)** : cause dominante des 7 demi-réussites de `r2`, déjà
  des 5 de `r1`. Relevée indépendamment par les trois juges des deux campagnes.
- **Constat** : les réponses décrivent le bon contenu, appliquent la bonne
  règle, mais citent la notion (« l'instruction M57 ») au lieu du chemin
  (`references/nomenclature-m57.md`). Le skill demandait de « signaler le lien »
  sans jamais exiger de nommer le fichier — l'exigence figurait dans les
  attendus des cas, pas dans la règle. Un défaut non éliminatoire, mais qui
  suffit à faire basculer un cas hors de la réussite dès qu'il s'ajoute à un
  second manque.
- **Action proposée** : rendre la traçabilité obligatoire et **motivée** —
  vérifier, corriger, distinguer la source interne de la mémoire du modèle — et
  l'ajouter à l'auto-vérification.
- **Enseignement général** : une exigence qui ne figure que dans le jeu de test
  n'est pas une règle du skill. Elle se mesure, mais rien ne la produit.
- **Statut** : intégré v1.0.3

### 2026-09-16 — ligne de trésorerie : l'objet écarté n'est pas nommé

- **Type** : lacune
- **Branche** : `references/dette-tresorerie.md`, `objets/emprunt.md`
- **Contexte (anonymisé)** : décalage de trésorerie en attendant le versement
  d'une subvention notifiée ; question posée en termes d'emprunt.
- **Constat** : le fond est juste — la ligne de trésorerie est bien désignée,
  la compétence et la délégation sont traitées, aucune valeur n'est inventée.
  Mais trois éléments manquent : le **caractère non budgétaire** de la ligne de
  trésorerie n'est jamais énoncé, l'**interdiction de financer une dépense de
  fonctionnement par l'emprunt** n'apparaît pas en toutes lettres, et
  `objets/emprunt.md` est écarté sans être nommé. Écarter un objet est une
  décision : elle se trace comme une mobilisation.
- **Action proposée** : poser explicitement dans `references/dette-tresorerie.md`
  le caractère non budgétaire de la ligne de trésorerie et l'interdiction de
  l'emprunt pour le fonctionnement ; étendre la règle de traçabilité du
  `SKILL.md` §4 au cas de l'objet **écarté**, pas seulement mobilisé.
- **Statut** : à traiter

### 2026-09-16 — la branche du cas n'est pas celle qui est citée

- **Type** : lacune
- **Branche** : `references/retex.md`, `references/controle-interne-financier.md`
- **Contexte (anonymisé)** : retour d'expérience après un incident d'exécution.
- **Constat** : la réponse cite `references/controle-interne-financier.md` et
  ne nomme jamais `references/retex.md`, qui est pourtant la branche du cas. La
  règle de traçabilité de la v1.0.3 est respectée dans sa forme — un chemin est
  bien cité — mais le chemin cité n'est pas le bon. Nommer un fichier ne
  garantit pas d'avoir emprunté la bonne route.
- **Action proposée** : vérifier le routage de `references/analyse-situation.md`
  vers `references/retex.md` ; la frontière entre retour d'expérience et
  contrôle interne est probablement trop faible dans le routeur.
- **Statut** : à traiter

### 2026-09-16 — rattachement et reste à réaliser ne sont pas distingués

- **Type** : lacune
- **Branche** : `references/budget-cycle.md`
- **Contexte (anonymisé)** : clôture d'exercice, dépenses engagées non
  mandatées.
- **Constat** : la réponse distingue correctement rattachement et journée
  complémentaire, mais ne distingue pas **rattachement et reste à réaliser** —
  la confusion la plus fréquente sur ce sujet, et celle qui a les effets
  comptables les plus lourds.
- **Action proposée** : ajouter la distinction au corps de
  `references/budget-cycle.md` et en faire un piège explicite de sa section
  « Pièges & confusions fréquentes ».
- **Statut** : à traiter
