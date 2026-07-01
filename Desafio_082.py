números = list()
pares = list()
ímpares = list()

def ponto_vírgula(índice, lista):
    if índice < len(lista) - 1:
        print(", ", end='')
    else:
        print(".")

while True:
    try:
        valor = int(input("Digite um valor: "))
        números.append(valor)
        while True:
            opção = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
            if opção in "SN":
                break
            if opção not in "SN":
                print("Opção inválida. Tente novamente.")
                continue
        if opção == "N":
            break
    except ValueError:
        print("Digite apenas números inteiros.")
        continue

for i in números:
    if i % 2 == 0:
        pares.append(i)
    else:
        ímpares.append(i)

print("Os números digitados foram: ", end='')
for posição, valor in enumerate(números):
    print(valor, end='')
    ponto_vírgula(posição, números)

print("Os números pares digitados foram: ", end='')
for posição, valor in enumerate(pares):
    print(valor, end='')
    ponto_vírgula(posição, pares)

print("Os números ímpares digitados foram: ", end='')
for posição, valor in enumerate(ímpares):
    print(valor, end='')
    ponto_vírgula(posição, ímpares)
