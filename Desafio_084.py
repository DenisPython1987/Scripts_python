pessoas = list()
parcial = list()
pesados = list()
leves = list()

while True:
    parcial.append(str(input("Digite o NOME da pessoa: ")).strip().title())
    while True:
        try:
            parcial.append(float(input("Digite o PESO da pessoa: ")))
            if parcial[1] > 1:
                pessoas.append(parcial[:])
                parcial.clear()
                break
            if parcial[1] < 1:
                print("Peso inválido. Entre com um peso válido.")
                continue
        except ValueError:
            print("O peso digitado é inválido. Tente novamente.")
            continue
    while True:
        resposta = str(input("Deseja continuar? [S/N]: ")).strip().lower()[0]
        if resposta not in "sn":
            print("Opção inválida. Tente novamente.")
            continue
        else:
            break
    if resposta == "n":
        break

for i in range(0, len(pessoas)):
    if pessoas[i][1] >= 100:
        pesados.append(pessoas[i])
    if pessoas[i][1] <= 70:
        leves.append(pessoas[i])

print(f"Ao todo, foram cadastradas {len(pessoas)} pessoas.")

if len(pesados) == 1:
    print(f"A pessoa mais pesada cadastrada foi {pesados[0][0]}, com o peso de {pesados[0][1]:.2f}kg.")
elif len(pesados) == 2:
    print(f"As pessoas mais pesadas foram: {pesados[0][0]} e {pesados[1][0]} com {pesados[0][1]:.2f}kg e "
          f"{pesados[1][1]:.2f}kg, respectivamente.")
elif len(pesados) > 3:
    print("As pessoas mais pesadas, foram: ", end='')
    for i in range(0, len(pesados)):
        print(f"{pesados[i][0]} com {pesados[i][1]:.2f}kg", end='')
        if i == len(pesados) - 2:
            print(" e ", end='')
        elif i < len(pesados) - 2:
            print(", ", end='')
        elif i == len(pesados) - 1:
            print(".")
else:
    print("Não tivemos pessoas pesadas cadastradas.")

if len(leves) == 1:
    print(f"A pessoa mais leve foi {leves[0][0]}, com o peso de {leves[0][1]:.2f}kg.")
elif len(leves) == 2:
    print(f"As pessoas mais leves foram {leves[0][0]} e {leves[1][0]} com {leves[0][1]:.2f}kg e "
          f"{leves[1][1]:.2f}kg, respectivamente.")
elif len(leves) > 3:
    print("As pessoas mais leves, foram: ", end='')
    for i in range(0, len(leves)):
        print(f"{leves[i][0]} com {leves[i][1]:.2f}kg", end='')
        if i == len(leves) - 2:
            print(" e ", end='')
        elif i < len(leves) - 2:
            print(", ", end='')
        elif i == len(leves) - 1:
            print('.')
else:
    print("Não tivemos pessoas leves cadastradas.")