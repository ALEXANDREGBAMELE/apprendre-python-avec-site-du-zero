annee = input("entrer une annee superieur a zero : ")
try:
    annee = int(annee)
    if annee <= 0:
        raise ValueError ("annee saisir est invalide")
    # assert annee > 0
except ValueError:
    print("vous n'avez pas saiair un un nombre ")
except AssertionError:
    print("vous n'avez pas saiair une annee superieur a zero")
    
    