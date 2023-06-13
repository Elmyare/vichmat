e_trap = 0.00000001 * 3
e_simp = 0.00000001 * 15
def fillx(h):
    down = 1
    up = 2
    t_x = []
    while (down <= up+(h/2)):
        t_x.append(down)
        down += h
    x = t_x
    return x

def filly(h):
    down = 1
    up = 2
    t_y = []
    while (down <= up+(h/2)):
        t_y.append(func(down))
        down += h
    y = t_y
    return y

def func(x):
    return 1/x

def Trap(y,h):
    s = 0
    for i in range(1,len(y)-1):
        s += y[i]
    v = 0.5 * (y[0] + y[len(y)-1])
    return h * (v + s)

def Simp(y,h):
    v = 0
    b = 0
    for i in range(1,len(y)-1):
        if i % 2 == 1:
            v += y[i]
        else:
            b += y[i]
    return (h / 3) * (y[0] + y[len(y)-1] + 4 * v + 2 * b)
h1 = 0.1
h2 = 0.1
result = 1
print("                2")
print("Метод Трапеций: ∫ 1/x dx")
print("                1")
while result > e_trap:
    h2 = h1 / 2
    first = Trap(filly(h1),h1)
    second = Trap(filly(h2),h2)
    result = abs(second - first)
    print(first,second,h1)
    h1 /= 2
result = 1
h1 = 0.1
h2 = 0.1
print("                2")
print("Метод Симпсона: ∫ 1/x dx")
print("                1")
while result > e_simp:
    h2 = h1 / 2
    first = Simp(filly(h1),h1)
    second = Simp(filly(h2),h2)
    result = abs(second - first)
    print(first,second,h1)
    h1 /= 2
    



    
    