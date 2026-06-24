'''
**Exercice 11 — Valider une entrée utilisateur**

Crée un programme qui :
1. Demande à l'utilisateur d'entrer un nombre entre 1 et 10
2. **Utilise une boucle `while`** pour forcer une réponse valide
3. Si invalide → affiche "Entrée invalide, réessaie"
4. Une fois valide → affiche "Merci !"

Indice : Utilise `try/except` pour gérer si ce n'est pas un nombre, ou juste des conditions.

*Notions : while, input, conditions, validation*
'''

while True:
  user_input = input("Entrez un chiffre entre 1 & 10: ")
  try:
    value = int(user_input)
    if value <= 10 and value >= 1:
      print("Merci !")
      break
  except ValueError:
    print("Invalide")