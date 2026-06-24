'''
**Exercice 10 — Trouver le minimum et maximum**

Crée deux fonctions :
1. `trouver_min(liste)` — retourne le plus petit nombre
2. `trouver_max(liste)` — retourne le plus grand nombre

**Sans utiliser `min()` ou `max()`**

Teste avec :
```python
nombres = [15, 3, 42, 8, 99, 1]
print(trouver_min(nombres))  # Doit afficher 1 
print(trouver_max(nombres))  # Doit afficher 99
```

*Notions : boucles, comparaisons, variables*
'''

# first function should return the minimum number in the list
def trouver_min(liste):
  minimum = liste[0] # start with the first element
  for nombre in liste:
    if nombre < minimum: # Comparison
      minimum = nombre # keep the number
  return minimum

# seconde function should return the maximum number in the list
def trouver_max(liste):
  maximum = liste[0]
  for nombre in liste:
    if nombre > maximum:
      maximum = nombre
  return maximum

#list
nombres = [15, 3, 42, 8, 99, 1]

# Test
print(trouver_min(nombres))
print(trouver_max(nombres))