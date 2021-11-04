#Atelier 2
#Exercice 2
#Deviser la liste en 3 morceaux egaux et inverser chaque morceau
Liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#on va crée 3 listes pour stocker les éléments de la liste
Liste1=[]
Liste2=[]
Liste3=[]
#la division de la liste
a=int(len(Liste)/3)#on prend un variable 'a' qui égale un tiers de la longueur de Liste pour qu'on peut diviser la liste en trois listes (on a declaré a de type 'int' pour que a soit un nombre naturel).La fonction len() renvoie le nombre des éléments (ou la longueur) de la liste

for i in range(a):#on utilise la boucle 'for' pour commencer à prendre les éléments de liste commençant avec le 1er élément(indice 0) jusqu'à l'élément qui a l'indice un tiers (1/3) de la longueur (a)(dans ce cas depuis l'indice 0 jusqu'à l'indice : a = 9/3 =3)
    Liste1.append(Liste[i])#la fonction 'append' va commencer à ajouter les éléments du 1er tiers de la List dans Liste1
for i in range(a,a*2):#va commencer depuis P jusqu'à a*2(le 2ème tiers de List)
    Liste2.append(Liste[i])#la fonction 'append' va commencer à ajouter les éléments du 2ème tiers de Liste dans Liste2
for i in range(a*2,a*3+len(Liste)%3):#ici la boucle 'for' va prendre le reste des éléments de Liste (les éléments du 3ème tiers + le reste si le longueur n'est pas divisible sur 3 (len(List)%3))
    Liste3.append(Liste[i])#la fonction 'append' va commencer à ajouter le reste de Liste dans Liste3
#inverser les listes
#après la division de Liste en trois listes : Liste1,Liste2 et Liste3 , on va les inverser avec l'opération '[::-1]'
print(Liste1[::-1])
print(Liste2[::-1])
print(Liste3[::-1])