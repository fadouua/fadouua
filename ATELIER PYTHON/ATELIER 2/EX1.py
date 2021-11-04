#Atelier 2
 #Exercice 1
#Entrer les listes
Liste1=[3,8,7,4,8,4,8]#faire entrer la 1ere liste
Liste2=[44,7,26,13,5,7,8]#faire entrer la 2eme liste
Liste3=[]# on a declaré une 3ème liste pour stocker les éléments qu'on va les exporter depuis les deux listes 
for i in range(1,len(Liste1),2):#on a utilisé la boucle 'for' qui va commencer depuis l'indice 1 jusqu'à la fin de la première liste avec deux pas pour qu'il va prendre seulement les éléments avec l'indice impair.Aussi la fonction len() renvoie le nombre des éléments (ou la longueur) de la liste1
    Liste3.append(Liste1[i])#append() ajoute les éléments dans une liste mais conserve la forme d'itérable.Donc #on a utilisé la boucle 'append' pour lorsqu'il trouve un élément avec indice impair il va le stocker dans la 3ème liste
for i in range(0,len(Liste2),2):#on a utilisé une autre boucle 'for' pour les éléments avec indices pairs(la boucle va commencer depuis l'indice 0 cette fois)
    Liste3.append(Liste2[i])##on a utilisé la boucle 'append' pour lorsqu'il trouve un élément avec indice impair il va le stocker dans la 3ème liste
#afficher la 3eme liste
print(Liste3)#on va afficher la liste qui contient les éléments avec indices impairs de la 1ère liste , et les éléments avec indices pairs de la 2ème 