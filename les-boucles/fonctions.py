def add( a, b):
    return a + b

print('La valeur de et de b vaut :', add(7,39))
resultats = {}
def table_multiplication(nombre):
    for coeficient in range(0,11):
        result = nombre * coeficient
    return result

print(table_multiplication(10))

# les fonctions lamda
carree =  lambda x : x*x
r =carree(5)
print(r)

# les modules de maths
import math
racine_carre_de_100 = math.sqrt(100)
print('la racine carre de 100 absolue de -5 est : ',racine_carre_de_100)

valeur_absolue = abs(-5)
print('la valeur absolue de -5 est : ', valeur_absolue)