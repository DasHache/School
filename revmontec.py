import matplotlib.pyplot as plt
import random as r
import numpy as np

def m(a, b, f, h, n= 100000):
    X, Y, np = [], [], 0
    for i in range(n):
        x = r.uniform(a, b)
        y = r.uniform(0, h)
        if y <= f(x):
            X.append(x)
            Y.append(y)
            np+=1
    return (np/n)*(b-a)*h, Y, X

def f(x):
    return x**2

def fp(f, x):
    h = 0.01
    return (f(x+h)-f(x-h))/h

def rs(a, b, f, n =1024):#volume avec méthode simpson
    dx = (b-a)/n
    v = 0
    for i in range(n):
        x1= a+ i*dx
        x2= x1+dx
        m = (x1+x2)/2
        v += f(x1)**2 +4*f(m)**2 + f(x2)**2
    return v* dx *np.pi/6 

def revolution(a, b, f, n=1024):#volume avec méthode riemann
    dx = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a + dx * i)**2
    return s * dx * np.pi

print(rs(0, 10, f))
print(revolution(0, 10, f))


X = np.linspace(0, 10, 1000)
Y = [x**2 for x in X]
aire, Yp, Xp = m(0, 10, f, 100)

plt.plot(X, Y, "b", label="function")
plt.plot(Xp, Yp, "r.", label=f"montecarlo {aire}")
plt.title("bite")
plt.legend()
plt.show()