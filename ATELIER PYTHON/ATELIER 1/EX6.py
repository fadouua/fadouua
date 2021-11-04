#selection 
#definir le tri selection
def selection(tab):
    for i in range(len(tab)):#la fonction len() renvoie le nombre des éléments (ou la longueur) de l'element

        min = i

        for j in range(i + 1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp

    return tab
#entrer les elements du tableau
tab = [97, 24, 16, 33, 2, 75, 62, 70]
#appeler le tri
selection(tab)
#appeler le tableau
print("Le tableau trié est:")
for i in range(len(tab)):
    print("%d" % tab[i])    
    
#bulle
#definir le tri bulle
def bulle(tab):
    n = len(tab)# len() renvoie le nombre des éléments (ou la longueur) dans l'element

    for i in range(n):
        for j in range(0, n - i - 1):

            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]

#faire entrer les elements du tableau
tab = [97, 24, 16, 33, 2, 75, 62, 70]
#faire appeler le tri bulle
bulle(tab)

print("Le tableau trié est:")
for i in range(len(tab)):
    print("%d" % tab[i])
    
#insertion
def insertion(tab):

    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k

#faire entrer les elements du tableau
tab = [97, 24, 16, 33, 2, 75, 62, 70]
insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("% d" % tab[i])
