# Écrivez une fonction qui vérifie si un nombre est pair ou impair.

def even_or_odd(number):
    if number % 2 == 0:
        return "pair"
    else:
        return "impair"
    
# Tests
print(even_or_odd(2)) # pair
print(even_or_odd(3)) # impair