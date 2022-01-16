

class Fraction :
    
    def __init__(self, numerateur, denominateur):
        self.n = numerateur
        self.d = denominateur
        
    def __str__(self):
        if self.d == 1 or self.n == 0: 
            return f"{self.n}"
        else : 
            return f" {self.n} / {self.d}"
        
    def __repr__(self) : 
        """ représenter la fraction en str"""
        if self.d == 1 or self.n == 0: 
            return f"{self.n}"
        else : 
            return f"{self.n} / {self.d}"
    
    def simplifier(self) :
        """simplifier fractions"""
        m = min(self.n, self.d)
        for i in range(2, m+1): 
           while self.n % i == 0 and self.d%i == 0 : 
               self.n = self.n // i 
               self.d = self.d // i
        return self

    
    def __add__(self, other):
        """


        Parameters
        ----------
        other : Fraction
            DESCRIPTION.

        Returns
        -------
        somme : Fraction
        1. récupérer le num et dénum du self
        2. récupérer le num et dénum du other
        3. multiplier les dénominateurs
        4. modifier et additionner les numérateurs
        5. créer la  nouvelle fraction
        6, simplifier
        

        """
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        d3 = d1*d2
        n3 = n1*d2 + n2*d1
        
        somme = Fraction(n3, d3)
        somme.simplifier()
        return somme   
    
    
    def __mul__(self, other) :
        """
        

        Parameters
        ----------
        other : Fraction
            DESCRIPTION.

        Returns
        -------
        produit : Fraction
        
        1. récupérer le num et dénum du self
        2. récupérer le num et dénum du other
        3. multiplier les dénominateurs
        4. mutiplier les numérateurs
        5. créer la  nouvelle fraction
        6, simplifier
        

        """
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        
        d3 = d1*d2
        n3 = n1*n2
        
        produit = Fraction(n3, d3)
        produit.simplifier()
        
        return produit
    
    def fraction_continue(self):
        """
        transformer en fraction continue
        
        Returns
        ------
        fc : liste contenant les 
        """
        fc = []
        n, d = self.n, self.d
        while d > 0 :
            q, r = n//d, n%d
            fc.append(q)
            n = d
            d = r
            #n, d = d, r (n <-- d puis d <-- r)
        return print(fc) 
    
    
    
def calcul_fraction_continue(l):
    """
    

    Parameters
    ----------
    l : list
        fraction continue sous forme de liste)
    Attention : hors de la classe car on prend une liste 
    en paramètre MAIS utilise les objets Fraction
    

    Returns
    -------
    temp : Fraction
        1. inverser la liste
        2. initialisation avec la 1ere valeur
        3. boucle à partir de l[1]
        4. on inverse puis on additionne

    """
    l.reverse()
   #variable temporaire
    temp = Fraction(l[0], 1)
    for x in l[1:]: 
        temp= Fraction(x, 1) + Fraction(temp.d, temp.n)
        
    return temp
    
fraction = calcul_fraction_continue([2, 1, 2, 2])
print(fraction)
        

TEST = Fraction(40,28)
TEST.fraction_continue() 

TEST = Fraction(57,21)
TEST.fraction_continue()   
    
A = Fraction(1, 2)
A.simplifier()

B = Fraction(2, 1)
D = Fraction(6, 2)
print(B*D)
print(A+B)

C = A*B 
C.simplifier()
print(C)        
    