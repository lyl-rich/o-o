prim = float(input("Digite o primeiro termo de PA: "))
quantidade = int(input("Digite a quantidade de termos: "))
razao = float(input("Digite a razao de PA: "))

print("Os termos da Progressao aritmetica sao: ")
for n in range(quantidade):
  termo = prim + n * razao
  print(termo)
