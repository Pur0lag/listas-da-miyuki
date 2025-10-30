A = []
for i in range(5):
    A.append(int(input(f"Insira o {i+1}° valor de A: ")))
B = []
for i in range(5):
    B.append(int(input(f"Insira o {i+1}° valor de B: ")))
C = A + B
print("O valor de C: ", C)