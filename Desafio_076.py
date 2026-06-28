contador = 0

produtos = ("Computador", 2568, "Mouse", 20.51, "Teclado", 30.65, "Tablet", 1585.5, "Scanner", 485.6,
            "Mouse Gamer", 258, "Teclado Mecânico", 585.6)
categoria = "Produtos Eletrônicos"
saudação = "Lojão do Denis"
print("-*-" * 20)
print(f"{saudação:^60}")
print("-*-" * 20)
print('')
print("-" * 60)
print(f"{categoria:^60}")
print("-" * 60)

while contador < len(produtos):
    print(f"{produtos[contador]:.<40} = {produtos[contador + 1]:.2f}")
    contador += 2

