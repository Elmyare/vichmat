import math, copy
from decimal import *

def f(x):
    return Decimal(1)/x

def fillx(left, right, h):
    hrange = round((right-left)/h)
    return [Decimal(left)+(x-Decimal(1))*Decimal(h) for x in range(left, left+hrange+1)]

def filly(left, right, h):
    return list(map(f, fillx(left,right,h)))

def trapeze(y,h):
    return Decimal(h)*(Decimal(0.5)*(y[0]+y[-1])+sum(y[1:-1]))

def simpson(y,h):
    return Decimal(h)/Decimal(3)*(y[0]+y[-1]+Decimal(4)*sum(y[1:-1:2])+Decimal(2)*sum(y[2:-1:2]))

if __name__=="__main__":
    eps1 = Decimal(0.00000003)
    eps2 = Decimal(0.00000015)
    left = 1
    right = 2
    h = 0.1
    print("                2")
    print("Метод Трапеций: ∫ 1/x dx")
    print("                1")
    while True:
        first = trapeze(filly(left, right, h),h)
        second = trapeze(filly(left, right, h/2),h/2)
        print(first, second, h)
        h /= 2
        if abs(first-second)<eps1:
            break
    print("                2")
    print("Метод Симпсона: ∫ 1/x dx")
    print("                1")
    h = 0.1
    while True:
        first = simpson(filly(left, right, h),h)
        second = simpson(filly(left, right, h/2),h/2)
        print(first, second, h)
        h /= 2
        if abs(first-second)<eps2:
            break
