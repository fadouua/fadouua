#ATELIER 1
#exercice 9:

#fonction qui cherche un élément dans une matrice puis renvoi sa position « i,j ».
def Position(M,x):
    for i in range(len(M)):#On va chercher dans le matrice jusqu'a la Taille de matrice
        for j in range(len(M[0])):# On va chercher dans chaque ligne de Matrice
            if x==M[i][j]:
                Indexi=i
                Indexj=j
                return Indexi,Indexj
        
#Fonction principale 

M = [ [0, 11, 5], [9, 18, -1], [20, 2, 2] ]
x=int(input("Entrez l'élément de recherche : ")) # Demande à l'utilisateur d'entrer un nombre.

a = Position(M,x)

print("la position (i,j) de  ",x,"dans la matrice est ",a) # affichage de la resultat 