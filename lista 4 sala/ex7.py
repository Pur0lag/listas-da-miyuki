A = []
for i in range(10):
    A.append(int(input(f"Insira o {i+1}° valor de A: ")))
B = []
for i in range(10):
    B.append(A[9-i])
print("Vetor B (invertido):", B)