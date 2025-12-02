import math
print("""
Tendo:
ax² + bx + c = 0""")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if d <= 0:
    print("Raizes irreais, tente novamente.")

else:
    x1 = (-b) + sqrt(d) / 2
    x2 = (-b) - sqrt(d) / 2

    print(f"x1: {x1}\nx2: {x2}")