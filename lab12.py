def func(x):
    return x**2 - 6*x 

eps = 0.0001
x = 0
a = 0
b = 10
i = 1
x1 = b - ((b - a) / 1.618)
x2 = a + ((b - a) / 1.618)
y1 = func(x1)
y2 = func(x2)

while True:
    if y1 < y2:
        b = x2
        x2 = x1
        x1 = b - ((b - a) / 1.618)
        y2 = y1
        y1 = func(x1)
    else:
        a = x1
        x1 = x2
        x2 = a + ((b - a) / 1.618)
        y1 = y2
        y2 = func(x2)
    print("Интервал:", a, b)
    i += 1 
    if b - a < eps:
        x = (a + b) / 2
        print("Шаги:",i)
        break
        

print("x =", x)
print("f(x) =", func(x))