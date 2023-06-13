from decimal import *
import math

def f_xsqrt_p(x, pr):
    x_pw = Decimal(1/2)-Decimal(pr)
    modificator = Decimal(1)
    for i in range(pr):
        modificator *= Decimal(1/2)-Decimal(i)
    return modificator*x**x_pw

def P(x,y, X):
    result = Decimal(0)
    to_add = Decimal(0)
    for i in range(len(x)):
        to_add = y[i]
        for j in range(len(x)):
            if i!=j:
                to_add *= (X-x[j])/(x[i]-x[j])
        result+=to_add
    return result

def factorial(x):
    result = Decimal(1)
    if x > 0:
        for i in range(x):
            result *= Decimal(i+1)
    print(result)
    return result

def eps_dif(M, X, n):
    to_mult = Decimal(1)
    for i in range(n):
        print(X-Decimal(i+1))
        to_mult *= X-Decimal(i+1)
    print(to_mult, n)
    return M/factorial(n)*to_mult

if __name__=="__main__":
    x_to_find = Decimal(2.56)
    x = [Decimal(1),
         Decimal(2),
         Decimal(3),
         Decimal(4)]
    y = [Decimal(1),
         Decimal(1.4142),
         Decimal(1.7321),
         Decimal(2)]
    p = P(x,y,x_to_find)
    m = max([abs(f_xsqrt_p(x_i+1, len(x))) for x_i in range(len(x))])
    print(m)
    e = eps_dif(m, x_to_find, len(x))
    print("P(x) = %f" %(p))
    print("Усеченная погрешность = %f" %(e))
