import math, copy
from decimal import *

E = 2.7182818284590452353602874

eps = 0.0001

def f(x, y, yP):
    return (E**x+y+yP)/3

def runge2(h, x0, yx0, ypx0):
    steps = round(1/h)
    first = 0
    second = 0
    while True:
        x = x0
        y = [yx0, ypx0]
        print("Шаг: %f" %(h))
        print("        X               Y               Y'")
        for i in range(steps):
            print("%.9f %.9f %.9f" %(x, y[0], y[1]))
            y0line = y[0]+y[1]*h
            y1line = y[1]+f(x,y[0],y[1])*h
            y0 = y[0] + (y[1]+y1line)*h/2
            y1 = y[1]+ (f(x,y[0],y[1]) + f(x+h, y0line, y1line))*h/2
            y[0] = y0
            y[1] = y1
            x+=h
        print("%.9f %.9f %.9f" %(x, y[0], y[1]))
        second = first
        first = y[0]
        h /= 2
        steps *= 2
        if abs(first-second)<eps:
            break

def runge4(h, x0, yx0, ypx0):
    steps = round(1/h)
    first = 0
    second = 0
    while True:
        x = x0
        y = [yx0, ypx0]
        print("Шаг: %f" %(h))
        print("        X               Y               Y'")
        for i in range(steps):
            print("%.9f %.9f %.9f" %(x, y[0], y[1]))
            k10 = h*y[1]
            k11 = h*f(x,y[0],y[1])
            k20 = h*(y[1]+0.5*k11)
            k21 = h*f(x+0.5*h,y[0]+0.5*k10,y[1]+0.5*k11)
            k30 = h*(y[1]+0.5*k21)
            k31 = h*f(x+0.5*h,y[0]+0.5*k20,y[1]+0.5*k21)
            k40 = h*(y[1]+k31)
            k41 = h*f(x+h,y[0]+k30,y[1]+k31)
            y[0] = y[0] + (k10+2*k20+2*k30+k40)/6
            y[1] = y[1] + (k11+2*k21+2*k31+k41)/6
            x+=h
        print("%.9f %.9f %.9f" %(x, y[0], y[1]))
        second = first
        first = y[0]
        h /= 2
        steps *= 2
        if abs(first-second)<eps:
            break


if __name__=="__main__":
    print("Рунге-Кутта 2:")
    runge2(h=0.1, x0=0, yx0=1, ypx0=1)
    print("Рунге-Кутта 4:")
    runge4(h=0.1, x0=0, yx0=1, ypx0=1)