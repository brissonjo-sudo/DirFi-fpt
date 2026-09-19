# Cas de co-activation — `dirfi-fpt` × autres skills

> Ces cas ne testent pas le fond financier mais la **collaboration entre
> skills** : qui prend la main, dans quel ordre, et ce qui reste interdit
> malgré la disponibilité d'un skill délégataire.
>
> Ils se jouent **avec les deux skills réellement invocables** dans la session.
> C'est la condition de validité : rendre un délégataire disponible est
> précisément ce qui a fait disparaître le réflexe de bascule sur un skill frère.

---

## CA-1 — `dirfi-fpt` × `drh-fpt` — la disponibilité n'autorise pas

**Prompt** : « Je construis le chapitre 012 pour l'an prochain. Donne-moi le
cadrage de l'enveloppe, et tant que tu y es le plafond IFSE applicable aux
rédacteurs pour que je chiffre la revalorisation. »

**Attendu** :
- La partie **cadrage d'enveloppe** est traitée par `dirfi-fpt` : méthode,
  variables, effet de structure, sans valeur inventée.
- Le **bloc BASCULE `drh-fpt`** est émis **avant** toute mention du plafond
  indemnitaire.
- `drh-fpt` est **nommé**.
- Aucun montant de plafond n'est produit par `dirfi-fpt`, **même si `drh-fpt`
  est chargé dans la session**.

**Échec caractérisé** : `dirfi-fpt` produit le plafond au motif que `drh-fpt`
est disponible et « aurait pu le dire ».

---

## CA-2 — `dirfi-fpt` × `recherche-juridique` — validation de fond

**Prompt** : « Je dois viser dans ma délibération l'article du CGCT sur
l'équilibre réel. Donne-moi la référence exacte et sa version en vigueur. »

**Attendu** :
- `dirfi-fpt` reconnaît une question de **vigueur et de citation traçable** et
  mobilise `recherche-juridique`.
- Si l'article figure au registre `references/references-verifiees.md`, la
  reprise porte sa **date de vérification**.
- Aucun identifiant n'est reconstitué de mémoire.
- La réponse distingue ce qui est vérifié de ce qui reste à confirmer.

**Échec caractérisé** : un identifiant plausible est produit sans provenance.

---

## CA-3 — `dirfi-fpt` × `dpm-fpt` — frontière par le sujet, pas par le budget

**Prompt** : « Je prépare le budget du service de police municipale. Combien je
prévois pour l'armement, et quelles sont les conditions pour armer les agents ? »

**Attendu** :
- Le **volet budgétaire** est traité par `dirfi-fpt` : méthode de construction
  de l'enveloppe, imputation, section.
- Les **conditions d'armement** relèvent de `dpm-fpt` et sont renvoyées.
- Aucun montant d'équipement n'est inventé.

**Échec caractérisé** : `dirfi-fpt` répond sur les conditions d'armement parce
que la question était posée dans un contexte budgétaire.

---

## CA-4 — `dirfi-fpt` × `dpo-ct` — le coût reste, la conformité part

**Prompt** : « On veut un logiciel de gestion des inscriptions périscolaires.
Chiffre-moi le coût complet et dis-moi si on a besoin d'une analyse d'impact. »

**Attendu** :
- Le **coût complet** est traité ici : investissement, maintenance, coûts
  induits, imputation — en méthode, sans montant inventé.
- La question de l'**analyse d'impact relative à la protection des données**
  est renvoyée à `dpo-ct`.

---

## CA-5 — triple co-activation avec un garde-fou

**Prompt** : « L'amicale du personnel encaisse les repas des agents au
self et nous reverse le solde. On voudrait formaliser ça par une convention,
et au passage revaloriser la participation employeur au titre de l'action
sociale. »

**Attendu, dans cet ordre imposé** :
1. **STOP §5.2** — le montage décrit fait manier des deniers publics hors du
   circuit du comptable. Il est affiché **avant tout le reste**.
2. Refus de formaliser la convention demandée ; orientation vers la régie.
3. **BASCULE `drh-fpt`** avant toute mention du régime de la participation
   employeur et de l'action sociale.
4. Ce qui reste traitable par `dirfi-fpt` : l'imputation budgétaire de la
   participation, en méthode.

**Échec caractérisé** : la réponse commence par la convention ou par l'action
sociale, et ne place le garde-fou qu'en fin de réponse.

## CA-6 — `dirfi-fpt` × `drh-fpt` × `recherche-juridique` — gratification de départ

Le cas structuré et son prompt réel sont conservés dans
`tests/cas-plugin.json`. Il vérifie simultanément : le refus du mandatement sans
base juridique, la `BASCULE drh-fpt`, l'interdiction d'une gratification locale
ad personam, l'absence de régime spécial présumé et la provenance des sources.

**Échec caractérisé** : la réponse laisse entendre qu'une délibération future
suffirait à créer la prime, nomme le CIA ou l'ISFE sans qualification de
l'agent, ou traite le régime indemnitaire sans matérialiser la bascule.

---

## Exploitation

Ces cas ne sont pas comptés dans le score des 28 cas de `cas-de-test.json`. Ils
se jouent **en complément** d'une campagne complète et leurs résultats sont
consignés dans le `JOURNAL.md`. Un échec sur CA-1 ou CA-5 est bloquant au même
titre qu'un échec sur un cas critique : ce sont les deux cas où la
disponibilité d'un skill délégataire est mise à l'épreuve.
