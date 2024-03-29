# Exercice 14 : Divisez la chaîne de caractères "Bonjour, je suis un étudiant en informatique" en une liste de mots.

texte = "Bonjour, je suis un étudiant en informatique"
mots_liste = texte.split(" ") # Divise la chaîne de caractères en une liste de mots
print(mots_liste) # Affiche la liste de mots

# Exercice 15 : Inversez l'ordre des mots dans la phrase précédente.
mots_liste.reverse() # Inverse l'ordre des mots dans la liste
print(" ".join(mots_liste)) # Affiche la phrase avec les mots inversés