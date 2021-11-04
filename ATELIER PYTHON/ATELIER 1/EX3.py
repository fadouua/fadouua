#Atelier 1:
 #Exercice 3:
#fonction récursive pour calculer la somme des nombres de 1 à n 
#Definir la founction
def Somme(N):
    if N == 0:
        return 0
    else:
        return N+Somme(N-1)
#entrer les valeurs par l'utilisateurs
n = int(input("Entrez un nombre :  "))
#appeler la fonction
print("La somme est :  ",Somme(n))
