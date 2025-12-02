while True:
    n1 = int(input("Numero um: "))
    n2 = int(input("Outro numero: "))
    print("""
    1. Media ponderada, com pesos 2 e 3, respectivamente
    2. Quadrado da soma dos 2 numeros
    3. Cubo do menor numero""")
    e = int(input(">>"))
    if e == 1:
        print(f"media ponderada de {n1} e {n2} = {(n1*2) + (n2*3) / (2+3):.2f}\n")
    elif e == 2:
        print(f"quadrado da soma de {n1} e {n2} = {(n1+n2)**2}\n")
    elif e == 3:
        if n1 < n2:
            print(f"Cubo de {n1} = {n1**3}\n")
        else:
            print(f"Cubo de {n2} = {n2**3}\n")
            