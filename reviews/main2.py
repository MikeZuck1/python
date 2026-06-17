list_name = ["Alice", "Bob", "Charlie", "David", "Eve"]

#2 façons d'afficher le nom et sa position dans la liste
for name in list_name:
    print(list_name.index(name) + 1, name)