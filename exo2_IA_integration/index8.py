'''
**Exercice 8 — Compter les occurrences**

Crée une fonction `compter_occurrences(liste, valeur)` qui :
- Prend une liste et une valeur
- Parcourt la liste avec une boucle `for`
- Compte combien de fois la valeur apparaît
- Retourne le nombre
- **Sans utiliser `.count()`**

Teste avec :
```python
nombres = [1, 2, 3, 2, 4, 2, 5]
print(compter_occurrences(nombres, 2))  # Doit afficher 3
'''


def compter_occurrences(liste, valeur):
  # for loop
  total = 0 
  for nombre in nombres:
    if nombre == valeur:
      total += 1
  return total

# list
nombres = [1, 2, 3, 2, 4, 2, 5]

#Test  
print(compter_occurrences(nombres, 2))