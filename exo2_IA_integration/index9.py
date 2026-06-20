'''
**Exercice 9 — Inverser une liste**

Crée une fonction `inverser_liste(liste)` qui :
- Prend une liste
- Retourne une nouvelle liste avec les éléments dans l'ordre inverse
- **Sans utiliser `.reverse()` ou slicing `[::-1]`**
- Utilise une boucle et une nouvelle liste

Teste avec :
```python
nombres = [1, 2, 3, 4, 5]  
print(inverser_liste(nombres))  # Doit afficher [5, 4, 3, 2, 1]
```

*Notions : boucles, listes, indices*
'''

def inverser_liste(liste):
  for y in range(len(nombres) -1, -1, -1): # reverse order of list number manually
    nombre_inverser.append(nombres[y]) # add numbers in the new list
  return nombre_inverser

nombres = [1, 2, 3, 4, 5]
nombre_inverser = [] 

# test
print(inverser_liste(nombre_inverser))