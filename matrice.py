class Matrice:
    def __init__(self, liste):
        self.lignes = len(liste)#nombre de lignes
        self.colonnes = len(liste[0])#nombre de colonnes
        self.pack = liste
        
    def __str__(self):
        mat = ""
        for i in range(self.lignes):
            mat += f"({str(self.pack[i])})\n"
            mat = mat.replace("[", "")
            mat = mat.replace("]", "")
        return mat
    
    def __add__(self, other):
        if self.lignes != other.lignes or self.colonnes != other.colonnes:
            return "impossible de faire l'addition"
        else:
            new_matrice = []
            ligne_matrice = []
            for i in range(self.lignes):
                for ii in range(self.colonnes):
                    x = self.pack[i][ii] + other.pack[i][ii]
                    ligne_matrice.append(x)
                new_matrice.append(ligne_matrice)
                ligne_matrice = []
        matrix = Matrice(new_matrice)
        
        return matrix.__str__()



L = [[0, 1], [0, 1]]
L2 = [[3, 1], [4, 1]]
B = Matrice(L2)
A = Matrice(L)
print(A+B)