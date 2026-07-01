número_cinco = []
números = []

while True:
    try:
        valor = int(input("Digite um valor: "))
        números.append(valor)
        while True:
            opção = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
            if opção not in "SN":
                continue
            else:
                break
        if opção == "N":
            break
    except ValueError:
        print("Valor inválido. Tente novamente.")
        continue

números.sort(reverse=True)
print(f"Foram digitados {len(números)}")
print("Os valores digitados, em ordem decrescente, foram: ", end='')
for posição, valores in enumerate(números):
    print(valores, end='')
    if posição < len(números) - 1:
        print(", ", end='')
    else:
        print('.')

if 5 in números:
    print("O número cinco foi digitado.")
else:
    print("O número cinco não foi digitado.")
