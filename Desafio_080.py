"""Esse daqui eu não consegui resolver"""


valores = list()
contador = 0

while contador < 5:
    try:
        valor = int(input(f"Digite o {contador + 1}º valor: "))
        if len(valores) == 0:
            valores.append(valor)
            print(f"O valor {valor} foi inserido na posição 0")
            contador += 1
            continue
        for posição, número in enumerate(valores):
            if valor <= número:
                valores.insert(posição, valor)
                print(f"O valor {valor} foi colocado na posição {posição}.")
                contador += 1
                continue

        else:
            valores.append(valor)
            print(f"O valor {valor} foi colocado na posição {len(valores) - 1}.")
            contador += 1
            continue
    except ValueError:
        print("Valor inválido. Tente novamente.")
        continue
print(f"Os números digitados foram: ", end='')
for posição, valor in enumerate(valores):
    print(valor, end='')
    if posição < len(valores) - 1:
        print(", ", end='')
    else:
        print(".")