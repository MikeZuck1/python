
---

## Exercices Partie 1 — Créer des données avec Python

**Exercice 1 — Gestion de contacts**

Crée un programme qui :
1. Crée une liste vide `contacts`
2. Ajoute 3 contacts (chacun étant un dictionnaire avec : nom, prénom, téléphone, email)
3. Affiche tous les contacts
4. Modifie l'email du premier contact
5. Supprime le deuxième contact
6. Affiche le nombre total de contacts restants

*Notions : variables, dictionnaires, listes, append, remove, len*

---

**Exercice 2 — Gestion d'inventaire**

Crée une liste de produits avec : nom, prix, quantité en stock.

```python
produits = [
    {"nom": "Stylo", "prix": 2.5, "quantite": 100},
    {"nom": "Cahier", "prix": 5.0, "quantite": 50},
    {"nom": "Gomme", "prix": 1.0, "quantite": 200}
]
```

Écris du code qui :
- Affiche le prix du 2ème produit
- Modifie la quantité du 1er produit à 80
- Ajoute un nouveau produit
- Affiche la liste complète

*Notions : listes, dictionnaires, accès aux éléments*

---

## Exercices Partie 2 — Gérer la logique de programmation

**Exercice 3 — Calculatrice simple**

Crée une fonction `calculer(num1, num2, operation)` qui :
- Prend 2 nombres et une opération (+, -, *, /)
- Retourne le résultat
- Gère le cas division par zéro avec `if/else`

Teste la fonction avec au moins 4 opérations différentes.

*Notions : fonctions, paramètres, conditions, division par zéro*

---

**Exercice 4 — Menu validé**

Crée un programme qui :
1. Affiche un menu : "1. Addition  2. Soustraction  3. Quitter"
2. Demande à l'utilisateur son choix
3. **Utilise une boucle `while`** pour forcer l'utilisateur à entrer 1, 2 ou 3
4. En fonction du choix, demande 2 nombres et affiche le résultat
5. Propose de refaire un calcul ou quitter

*Notions : while, input, conditions, boucles, fonctions*

---

**Exercice 5 — Moyenne de notes**

Crée une fonction `calculer_moyenne(notes)` qui :
- Prend une liste de notes
- Utilise une boucle `for` pour les additionner
- Retourne la moyenne
- Affiche "Admis" si moyenne ≥ 10, sinon "Recalé"

*Notions : listes, boucles for, fonctions, conditions*

---

## Exercices Partie 3 — Web Scraping

**Exercice 6 — Scraper simple**

À partir de `https://books.toscrape.com` :

1. Récupère le titre de la page avec `requests` + `BeautifulSoup`
2. Extrait les titres de **tous les livres** de la première page
3. Crée une liste de dictionnaires avec : titre, prix
4. Sauvegarde dans un fichier CSV

*Notions : requests, BeautifulSoup, CSV, ETL*

---

**Exercice 7 — ETL complet (Transform + Load)**

En utilisant les livres du site précédent :

1. **Extract** — récupère titre et prix
2. **Transform** — convertis le prix (£ en €) avec taux 1.2
3. **Load** — sauvegarde dans CSV avec colonnes : titre, prix_original, prix_euro

*Notions : ETL complet, transformation de données, CSV*

---

**Plan de travail jusqu'au 2-3 juillet**

| Dates | À faire |
|---|---|
| **10-12 juin** | Exercices 1 + 2 |
| **13-15 juin** | Exercices 3 + 4 + 5 |
| **16-18 juin** | Exercices 6 + 7 |
| **19-21 juin** | Relire les quiz OpenClassrooms |
| **22-25 juin** | Révision des concepts clés |
| **26-2 juillet** | Refaire les 3 quiz complets |

---