# Exercices SQL - Préparation Test Digital City

**Basé sur :** Partie 1 (Modélisation relationnelle) + Partie 2 (Requêtes simples) + 1 Bonus Partie 3

---

## 🗄️ Partie 1 — Modélisation Relationnelle

**Exercice 1 — Identifier les clés primaires**

Regarde ta base `panamapapers`. Réponds à ces questions sans écrire de code :

1. Quelle est la clé primaire de la table `entity` ?
2. Quelle est la clé primaire de la table `address` ?
3. Quelle est la clé primaire de la table `officer` ?

*Notions : clé primaire, unicité, identification*

---

**Exercice 2 — Identifier les clés étrangères**

Toujours sans code, réponds :

1. Quelle colonne dans `entity` pointe vers `address` ?
2. Quelle colonne dans `assoc_officer_entity` pointe vers `officer` ?
3. Quelle colonne dans `assoc_officer_entity` pointe vers `entity` ?

*Notions : clé étrangère, références, relations*

---

**Exercice 3 — Types d'associations**

Pour chaque paire de tables, dis quel type d'association les lie (1-1, 1-N, N-N) :

1. `entity` et `address` → ?
2. `entity` et `officer` → ?
3. `assoc_officer_entity` et `entity` → ?

*Notions : associations, cardinalités, tables d'association*

---

**Exercice 4 — Modélisation complète**

Dessine (ou décris) le schéma de ta base `panamapapers` :

- Les 3 tables principales : entity, address, officer
- Les clés primaires (PK)
- Les clés étrangères (FK)
- Les types d'associations (1-N, N-N)

*Notions : modèle entité-association, schéma relationnel*

---

## 🗄️ Partie 2 — Requêtes Simples

**Exercice 5 — SELECT basique**

Affiche le `name` et le `status` de toutes les entités.

*Notions : SELECT, FROM*

---

**Exercice 6 — SELECT avec WHERE**

Affiche le `name` de toutes les entités dont le `status` est `"Active"`.

*Notions : SELECT, FROM, WHERE*

---

**Exercice 7 — SELECT avec WHERE et AND**

Affiche le `name` et `jurisdiction` de toutes les entités dont le `status` est `"Active"` ET la `jurisdiction` est `"BAH"`.

*Notions : SELECT, FROM, WHERE, AND*

---

**Exercice 8 — Jointure simple (2 tables)**

Affiche le `name` de chaque entité ainsi que son `address` correspondante.

*Notions : JOIN, ON, clés étrangères*

---

**Exercice 9 — Jointure avec WHERE**

Affiche le `name` et `address` de toutes les entités dont le `status` est `"Active"` (en joignant entity et address).

*Notions : JOIN, WHERE, filtrage après jointure*

---

## 🌟 Bonus — Partie 3 (Optionnel)

**Exercice 10 — GROUP BY et COUNT**

Compte combien d'entités actives il y a par juridiction.

Résultat attendu : juridiction | nombre d'entités

*Notions : GROUP BY, COUNT(), agrégation*

---

## 📝 Conseils pour les exos

1. **Exo 1-4** : Réfléchis d'abord, puis vérifie dans SQLiteStudio
2. **Exo 5-9** : Écris ta requête, teste-la, compare avec d'autres solutions
3. **Exo 10** : Bonus — fais-le si tu as du temps

## ⏱️ Timing conseillé

- **Exo 1-4** : 30 min (modélisation)
- **Exo 5-9** : 1h (requêtes)
- **Exo 10** : 15 min (bonus)

**Total : 1h45 par session SQL**