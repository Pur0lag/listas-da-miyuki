# ex2.py

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1 + n2) / 2

if media >= 6.0:
        print(f"Aluno aprovado. Média: {media:.1f}")
else:
        exame = float(input("Aluno em exame. Digite a nota do exame: "))
        mediaf = (media + exame) / 2
        if mediaf >= 5.0:
            print(f"Aluno aprovado em exame. Média final: {mediaf:.1f}")
        else:
            print(f"Aluno reprovado. Média final: {mediaf:.1f}")