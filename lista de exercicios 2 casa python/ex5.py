##fiz com ajuda de IA !!!!!
def calcular_salario_liquido(salario_bruto):

    if salario_bruto < 800.0:
        ir_rate = 0.0
        encargos_rate = 0.0
    elif salario_bruto <= 1600.0:
        ir_rate = 0.08
        encargos_rate = 0.05
    else:
        ir_rate = 0.15   
        encargos_rate = 0.07  

    ir = salario_bruto * ir_rate
    encargos = salario_bruto * encargos_rate
    total_descontos = ir + encargos
    salario_liquido = salario_bruto - total_descontos

    return ir, encargos, total_descontos, salario_liquido

entrada = input("Digite o salário bruto (use . ou , como separador decimal): ").strip()
 
entrada = entrada.replace(',', '.')
salario_bruto = float(entrada)
if salario_bruto < 0:
            print("Salário não pode ser negativo.")


ir, encargos, total_descontos, salario_liquido = calcular_salario_liquido(salario_bruto)

print(f"\nSalário bruto: R$ {salario_bruto:.2f}")   
print(f"Imposto de Renda: R$ {ir:.2f}")
print(f"Encargos: R$ {encargos:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")

##fiz com ajuda de IA !!!!!
