import math

A = float(input("insira o valor de A: "))
B = float(input("insira o valor de B: "))
C = float(input("insira o valor de C: "))

delta = B * B - 4 * A * C

if A == 0 or delta < 0:
    print("da pra calcular n pae")
else:
    r1 = (-B + math.sqrt(delta)) / (2 * A)
    r2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")