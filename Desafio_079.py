números = list()

while True:
    try:
        valor = int(input("Digite um valor: "))
        if isinstance(valor, int):
            if valor in números:
                print("O valor digitado já está cadastrado. Digite outro valor.")
                continue
            else:
                números.append(valor)
        while True:
            opção = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
            if opção not in "SN":
                print("Opção inválida. Tente novamente.")
                continue
            else:
                break
        if opção == "N":
            break
    except ValueError:
        print("Valor digitado inválido. Tente novamente.")
        continue

print(f"Os valores digitados foram: ", end='')
for i, j in enumerate(sorted(números)):
    print(f"{j}", end='')
    if i < len(números) - 1:
        print(", ", end='')
    else:
        print('.')