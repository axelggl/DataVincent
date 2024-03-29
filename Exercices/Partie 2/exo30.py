# Utilisez une boucle `for` pour afficher le titre et l'auteur de chaque livre dans le dictionnaire

livres = {
    "Livre 1": "John Doe",
    "Livre 2": "Jean Dupont",
    "Livre 3": "Frédéric-Jacques de la Rivière"
}

for livre, auteur in livres.items():
    print(livre, auteur) # Affiche le titre et l'auteur de chaque livre dans le dictionnaire