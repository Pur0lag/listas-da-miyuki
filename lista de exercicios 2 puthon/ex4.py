
a = float(input("Informe o lado A: ").strip())
b = float(input("Informe o lado B: ").strip())
c = float(input("Informe o lado C: ").strip())


if a <= 0 or b <= 0 or c <= 0:
    print("Não forma um triângulo ")
    

if not (a < b + c and b < a + c and c < a + b):
    print("Não forma um triângulo.")



if a == b and b == c:
    print("Triângulo equilátero.")
else:
    if a == b or a == c or b == c:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")