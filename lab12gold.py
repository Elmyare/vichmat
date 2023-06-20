import math, copy
from decimal import *

def f(x):
    return x**2-6*x

if __name__=="__main__":
    a = Decimal(0)
    b = Decimal(10)
    eps = Decimal(0.0001)
    i = 1
    x1 = a+Decimal(0.382)*(b-a)
    x2 = a+Decimal(0.618)*(b-a)
    y1 = f(x1)
    y2 = f(x2)
    while True:
        if y1>y2:
            a = x1
            x1 = x2
            x2 = a+Decimal(0.618)*(b-a)
            y1 = y2
            y2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a+Decimal(0.382)*(b-a)
            y2 = y1
            y1 = f(x1)
        print("Шаг %d: a = %.15f, b = %.15f" %(i, a, b))
        i += 1
        if abs(b-a)<eps:
            x = (a+b)/Decimal(2)
            print("x = %.15f, f(x) = %.15f" %(x, f(x)))
            break
