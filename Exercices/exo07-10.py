# Exercice 07 : Créez une liste contenant les jours de la semaine.
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

# Exercice 08 : Comment accédez-vous à l'élément "Mercredi" dans la liste créée?
print(jours[2]) # Étant donné que l'index commence à 0, Mercredi est à l'index 2

# Exercice 09 : Ajoutez "Dimanche" comme premier élément de cette liste.
jours.insert(0, "Dimanche") # Ajoute Dimanche à l'index 0
print(jours) # Affiche la liste des jours de la semaine avec Dimanche en premier
print(jours[0]) # Affiche Dimanche

# Exercice 10 : Supprimez "Lundi" de la liste des jours de la semaine.
jours.remove("Lundi") # Supprime Lundi de la liste
print(jours) # Affiche la liste des jours de la semaine sans Lundi
