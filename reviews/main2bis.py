list_name = ["Alice", "Bob", "Charlie", "David", "Eve"]

#2 façons d'afficher le nom et sa position dans la liste
for index, name in enumerate(list_name, start=1):
    print(index, name)