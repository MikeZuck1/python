customers = [
  {"nom": "Alice", "age": 30, "ville": "Bruxelles"},
  {"nom": "Bob", "age": 25, "ville": "Anvers"},
  {"nom": "Charlie", "age": 35, "ville": "Liège"},
  {"nom": "David", "age": 28, "ville": "Bruxelles"},
  {"nom": "Eve", "age": 22, "ville": "Namur"}
]

def print_customers():
  '''
    Cette fonction parcourt la liste des clients et affiche le nom de ceux qui habitent à Bruxelles.
  '''
  for customer in customers: 
    if customer["ville"] == "Bruxelles":
      print(f"{customer['nom']} habite à Bruxelles.") 
print_customers()
