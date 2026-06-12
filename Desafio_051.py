primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
termo = primeiro_termo

for i in range(1, 11):
    if i == 1:
        print(primeiro_termo)
    else:
        print(termo + razão)
        termo += razão