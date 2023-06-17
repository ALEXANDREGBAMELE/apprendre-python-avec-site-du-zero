import os

annee = input('Entrer l\'annee : ')
annee = int(annee)
if annee % 4 == 0 or annee % 10 == 0:
    print('l\'annee saisir est bixetille')
else:
    print('l\'annee saisir n\'est pas bixetille')
os.system('pause')
