import numpy as np
import matplotlib.pyplot as plt

class Quadrilatère:
    
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        
    def __repr__(self):
        return f"le quadrilatère à les coordonnées {self.c1}, {self.c2}, {self.c3}, {self.c4}"
    
    def mag(self, coté):
        m = []
        if coté == "l1":
            for i in range(2):
                m.append(self.c2[i]-self.c1[i])
                
        return f"m = {m}"
    
A = Quadrilatère([1, 2], [1, 4], [3, 4], [3, 2])

print(A.mag("l1"))