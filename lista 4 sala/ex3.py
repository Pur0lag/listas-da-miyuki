A = []
for i in range(5):
    A.append(int(input(f"Insira o {i+1}° valor de A: ")))
B = []
for i in range(5):
    B.append(int(input(f"Insira o {i+1}° valor de B: ")))
C = []
for i in range(5):
    C.append(A[i]-B[i])
    print("O valor de C: ", C)