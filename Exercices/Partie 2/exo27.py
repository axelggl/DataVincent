# . Écrivez une fonction qui prend une liste de nombres et retourne leur moyenne

def moyenne(liste):
    return sum(liste) / len(liste) # Une moyenne est la somme des éléments d'une liste divisée par le nombre d'éléments de la liste

# Tests
print(moyenne([1, 2, 3])) # 2.0
print(moyenne([8, 12, 11.5, 14])) # 11.375