

tabela_brasileirão = ("Palmeiras", "Flamengo", "Fluminense", "Atlético_PR", "Bragantino",
                      "Bahia", "Coritiba", "São Paulo", "Atlético_MG", "Corinthians",
                      "Cruzeiro", "Botafogo", "EC Vitória", "Internacional", "Santos",
                      "Grêmio", "Vasco da Gama", "Remo", "Mirassol", "Chapecoense")

print("Os cinco primeiros colocados do Campeonato Brasileiro de 2026 são: ")
for i in range(0, 5):
    print(f"{tabela_brasileirão[i]}", end='')
    if i < 4:
        print(",", end=' ')
    else:
        print(".")

print("O quatro últimos colocados são: ")
for j, i in enumerate(tabela_brasileirão[-4:]):
    print(i, end='')
    if j < 3:
        print(", ", end='')
    else:
        print(".")

print("A tabela do Brasileirão em ordem alfabética é a seguinte:")
ordenada = sorted(tabela_brasileirão)

for i in ordenada:
    print(i)

print(f"A Chapecoense está na {tabela_brasileirão.index("Chapecoense") + 1}ª posição.")