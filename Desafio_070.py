nome_menor = ''
menor = 0
mais_de_mil = 0
soma = 0
while True:
    try:
        nome = str(input("Digite o nome do produto: ")).strip().upper()
        while True:
            preço = float(input("Digite o preço do produto: "))
            if preço < 1:
                print("O preço mínimo é R$1,00! Tente novamente.")
                continue
            else:
                break
    except ValueError:
        print("Preço inválido! Tente novamente.")
        continue
    if menor == 0:
        menor = preço
        nome_menor = nome
    if preço < menor:
        menor = preço
        nome_menor = nome
    soma += preço
    if preço > 1000:
        mais_de_mil += 1
    escolha = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if escolha in "Nn":
        break
if mais_de_mil == 1:
    plural = "produto"
else:
    plural = "produtos"
print(f"O total da sua compra foi R${soma}")
if mais_de_mil > 0:
    print(f"Ao todo, você comprou {mais_de_mil} {plural} com o preço maior que R$1000,00")
print(f"O produto mais barato é o {nome_menor} que custa R${menor}")
