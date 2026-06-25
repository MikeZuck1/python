'''
**Exercice 13 — Tri simple (Bubble Sort)**

Crée une fonction `trier_liste(liste)` qui :
- Prend une liste de nombres
- Retourne une nouvelle liste triée du plus petit au plus grand
- **Sans utiliser `.sort()` ou `sorted()`**
- Utilise la méthode Bubble Sort (2 boucles imbriquées)

Teste avec :
```python
nombres = [5, 2, 8, 1, 9]
print(trier_liste(nombres))  # Doit afficher [1, 2, 5, 8, 9]
```

*Notions : boucles imbriquées, comparaisons, algorithmique*
'''

def trier_liste(liste):
  # empty list - will receive the sorted list
  # sorted_liste = [] 
  # for i in range(len(liste)):
  #   for y in range(len(liste)):
  #     if liste[i] < liste[y]:
  #       liste[y], liste[i] = liste[i], liste[y]
  # return liste
  
  n = len(liste)
  # iterate all elements in the liste
  for i in range(n):
    # to know if there is an exchange between elements
    swapped = False
  
    for j in range(0, n - i - 1):
      if liste[j] > liste[j + 1]:
        liste[j], liste[j + 1] = liste[j + 1], liste[j]
        swapped = True
    
    # if there is note exchange that mean the loop is finished
    if not swapped:
      break
    
  return liste
#list
nombres = [5, 2, 8, 1, 9]

# Test - sorted list
print(trier_liste(nombres))  # Doit afficher [1, 2, 5, 8, 9]