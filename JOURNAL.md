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
