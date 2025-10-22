fi = [1, 1]

while len(fi) < 15:
    proximo = fi[-1] + fi[-2]
    fi.append(proximo)

# Exibe a série
print("Série de Fibonacci até o 15º termo:")
print(fi)
