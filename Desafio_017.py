from math import hypot

cateto_adjacente = float(input("Digite o cateto adjacente: "))
cateto_oposto = float(input("Digite o cateo oposto: "))

print(f"A hipotenusa é {hypot(cateto_adjacente, cateto_adjacente):.2f}")
