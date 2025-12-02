while True:
    n1 = int(input("Um numero: "))

    if n1 % 2 == 0:
        print(f"quadrado de {n1} = {n1**2}\n")
    else:
        print(f"cubo de {n1} = {n1**3}\n")