#Atelier1
 #Exercice2
#fonction pour convertir le nombre decimal en nombre binaire
#definir la fonction

def binaire(N):
    d = 1
    S = 0
    while(N != 0):
        F = N%2
        S += F*d
        d *= 10
        N //= 2
        
    return S

#Entrer les valeurs par l'utilisateur
n=int(input("Entrez un nombre :  "))
#appeler la fonction
print("Le nombre binaire est : ",binaire(n))

       
        


