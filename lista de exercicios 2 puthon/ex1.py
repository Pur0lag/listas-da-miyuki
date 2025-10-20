n1 = float(input("Insira  a primeira nota: "))
n2 = float(input("Insira  a segunda nota: "))
n3 = float(input("Insira  a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 6.0:
    print(f"Aluno aprovado. Média = {media:.2f}")
else:
    print(f"Aluno não aprovado. Média = {media:.2f}")