'''
  this function return True or False
  if a value is in the list. The loop
  allows to iterate in the list to find 
  the a value and then the if condition
  access to list to find if the value is 
  inside or not.
'''
def recherche(liste, valeur):
  for i in range(len(liste)):
    if liste[i] == valeur: 
      return True
  return False

# Test
arr = ["chat", "chien", "lion"]
print(recherche(arr, "chat"))  
print(recherche(arr, "ours"))