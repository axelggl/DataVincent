# Créez un petit programme qui:
# - Demande à l'utilisateur d'entrer son nom, son âge, et sa ville de résidence.
# - Stocke ces informations dans un dictionnaire.
# - Affiche un message personnalisé qui utilise ces informations, par exemple: "Bonjour [nom],
# vous avez [âge] ans et vous vivez à [ville]."
# - Ajoutez une fonction dans ce programme qui calcule l'année de naissance de l'utilisateur à
# partir de son âge et affiche un message "Vous êtes né(e) en [année].". Prenez en compte
# que l'année actuelle est obtenue dynamiquement via le module `datetime`.

import datetime

def annee_naissance(age):
    annee_actuelle = datetime.datetime.now().year
    return annee_actuelle - age

infos = {
    "nom": input("Entrez votre nom: "),
    "age": int(input("Entrez votre âge: ")),
    "ville": input("Entrez votre ville de résidence: ")
}

print(f"Bonjour {infos['nom']}, vous avez {infos['age']} ans et vous vivez à {infos['ville']}.")
print(f"Vous êtes né(e) en {annee_naissance(infos['age'])} ou en {annee_naissance(infos['age']) - 1}")
