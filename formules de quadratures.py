import numpy as np

def fp(x, f):
    h = 0.01
    return (f(x+h) - f(x-h))/h
    
def PM(a, b, f):
    return f((a + b)/2)(b - a)

def Trap_ez(a, b, f):
    return (b - a)*(f(a) + f(b))/2

def Simpson(a, b, f):
    return (b-a) * (f(a) + f((b+a)/2) + f(b))/6

"""
    Subdiviser l'intervalle
    dx = (b - a) / n
    v = 0
    
    Appliquer la FQ de Simpson
    for i in range(n):
        x1 = a + i*dx
        x2 = x1 + dx
        milieu = (x1 + x2) / 2
        v += f(x1)**2 + 4*f(milieu)**2 + f(x2)**2 
    
    #Resultat final
    return np.pi * v * dx / 6
"""


def longueur(a, b, f, n=1024):
    #Subdiviser l'intervalle
    dx = (b - a) / n
    l = 0
    
    #Appliquer la FQ de Simpson
    for i in range(n):
        xg = a + i*dx
        xd = xg + dx
        milieu = (xg + xd) / 2
        l += np.sqrt(1 + fp(xg)**2) + 4*np.sqrt(1 + fp(milieu)**2) + np.sqrt(1 + fp(xd)**2)
    
    #Resultat final
    return l * dx / 6
 