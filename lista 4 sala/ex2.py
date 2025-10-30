import math

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *=  i
    
    return fat

A = []
for i in range(6):
    A.append(int(input(f"Insira o {i+1}° valor de A: ")))
B = []
for i in range(6):
    B.append(fatorial(A[i]))
    print("O valor de B:", B)