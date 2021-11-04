#Atelier 1:
  #Exercice 1:
# Python fonction pour trouver la somme des series 1! / 1+ 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 
#Definir la fonction factoriel
def Fact(N):
    
    if N==1:
         return N
    #determiner la factoriel par la recursivite
    return N * Fact(N - 1)
#Definir la fonction main
def determinate(c):
    #Declaration of the accumaltor variable (final result) 
    resultat = 0
    # Declaration of the main loop that reduce to last 
    for i in range(1, c + 1):
        resultat = (Fact(i)/i) + resultat
    #la resultat final
    return resultat
#affichage de la resultat final
print(determinate(int(input("entrez les elements: \n"))))



