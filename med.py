mb = ""
pm = float("inf")
sp = 0
for x in range(5):
  medicamento = input(f"Digite o nome do medicamento: ")
  preco = float(input(f"Digite o preço: "))
  
  if preco < pm:
    pm = preco
    mb = medicamento
    
  sp += preco
media = sp/5

print(f"""
O nome do medicamento mais barato é: {mb}
O preço é {pm}
5A média aritmética é: {media}""")
