import requests
from bs4 import BeautifulSoup
import csv

url = 'https://books.toscrape.com'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Extraire les titres dans une liste
titres = []
for title in soup.find_all('h3'):
    titres.append(title.get_text())

# Sauvegarder dans un CSV
with open('livres.csv', mode='r', newline='') as fichier:
    writer = csv.writer(fichier)
    writer.writerow(['titre'])  # en-tête
    for titre in titres:
         writer.writerow([titre])

print(f"{len(titres)} livres sauvegardés dans livres.csv ✅")