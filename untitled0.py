

import random as r
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3

def montecarlo(a, b, h, f, n = 1024):
    X, Y = [], []
    np = 0
    for i in range(n):
        x = r.uniform(a, b)
        y = r.uniform(0, h)
        if y <= f(x):
            X.append(x)
            Y.append(y)
            np += 1
    return X, Y, (np/n)* (b-a) * h

X = np.linspace(-10, 10, 1000)
Y = [f(x) for x in X]
plt.plot(X, Y)

Xm, Ym, aire  = montecarlo(1, 7, 300, f)

plt.plot(Xm, Ym, "r.")

axes = plt.gca()

axes.spines["top"].set_position("zero")
axes.spines["bottom"].set_position("zero")
axes.spines["left"].set_position("zero")
axes.spines["right"].set_position("zero")
plt.show()


def fp(f, x):
    h= 0.01
    return (f(x + h) - f(x - x))/h

def pm(f, a, b):
    return (b-a)* f((a + b)/2)

def tz(f, a, b):
    return (b-a) * (f(a) + f(b))/2

def revs(a, b, f, n =1024):
    dx = (b-a)/n
    v = 0
    for i in range(n):
        x1 = a+ i*dx
        x2 = x1 + dx
        m = (x1+ x2)/2
        v += f(x1)**2 + 4*f(m)**2 + f(x2)**2
        
    return np.pi * v / 6

def lon(a, b, n, f):
    dx = (b-a)/n
    l = 0
    for i in range(n):
        x1 = a + dx*i
        x2 = x1 +dx
        m = (x1+x2)/2
        l+= (1 + fp(x1)**2)**(1/2) + 4(1 + fp(m)**2)**(1/2)
    return l * dx / 6