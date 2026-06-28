from operator import contains

contador = soma = 0

while True:
    try:
        número = int(input("Digite um número inteiro [999 para parar]: "))
        if número == 999:
            break
        else:
            contador += 1
            soma += número
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        continue
if contador == 1:
    print(f"Você digitou somente o número {soma}")
else:
    print(f"Ao todo, você digitou {contador} números e a soma entre eles é {soma}")