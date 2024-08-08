a = int(input("Informe um número inteiro: "))
b = int(input("Outro: "))

if a < b:
soma = 0
for inter in range(a,b + 1):
soma += inter
print(f"{a} + {b} = {soma}")
else:
print("ERRO, tente novamente")
