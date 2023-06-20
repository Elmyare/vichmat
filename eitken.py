import numpy as np
from decimal import *
n = 4
x = []
y = []
z = 0
h = 1
for i in range(n):
    x.append(z + h)
    z += h
    #h = 0.5
    y.append(x[i]**0.5)
print(x,y)
    
x_interp = 2.56

def print2d(a):
    for c in a:
        for b in c:
            print("%.4f  " %(b), end="")
        print()

def aitken(x, y, x_interp):
    n = len(x)
    a = np.zeros((n,n))
    for i in range(n):
        a[i,0] = y[i]
    for j in range(1,n):
        for i in range(n-j):
            a[i,j] = ((x_interp - x[i+j]) * a[i][j-1] - (x_interp - x[i]) * a[i+1][j-1]) / (x[i] - x[i+j])
    print2d(a)
    return a[0,n-1]

print("Результат интерполяции:", aitken(x, y, x_interp))