lettres = "Bonjour les zeros"
voielle = ['a','e','u','i','o','u','y','A','E','U','I','O','U','Y']

for lettre in lettres :
    if lettre in voielle:
        print('*')
    else :
        print(lettre)

# exercice sur le break
while 1:
    reponse = input('Entrer \'Q\' pour quiter  la boucle : ')
    if reponse == 'Q':
        print('Fin de la boucle')
        break
