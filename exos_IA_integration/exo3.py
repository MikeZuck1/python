import random

'''
  Calcule la moyenne en divisant la somme des éléments 
  par le nombre d'éléments Génère une liste de 10 nombres 
  aléatoires entre 1 et 100
'''
test = [random.randint(1, 100) for _ in range(10)] 
average = sum(test) / len(test)

print("Test:", test)
print("Average:", average)