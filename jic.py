# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:45:03 2022

@author: dasha
"""

class Resistor:
    
    def __init__(self, resistance):
        self.r = resistance
    
    def __repr__(self):
        return f" generator with {self.p} V as output"
        
    def find_current(self, potential):
        return potential / self.r
    
    def find_potential(self, current):
        return current * self.r
    
    def resistance_serie(self, other):
        NR = Resistor(self.r + other.r)
        return NR
    
    def resistance_parallele(self, other):
        if self.r != 0 and other.r != 0:
            newresistance = 1 / (1/self.r + 1/other.r)    
        
        elif self.r == 0 and other.r == 0:
            return "no resistance, be careful maybe you have an error", 0
        
        elif self.r == 0:
            newresistance = other.r
            
        else:
            newresistance = self.r
        
        RN = Resistor(newresistance)
        return RN
    

import resistor as res
import generator as ge

def creation_circuit():
    Intensité = 0
    Valeures = ["Ug", "courant"]
    Resistances = []
    longueur = len(Valeures) 
    ii = 0
    R = 0
    
    reponse = input("avez vous plusieurs resistances ? 'no' or 'number'")
    
    if reponse != "no":
        for i in range(int(reponse)):
             R = res.Resistor(float(input("valeur de la resistance, x if unknown")))
             Resistances.append(R)      
        if input("sont elles en 'parallele' ou en 'serie'") == "parallele":
            resistance_equivalente = Resistances[0].resistance_parallele(Resistances[1])
            R = resistance_equivalente
        else:
            resistance_equivalente = Resistances[0].resistance_serie(Resistances[1])
            R = resistance_equivalente
    else:
        R = res.Resistor(float(input("la resistance de votre resistance ?")))  
        
    

    if input("vous cherchez la 'resistance_equivalente' ou une 'valeur'") == "valeur":
        for i in range(longueur):    
            a = input(f"connaissez vous le/la {Valeures[i]} du circuit ? 'value' or 'no'")
            if a != "no":
                if i == 0:
                    G = ge.Generator(float(a))
                if i == 1:
                    Intensité = float(a)
            else:
                ii = i
        
        if Valeures[ii] == "courant":
            Intensité = R.find_current(G.ret_potentiel())
            return Intensité
        if Valeures[ii] == "potentiel":
            Ug = R.find_potential(Intensité) 
            return Ug
        if Valeures[ii] == "resistance":
            R = G.find_resistance(Intensité)
            return R
    else:
        return R
        
print(creation_circuit())

class Generator:
    def __init__(self, potentiel):
        self.p = potentiel
        
    def __repr__(self):
        return f" generator with {self.p} V as output"
    
    def find_resistance(self, current):
        return self.p /current
    
    def ret_potentiel(self):
        return self.p
    
