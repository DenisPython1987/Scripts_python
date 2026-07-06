from random import randint
from time import sleep

megasena = list()
parcial = list()

while True:
    try:
        número = int(input("Quantos jogos você quer? "))
        if número < 0:
            print("Por favor, digite um valor positivo para a quantidade de jogos!")
            continue
        for jogo in range(número):
            for aposta in range(0, 6):
                parcial.append(randint(1, 60))
            megasena.append(parcial[:])
            parcial.clear()
        break
    except ValueError:
        print("Número inválido. Tente novamente.")
        continue

for i in range(len(megasena)):
    print(f"O {i + 1}º jogo foi: ", end='')
    for indice in range(0, len(megasena[i])):
        print(f"{megasena[i][indice]}", end='')
        if indice < len(megasena[i]) - 1:
            print(", ", end='')
        else:
            print('.')