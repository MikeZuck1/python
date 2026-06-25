'''
**Exercice 12 — Fusionner deux listes**

Crée une fonction `fusionner_listes(liste1, liste2)` qui :
- Prend deux listes
- Retourne une nouvelle liste contenant tous les éléments des deux
- **Sans utiliser `+` ou `.extend()`**
- Utilise deux boucles `for`

Teste avec :
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(fusionner_listes(list1, list2))  # Doit afficher [1, 2, 3, 4, 5, 6]
```
'''

def fusionner_listes(liste1, liste2):
  # empty list
  new_list = []
  
  for first in liste1: # first loop to check the first list
    new_list.append(first)
  for second in liste2:
    new_list.append(second)
  return new_list
    
# lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Test
print(fusionner_listes(list1, list2))