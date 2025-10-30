A = []
for i in range(5):
    A.append(int(input(f"insira  {i+1}° do vetor A: ")))
B = []
for i in range(5):
    B.append(A[i] * 3)
    print("O vetor B é:", B)