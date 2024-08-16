rpr = 0
apr = 0
prf = 0

for x in range(10):
    m = float(input("Média do aluno: "))

if m < 7:
    rpr += 1
elif m >= 4 and m < 7:
    prf += 1
elif m >= 7:
    apr += 1
else:
    print("ERRO, tente novamente.")

print("""
Alunos reprovaos: {}
Prova final: {}
Aprovador: {}
""".format(rpr, prf, apr))
