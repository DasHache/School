def der(x, dx, f):
    return (f(x + dx) - f(x-dx))/(2*dx)
    
    
def newton(x0, f, dx, n=20):
    for i in range(n):
        x0 = x0 - f(x0)/der(x0, dx, f)
    return x0


def f(x):
    return x + 2

print(newton(5, f, 0.01))