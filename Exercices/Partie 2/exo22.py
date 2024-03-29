# Utilisez une condition pour afficher "C'est le week-end" si le jour est "Samedi" ou "Dimanche".

jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for jour in jours:
    print(jour)
    if jour == "Samedi" or jour == "Dimanche":
        print("C'est le week-end") # Affiche "C'est le week-end" si le jour est Samedi ou Dimanche