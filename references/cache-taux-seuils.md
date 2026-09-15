# Cache — taux, seuils et valeurs vérifiées

> ⚠️ **Cache indicatif, jamais une source primaire.** Ce fichier est un
> **artefact de maintenance du dépôt**. Il n'est **pas** inclus dans le package
> d'exécution (`scripts/package_skill.py` l'exclut) et ne doit **jamais** être
> cité comme source dans une réponse.
>
> Il sert à une seule chose : garder la trace de ce qui a déjà été vérifié, avec
> **quand** et **où**, pour savoir ce qu'il faut recontrôler. Une valeur
> présente ici reste soumise à la règle du `SKILL.md` §5.4 : **elle se
> revérifie à la date d'usage**.
>
> Les **identifiants de textes** (LEGIARTI, JORFTEXT, NOR) ne vont pas ici mais
> dans `references-verifiees.md`. Ce fichier ne contient que des **valeurs
> chiffrées**.

---

## 1. Pourquoi ce fichier existe

Les finances locales sont le domaine où les valeurs se périment le plus vite :
la plupart changent **au 1er janvier**, certaines en cours d'exercice. Une
valeur mémorisée par le modèle est, statistiquement, une valeur fausse.

Ce cache matérialise cette réalité. Une cellule vide n'est **pas** une invitation
à combler le vide : c'est l'état normal tant que la vérification n'a pas eu
lieu.

**Règle absolue** : si une valeur demandée ne figure pas ici avec une date de
vérification récente, la réponse **ne la donne pas**. Elle donne la méthode, la
formule, et indique où vérifier.

---

## 2. Valeurs vérifiées

*Aucune valeur vérifiée à ce jour.* Le skill est en v1.0.0 et n'a pas encore
fait l'objet d'une campagne de vérification de valeurs.

| Objet | Valeur | Date d'effet | Source | Vérifié le | Statut |
|---|---|---|---|---|---|
| — | — | — | — | — | *à renseigner* |

---

## 3. Valeurs à vérifier en priorité

Liste de ce qui est le plus souvent demandé et le plus souvent faux. À remplir
au fil des vérifications réelles, **jamais de mémoire**.

### 3.1 Cycle budgétaire

| Objet | Source à consulter | Statut |
|---|---|---|
| Date limite de vote du budget primitif | CGCT, Légifrance | *à renseigner* |
| Date limite de vote du compte administratif | CGCT, Légifrance | *à renseigner* |
| Délai entre le débat d'orientation budgétaire et le vote du budget | CGCT, Légifrance | *à renseigner* |
| Seuil démographique déclenchant l'obligation de rapport d'orientation budgétaire | CGCT, Légifrance | *à renseigner* |
| Bornes de la journée complémentaire | Instruction M57, DGFiP | *à renseigner* |
| Seuil de déficit du compte administratif ouvrant la saisine de la CRC | CGCT, Légifrance | *à renseigner* |
| Quotité de dépenses d'investissement engageable avant le vote du budget | CGCT, Légifrance | *à renseigner* |

### 3.2 Exécution

| Objet | Source à consulter | Statut |
|---|---|---|
| Délai global de paiement applicable aux collectivités | Textes commande publique, DAJ | *à renseigner* |
| Taux des intérêts moratoires et indemnité forfaitaire de recouvrement | Textes commande publique, DAJ | *à renseigner* |
| Taux de l'intérêt légal en vigueur | Banque de France, Légifrance | *à renseigner* |
| Seuils de dispense de pièces justificatives | Nomenclature des pièces justificatives, DGFiP | *à renseigner* |

### 3.3 Recettes, fiscalité et dotations

| Objet | Source à consulter | Statut |
|---|---|---|
| Coefficient de revalorisation forfaitaire des bases | Loi de finances de l'année | *à renseigner* |
| Règles et taux plafonds de lien entre les taux | CGI, Légifrance | *à renseigner* |
| Taux du fonds de compensation pour la TVA | Loi de finances, DGCL | *à renseigner* |
| Montants et critères de répartition de la DGF de l'année | DGCL, portail des dotations | *à renseigner* |
| Seuil de prescription de l'action en recouvrement | CGCT / CGI, Légifrance | *à renseigner* |

### 3.4 Subventions et commande publique

| Objet | Source à consulter | Statut |
|---|---|---|
| Seuil de subvention déclenchant l'obligation de convention | Textes relatifs aux associations, Légifrance | *à renseigner* |
| Seuils de procédure de la commande publique | DAJ, code de la commande publique | *à renseigner* |
| Taux d'avance obligatoire et seuil de déclenchement | Code de la commande publique | *à renseigner* |
| Taux plafond de la retenue de garantie | Code de la commande publique | *à renseigner* |

### 3.5 Dette et analyse financière

| Objet | Source à consulter | Statut |
|---|---|---|
| Seuils d'alerte de la capacité de désendettement | Doctrine CRC / Cour des comptes — **non réglementaires** | *à renseigner* |
| Ratios obligatoires à annexer au budget et leur définition | CGCT, Légifrance | *à renseigner* |
| Plafonds prudentiels des garanties d'emprunt | CGCT, Légifrance | *à renseigner* |
| Durées d'amortissement de référence par catégorie de bien | Instruction M57, DGFiP | *à renseigner* |

> **Note sur les seuils d'alerte de ratios** : ils relèvent de la **doctrine**,
> pas de la réglementation. Les présenter comme des normes juridiques est une
> erreur de qualification, indépendamment de leur exactitude chiffrée.

---

## 4. Journal des vérifications

| Date | Objet vérifié | Source | Résultat |
|---|---|---|---|
| — | — | — | *aucune vérification enregistrée* |

---

## 5. Procédure de mise à jour

1. **Revue de loi de finances (janvier)** — reprendre l'intégralité de la
   section 3.3, plus les seuils de la commande publique et le taux du FCTVA.
2. **Revue de rentrée (1er septembre)** — reprendre les sections 3.1, 3.2 et
   3.5, et contrôler les évolutions de la M57.
3. **Au fil de l'eau** — toute valeur vérifiée en séance pour répondre à une
   demande est reportée ici avec sa date et sa source.
4. **Anti-divergence** — si une valeur figure aussi dans une branche de
   `references/`, la branche est la source interne unique : modifier la branche
   d'abord, reporter ici ensuite.
5. **Péremption** — une valeur vérifiée lors d'un exercice antérieur est réputée
   **périmée**, pas « probablement encore juste ».
