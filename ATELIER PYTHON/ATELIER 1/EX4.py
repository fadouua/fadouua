#Atelier 1:
 #Exercice 4:
#fonction récursive pour imprimer la série Fibonacci
#definir la fonction
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
#Entrer la valeur par l'utilisateur
n = int(input("Entrez le nombre de termes:"))

for i in range(n):
    print(fibonacci(i))