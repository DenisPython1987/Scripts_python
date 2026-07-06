números = [[], []]
contador = 0
while contador < 7:
    try:
        valor = int(input(f"Digite o {contador + 1}º valor: "))
        if valor % 2 == 0:
            números[0].append(valor)
            números[0].sort()
        else:
            números[1].append(valor)
            números[1].sort()
        contador += 1
    except ValueError:
        print("Valor inválido! Tente novamente.")
        continue

print("Os números pares digitados foram: ", end='')
for indice in range(0, len(números[0])):
    print(f"{números[0][indice]}", end='')
    if indice < len(números[0]) - 2:
        print(", ", end='')
    elif indice == len(números[0]) - 2:
        print(" e ", end="")
    else:
        print(".")

print("Os valores ímpares digitados foram: ", end='')
for indice in range(0, len(números[1])):
    print(f"{números[1][indice]}", end='')
    if indice < len(números[1]) - 2:
        print(", ", end='')
    elif indice == len(números[1]) - 2:
        print(" e ", end="")
    else:
        print(".")
