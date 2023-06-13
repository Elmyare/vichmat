import math, copy
from decimal import *

def max_decimal(a):
    maxx = Decimal(0)
    for c in a:
        if c>maxx:
            maxx = c
    return maxx

def matrix_minus(a,b):
    result = copy_list(a)
    for i, val_x in enumerate(b):
        for j, val_j in enumerate(val_x):
            result[i][j] -= val_j
    return result

def matrix_mult(a,b):
    rows_a = len(a)
    rows_b = len(b)
    cols_a = len(a[0])
    cols_b = len(b[0])
    if (cols_a==rows_b):
        matrix = [[Decimal(0) for row in range(cols_b)] for col in range(rows_a)]
        #print(matrix)
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    #print(i,j,k)
                    matrix[i][j] += a[i][k]*b[k][j]
        return matrix
    else:
        return None

def matrix_to_iterable(a):
    matrix = copy_list(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            #print(matrix[i][j],"/",a[i][i]," ",i,j, id(matrix[i][j]), id(a[i][j]))
            #print(a)
            matrix[i][j] = a[i][j] / a[i][i]
        #print("")
    return matrix

def enter_matrix():
    print("enter matrix. If done, just press Enter.")
    text = " "
    result = []
    while True:
        text = input()
        if text != "":
            result.append(list(map(Decimal, text.split())))
        else:
            break
    return result

def copy_list(a):
    result = [[0 for s in c] for c in a]
    for i, val1 in enumerate(a):
        for j, val2 in enumerate(val1):
            result[i][j] = copy.deepcopy(val2)
    return result

if __name__=="__main__":
    matrix = enter_matrix()
    epsilon = Decimal(float(input("Enter epsilon: ")))
    #print(matrix)
    matrix = matrix_to_iterable(matrix)
    #print("matrix: ", matrix)
    B = copy_list([[c[-1]] for c in matrix])
    #print("B:", B)
    C = copy_list([val[:i]+[Decimal(0)]+val[i+1:-1] for i, val in enumerate(matrix)])
    #print("C:", C)
    L = copy_list([(([0]*i)+[1]+([Decimal(0)]*(len(matrix)-i-1))) for i in range(len(matrix))])
    #print("L: ", L)
    c_norm = max_decimal([sum([abs(s) for s in c]) for c in C])
    b_norm = max_decimal([abs(c[0]) for c in B])
    #print("normi: ", c_norm, b_norm)
    N = round((epsilon*(Decimal(1)-c_norm)/b_norm).ln()/c_norm.ln()+Decimal(0.5))
    #print(type(N), N)
    x = [[0]]*len(C)
    print("N: ", N)
    for i in range(N):
        x_next = matrix_minus(B, matrix_mult(C, x))
        x = x_next
        print(x)

#print(matrix_sum([[1,2],[3,4]], [[5,6],[7,8]]))