import matplotlib.pyplot as plt

def Lotvol(x0, y0, a, b, j, d, h = 0.01, g = 100000):
    Y,X = [x0], [y0]
    
    for i in range(g):
        x = X[i] + h * (a*X[i]-b*X[i]*Y[i])
        y = Y[i] + h * (j*Y[i]*X[i]-d*Y[i])
        X.append(x if x > 0 else 0)
        Y.append(y if y > 0 else 0)
        
    T = [t for t in range(g+1)]
    plt.subplot(2, 1, 1)
    plt.plot(T, X, "--b", label="proies")
    plt.plot(T, Y, "r", label="prédateurs")
    plt.legend()
    
    axes = plt.gca()
    axes.spines["right"].set_visible(False)
    axes.spines["top"].set_visible(False)
    axes.spines["left"].set_position("zero")
    axes.spines["bottom"].set_position("zero") 
    
    plt.subplot(2, 1, 2)
    plt.plot(X, Y, "y", label="prédateurs en fonctions des proies")
    plt.xlabel("proies")
    plt.ylabel("prédateurs")
    plt.legend()
    
    axes = plt.gca()
    axes.spines["right"].set_visible(False)
    axes.spines["top"].set_visible(False)
    axes.spines["left"].set_position("zero")
    axes.spines["bottom"].set_position("zero") 
        
    return X, Y


#call Lotvol
X1, Y1 = Lotvol(1000, 300, 0.1, 0.001, 0.0001, 0.1)
plt.legend()
plt.title("bruh")
