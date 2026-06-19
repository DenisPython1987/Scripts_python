primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
contador = 0
while contador < 10:
    if contador == 0:
        print(primeiro_termo, end=' ')
    else:
        primeiro_termo += razão
        print(primeiro_termo, end=' ')
    contador += 1
