
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
   
      

nums = [a, b, c]
nums_sorted = sorted(nums)

menor = nums_sorted[0]
medio = nums_sorted[1]
maior = nums_sorted[2]

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"O número do meio é: {medio}")

