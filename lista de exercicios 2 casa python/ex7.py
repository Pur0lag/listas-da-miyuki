num = int(input("insira um numero de 1 a 5: "))
if num < 1 or num > 5:
    print("Número inválido.")
match num:
    case 1:
        print(f'Engenharia')
    case 2:
        print(f'Edificações')
    case 3:
        print(f'Sistemas elétricos')
    case 4:
        print(f'Turismo')
    case 5:
        print(f'Análise de Sistemas')