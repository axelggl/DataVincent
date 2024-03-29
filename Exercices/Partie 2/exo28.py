#  Écrivez une fonction qui prend deux chaînes de caractères et retourne une fusion de ces deux chaînes, séparées par un espace.

def concatener_chaines(chaine1, chaine2):
    return chaine1 + " " + chaine2

# Tests
print(concatener_chaines("Bonjour", "Vincent")) # Bonjour Vincent
print(concatener_chaines("Quoi?", "Feur.")) # Quoi? Feur.