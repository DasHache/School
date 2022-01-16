import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sqrt(1-x**2)

def g(x):
    return -(np.sqrt(1-x**2))

X = np.linspace(-1, 1, 10000)
Y = [f(x) for x in X]
Y1 = [g(x) for x in X]

plt.plot(X, Y, "b")
plt.plot(X, Y1, "b")

axes = plt.gca()

axes.spines["top"].set_visible(False)
axes.spines["left"].set_visible(False)
axes.spines["right"].set_position("zero")
axes.spines["bottom"].set_position("zero")

plt.show()