#Atelier 1:
  #Exercice 5:
#fonction récursive pour compter les chiffres d'un nombre donné
#definir la fonction
def Compter(N):
    if N == 0:
        return 0

    return 1+Compter(N//10)
#entrer les valeurs par l'utilisateurs
n = int(input("Entrez le nombre : "))
#appeler la fonction
print("Le nombre de chiffre est : ",Compter(n))
