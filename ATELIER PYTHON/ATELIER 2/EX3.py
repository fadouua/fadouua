#Atelier 2
#exercice 3
#faire entrer la liste
Liste=[2,8,4,48,2,1,3,3,1,7,23,99,34]
#declare le dictionnaire
Dic={}

for i in range(len(Liste)):
    S = 0# on a declaré le variable 'S' pour compter combien de fois l'element a été répétées
    for j in range(len(Liste)):#la boucle 'for' va exporter les éléments pour trouver est ce qu'il y a un élément égale à un autre
        if Liste[j] == Liste[i]:
            S += 1
            #le compteur 'a' va être ajouté par 1 lorsqu'il trouve 2 éléments égaux, et ainsi de suite
    Dic[Liste[i]]= S#ici va être stocker l'élément avec nombre de fois trouvés répétées dans la liste, dans le dictionnaire , la boucle va être répétée jusqu'à la fin de la liste
#affichage de dictionaire
print(Dic)