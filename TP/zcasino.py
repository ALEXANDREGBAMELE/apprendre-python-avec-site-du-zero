# importation des modules
import os
from random import randrange
from math import ceil

# Declaration des variables
argent = 1000 # On a 1000 $ pour commencer
continuer_partie = True # Tantque continuer_partie est true le jeux continue

print("Vous vous installez à la table de roulette avec", argent,
"$.")

while continuer_partie :
    nombre_de_mise = -1
    '''Tant que nombre de mise est compris entre 0 et 49
     on peux toujour miser'''
    while nombre_de_mise <0 or nombre_de_mise >49:
        nombre_de_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
        # On convertit le nombre misé
        try :
            nombre_de_mise = int(nombre_de_mise)
        except ValueError :
            print('Vous devez saisir un nombre')
            nombre_de_mise = -1
            continue
        if nombre_de_mise < 0:
            print ('Le nombre est negatif')
        if nombre_de_mise > 49:
            print('Le nombre est superieur a 49')
    # À présent, on sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        # On convertit la mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")
            
        # Le nombre misé et la mise ont été sélectionnés par
    # l'utilisateur, on fait tourner la roulette
    numero_gagnant = randrange(50)
    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)
    
    # Le nombre misé et la mise ont été sélectionnés par
    # l'utilisateur, on fait tourner la roulette
    # On établit le gain du joueur
    if numero_gagnant == nombre_de_mise:
        print("Félicitations ! Vous obtenez", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_de_mise % 2: # ils sont de la même couleur
        mise = ceil(mise * 0.5)
        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
        argent += mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= mise
    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
    # On affiche l'argent du joueur
        print("Vous avez à présent", argent, "$")
    quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
    if quitter == "o" or quitter == "O":
        print("Vous quittez le casino avec vos gains.")
        continuer_partie = False
# On met en pause le système (Windows)
os.system("pause")

                    
                    