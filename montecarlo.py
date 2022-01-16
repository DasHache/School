#Les modules
import random as r
import numpy as np
import matplotlib.pyplot as plt

#Définir la fonction
def f(x):
    return x**2

#La méthode de Monte-Carlo
def montecarlo(a, b, hmax, f, n=100000):
    nbpts = 0
    X, Y = [], []
    
    for i in range(n):
        x = r.uniform(a, b)
        y = r.uniform(0, hmax)
        if y <= f(x):
            nbpts += 1
            X.append(x)
            Y.append(y)
    
    return nbpts/n * (b-a) * hmax, X, Y

#Représentation graphique
a, b, hmax = -10, 10, 100

aire, pointsX, pointsY = montecarlo(a, b, hmax, f)

X = np.linspace(a, b, 100)
Y = [f(x) for x in X]
plt.plot(X, Y, label="fonction f")
plt.plot(pointsX, pointsY, "r.", label="points")

#Gestion des axes
axes = plt.gca()
axes.spines["top"].set_visible(False)
axes.spines["right"].set_visible(False)
axes.spines["bottom"].set_position("zero")
axes.spines["left"].set_position("zero")

#Gestion des titres et des labels
plt.legend()
plt.xlabel("abscisses")
plt.ylabel("ordonnées")
plt.title(f"aire = {aire}")

