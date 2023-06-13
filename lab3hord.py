from decimal import *

def f(x):
    return x**Decimal(2) - Decimal(3)

def mid(a,b):
    return (a*f(b)-b*f(a))/(f(b)-f(a))

if __name__=="__main__":
    E = Decimal(0.00000000000001)
    begin = Decimal(1)
    end = Decimal(2)
    middle = 0
    i = 0
    while (True):
        i += 1
        middle_prev = middle
        middle = mid(begin, end)
        
        eps = middle - middle_prev
        if f(begin)*f(middle) < 0:
            end = middle
        elif f(middle)*f(end) < 0:
            begin = middle
        print("i = %d: (%f;%f)" %(i, begin, end))

        if abs(eps)<E:
            break

