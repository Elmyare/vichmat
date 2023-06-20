import math, copy
from decimal import *

def f(x):
    return x**2-6*x

if __name__=="__main__":
    a = Decimal(0)
    b = Decimal(10)
    eps = Decimal(0.0001)
    i = 1
    while True:
        y1 = a+Decimal(0.382)*(b-a)
        y2 = a+Decimal(0.618)*(b-a)
        if f(y1)>f(y2):
            a = y1
        else:
            b = y2
        print("Шаг %d: a = %.15f, b = %.15f" %(i, a, b))
        i += 1
        if abs(b-a)<eps:
            x = (a+b)/Decimal(2)
            print("x = %.15f, f(x) = %.15f" %(x, f(x)))
            break
