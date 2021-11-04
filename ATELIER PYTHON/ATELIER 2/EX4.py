#Atelier 2
#Exercice 4
#in va declare deux set
Set1 = {1,2,3,4,5,6,7,8,9,100}
Set2 = {0,11,3,9,544,3,8}
#l'intersection
Set3 = Set1.intersection(Set2)#cette Set3 est le résultat de l'intersection de la Set1 avec Set2 par l'utilisation de l'operation : Set1.intersection(Set2) 
print(Set3)#on va afficher set3
#la difference
print(Set1.difference(Set3))#on a utilisé l'opération suivante : Set1.difference(Set2) pour supprimer les éléments communs entre la Set1 et Set2 de la Set1 