primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
contador = 0
posição = 10
while contador <= posição:
    print(primeiro_termo, end=' ')
    primeiro_termo += razão
    if contador == posição:
        posição = int(input("\nVocê deseja ver mais quantas posições? Digite zero para sair: "))
        if posição == 0:
            break
        else:
            continue
    contador += 1