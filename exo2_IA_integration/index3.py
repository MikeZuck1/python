'''
Crée une fonction `calculer(num1, num2, operation)` qui :
- Prend 2 nombres et une opération (+, -, *, /)
- Retourne le résultat
- Gère le cas division par zéro avec `if/else`

Teste la fonction avec au moins 4 opérations différentes.

*Notions : fonctions, paramètres, conditions, division par zéro*
'''

def calculer(num1, num2, operation):
  # if/else
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "/":
    if num2 == 0:
      print("Error: divided by 0")
      return None
    return num1 / num2
  elif operation == "*":
    return num1 * num2
  else:
    return None

# Test
print(calculer(10, 20, "+"))
print(calculer(10, 20, "-"))
print(calculer(10, 0, "/"))
print(calculer(10, 20, "*"))

# Example about how to think before going to the next step.
def calculer(num1, num2, operation):
    pass