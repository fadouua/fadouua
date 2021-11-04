#Atelier 1
#exercice8
#fonction Python pour trouver la fréquence d’un caractère dans une chaîne.
def fréquence(l,c) :
    comp=0
    for x in l :
        if x==c :
            comp += 1
    return comp    
#faire entrer la chaine de caractere par l'utilisateur
l=input(str("entez la chaine de caractere:"))
#faire entrer le caractere par l'utilisateur
caractere=input("tapez le caractère  ")
#appeler la fonction
print (fréquence(l,caractere))