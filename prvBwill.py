s = 0
while True:
    v = float(input("Valor do produto: R$"))
    s += v

    if v == 0:
        break

print("_"*50)
print(f"Valor total dos produtos: R${s:.2f} reais.")

if s > 300:
    print("Com desconto: R${:.2f} reais.".format(s*0.90))

elif s >= 100 and v <= 300:
    print("Com desconto: R${:.2f} reais.".format(s*0.95))

elif s < 100:
    print("Sem desconto.")
