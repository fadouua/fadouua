class Etudiant:
    """defintion du class"""
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne


# la liste d'etudiant
studentsList = [ Etudiant("lkhamal", "Fadoua", 21, "P1234567", 12),
             Etudiant("koko", "Hind", 20, "P1308883", 13),
             Etudiant(" mugiwara", "luffy", 22, "P1338764", 6.5),
             Etudiant("potegas", "Ace", 21, "P13022878", 8),
             Etudiant("lunni", "Nami", 23, "P13096373", 11.5)]

# triage selon l'age 
def sortByAge(student):
    return student.age

studentsList.sort(key=sortByAge)

for student in studentsList:
    print(".........")
    print(student.nom)
    print(student.prenom)
    print(student.age)
print(".....end of list.........")

# triage selon la moyenne
def sortByAverage(student):
    return student.moyenne

studentsList.sort(key=sortByAverage)

for student in studentsList:
    print("...........")
    print(student.nom)
    print(student.prenom)
    print(student.moyenne)

print("......end of list.........")