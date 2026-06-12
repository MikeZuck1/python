Plan d'entraînement IA Integration specialist.

---

**Ce qui est demandé dans le test**

- **Python** : algorithmique de base
- **SQL** : partie 1 (modélisation relationnelle) + partie 2 (requêtes simples)

---

## Exercices Python

**Exercice 1 — Conditions et boucles**

Écris un programme qui affiche tous les nombres de 1 à 50, mais :
- Si le nombre est divisible par 3 → affiche `"Fizz"`
- Si le nombre est divisible par 5 → affiche `"Buzz"`
- Si divisible par les deux → affiche `"FizzBuzz"`
- Sinon → affiche le nombre

*Notions : boucles, conditions, modulo `%`*

---

**Exercice 2 — Fonctions et dictionnaires**

Crée une liste de 5 clients sous forme de dictionnaires :
```python
clients = [
    {"nom": "Alice", "age": 30, "ville": "Bruxelles"},
    ...
]
```
Écris une fonction qui prend cette liste et retourne uniquement les clients qui habitent à Bruxelles.

*Notions : listes, dictionnaires, fonctions, conditions*

---

**Exercice 3 — Manipulation de données**

Écris un programme qui :
1. Crée une liste de 10 nombres aléatoires entre 1 et 100
2. Calcule la moyenne
3. Affiche les nombres supérieurs à la moyenne

*Notions : listes, boucles, fonctions, `random`*

---

**Exercice 4 — Algorithme de recherche**

Écris une fonction `recherche(liste, valeur)` qui parcourt une liste et retourne `True` si la valeur est trouvée, `False` sinon. Sans utiliser `in` ou `.index()`.

*Notions : fonctions, boucles, conditions*

---

## Exercices SQL

*(sur ta base `panamapapers`)*

**Exercice 1 — SELECT simple**

Affiche le `name` et la `jurisdiction` de toutes les entités dont le statut est `"Active"` et dont la juridiction est `"BAH"` (Bahamas).

*Notions : SELECT, WHERE, AND*

---

**Exercice 2 — Clé primaire / modélisation**

Réponds à ces questions sans écrire de code :
- Quelle est la clé primaire de la table `entity` ?
- Quelle est la clé étrangère qui lie `assoc_officer_entity` à `officer` ?
- Quel type d'association lie `entity` et `officer` ? (1-1, 1-N, N-N)

*Notions : modélisation relationnelle*

---

**Exercice 3 — Jointure simple**

Affiche le `name` de chaque entité ainsi que l'`address` correspondante en joignant `entity` et `address`.

*Notions : JOIN, ON*

---

**Exercice 4 — Jointure + filtre**

Affiche le nom des officers liés à des entités dont la juridiction est `"BAH"`, en passant par la table `assoc_officer_entity`.

*Notions : jointure sur 3 tables, WHERE*

---

**Plan jusqu'au 2-3 juillet**

| Jour | À faire |
|---|---|
| Aujourd'hui | Python exo 1 + 2 |
| Demain | Python exo 3 + 4 |
| Après-demain | SQL exo 1 + 2 |
| J-2 | SQL exo 3 + 4 |
| J-1 | Révision générale + relecture |