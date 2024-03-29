# Créez une liste de nombres, puis filtrez pour n'afficher que les nombres pairs

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nombre in nombres:
    if nombre % 2 == 0: # Modulo 2 permet de vérifier si le nombre est pair
        print(nombre)