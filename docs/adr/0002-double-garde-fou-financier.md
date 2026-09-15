# ADR-0002 — Deux garde-fous plutôt qu'un

**Statut** : accepté
**Date** : 2026-09-15

## Contexte

Chaque skill du pattern possède **un** garde-fou « hard stop » propre à son
métier, qui s'affiche avant tout autre contenu. Pour `dpm-fpt`, c'est le
dépassement des pouvoirs d'agent de police judiciaire adjoint.

La transposition aux finances locales bute sur un constat : deux risques
distincts justifient un arrêt, et ils n'ont ni le même fondement, ni la même
conduite à tenir.

1. Le **maniement de deniers publics hors du circuit du comptable public**.
   Fondement : la séparation de l'ordonnateur et du comptable. Sanction :
   gestion de fait, responsabilité personnelle devant le juge des comptes.
   Conduite : ne pas mettre en œuvre, saisir le comptable.
2. L'**exécution d'un acte budgétaire irrégulier** (budget non voté, déséquilibre
   réel, dépense obligatoire non inscrite). Fondement : les règles d'équilibre
   et la procédure de contrôle budgétaire. Conduite : régulariser d'abord, la
   chambre régionale des comptes pouvant être saisie.

## Décision

Retenir **deux** garde-fous distincts, avec chacun son bloc de sortie littéral,
et un ordre d'affichage imposé quand les deux se déclenchent : le STOP gestion de
fait d'abord, l'alerte budgétaire ensuite, la réponse métier après.

Le routeur de couche 1 (`references/analyse-situation.md`) porte les deux
détecteurs en section 0, avant toute qualification métier.

## Conséquences

- Le premier garde-fou est un **arrêt** : il interdit le montage. Le second est
  une **alerte** : il interdit d'exécuter en l'état mais ouvre une voie de
  régularisation. Les formulations retenues reflètent cette différence de nature.
- Le hard stop gestion de fait n'est pas une impasse : son routeur en 4 points
  oriente vers la régie, la qualification du flux, le régime des satellites, ou
  l'abstention motivée. Un garde-fou qui ne propose aucune issue régulière est
  contourné par l'utilisateur.
- `validate_repo.py` fige les deux blocs verbatim : les affaiblir devient une
  régression détectée en intégration continue.

## Alternatives écartées

- **Un garde-fou unique « irrégularité financière »** — écarté : la fusion aurait
  produit un message générique, alors que la conduite à tenir diffère
  radicalement (saisir le comptable / régulariser devant l'assemblée).
- **Traiter l'irrégularité budgétaire en simple renvoi de branche** — écarté :
  l'expérience des skills frères montre que sans bloc prioritaire, le modèle
  répond d'abord à la question technique posée et ne signale l'irrégularité
  qu'en fin de réponse, quand elle a déjà été validée implicitement.
