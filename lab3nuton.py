from decimal import *

def f(x):
    return x**Decimal(2) - Decimal(3)

def f_p(x):
    return 2*x

if __name__=="__main__":
    E = Decimal(0.00000000000001)
    begin = Decimal(1)
    end = Decimal(2)
    x_prev = Decimal(2)
    i = 0
    while True:
        i += 1
        x = x_prev-(f(x_prev)/f_p(x_prev))
        eps = x - x_prev
        x_prev = x
        print("X%d = %f" %(i, x))
        if abs(eps)<E:
            break

