soma = 0
contador = 0
maior = 0
menor = 0

while True:
    número = int(input("Digite um número: "))
    contador += 1
    soma += número
    if contador == 1:
        menor = número
    else:
        if número > maior:
            maior = número
        elif número < menor:
            menor = número
    escolha = str(input("Você quer continuar? [S/N]")).strip().upper()[0]
    if escolha in "N":
        break


print(f"A média entre os {contador} números digitados é {soma / contador}.")
print(f"O maior número foi {maior} e o menor foi {menor}")