A = []
for i in range(8):
    A.append(int(input(f"Insira o {i+1} valor de A: ")))
B = []
for i in range(8):
    B.append(A[i] ** 2)
print("Vetor B:", B)