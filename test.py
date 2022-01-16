import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

X = np.linspace(-10, 10, 1000)
Y = [f(x) for x in X ]
plt.subplot(2, 1, 1)#the indication of the position is mandatory
plt.plot(X, Y, "r")

plt.subplot(2, 1, 2)
plt.plot(X, Y, "b.")
plt.show()