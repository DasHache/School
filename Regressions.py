import matplotlib.pyplot as plt
import numpy as np

def reglin(X, Y):
    n = len(X)
    sxy, sx2 = 0, 0
    for i in range(n):
        sxy += X[i]*Y[i]
        sx2 += X[i]**2
    return sxy/sx2
    
    
def regaff(X, Y):
    n = len(X)
    sx, sy, sxy, sxx =0, 0, 0, 0
    for i in range(n):
        sx += X[i]
        sy += Y[i]
        sxy += X[i]*Y[i]
        sxx += X[i]**2
    mx, my = sx/n, sy/n
    a = (sxy - n*mx*my)/(sxx-n*mx**2)
    b = my - a*mx
    return a, b
    

def regmono(X, Y):
    n = len(X)
    Xn = [np.log(x) for x in X]
    Yn = [np.log(y) for y in Y]
    sx, sy, sxy, sxx =0, 0, 0, 0
    for i in range(n):
        sx += Xn[i]
        sy += Yn[i]
        sxy += Xn[i]*Yn[i]
        sxx += Xn[i]**2
    mx, my = sx/n, sy/n
    a = (sxy - n*mx*my)/(sxx-n*mx**2)
    b = my - a*mx
    return a, np.exp(b)
    
    
    
def regexp(X, Y):
    n = len(X)
    Yn = [np.log(y) for y in Y]
    sx, sy, sxy, sxx =0, 0, 0, 0
    for i in range(n):
        sx += X[i]
        sy += Yn[i]
        sxy += X[i]*Yn[i]
        sxx += X[i]**2
    mx, my = sx/n, sy/n
    a = (sxy - n*mx*my)/(sxx-n*mx**2)
    b = my - a*mx
    return np.exp(a), np.exp(b)

X = [2, 4, 6, 8, 10, 12, 14, 16, 18]
Y = [855, 618, 422, 282, 189, 138, 84, 56, 37]

plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(X, Y)
plt.title("linéaire")

plt.subplot(3, 1, 2)
plt.loglog(X, Y)
plt.title("mono")

plt.subplot(3, 1, 3)
plt.semilogy(X, Y)
plt.title("exponentielle")


plt.figure(2)

a, b = regaff(X, Y)
c, d = regmono(X, Y)
e, f = regexp(X, Y)

Z = np.linspace(2, 18, 10)
A = [a * x + b for x in Z]
B = [d*x**c for x in Z]
C = [f*e**x for x in Z]

plt.plot(X, Y, "b", label="fonction")
plt.plot(Z, A, ".r", label="affine")
plt.plot(Z, B, ".g", label="monomiale")
plt.plot(Z, C, ".y", label="exp")

