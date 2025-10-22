nm = int(input("insira seu numero menor ou igual a 50 :"))

while nm<=51:
    if nm<=250:
        nm*=3
    else:
        break

print(f"o valor max é de {nm}.")