from decimal import *

def f(x):
    return x**Decimal(2) - Decimal(3)

def mid(a,b):
    return (a+b)/2

def epsilon(a,b):
    return abs(b-a)/2

if __name__=="__main__":
    E = Decimal(0.00001)
    eps = Decimal(1)
    begin = Decimal(1)
    end = Decimal(2)
    i = 0
    while (eps>E):
        i += 1
        middle = mid(begin, end)
        eps = epsilon(begin,end)
        if f(begin)*f(middle) < 0:
            end = middle
        elif f(middle)*f(end) < 0:
            begin = middle
        print("i = %d: (%f;%f)" %(i, begin, end))

