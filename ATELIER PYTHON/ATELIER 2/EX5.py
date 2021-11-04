#Atelier 2
#exercice 5
L=[1,4,7,4,3,7,9] #La liste
L1=[] # La nouvelle liste pour stocker les elements existant dans le dictionaire
DIC={"FADOUA":5 , "KARIMA":4 , "MANAL":8 , "NADA":7} # entrer les elements du dictionaire

for val in L: #Boucle for pour se passe dans la liste
        if val in DIC.values():
            L1.append(val) #Remplier les elements de le liste
    

print(L1) #Afficher la resultat de la liste


