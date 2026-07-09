
from time import sleep

jogador = dict()
gols_marcados = list()
contador = total_gols = 0
plural = ''

saudação = "Python Futebol Clube"
print("-*-" * 20)
print(f"{saudação:^60}")
print("-*-" * 20)

nome = str(input("Digite o nome do jogador: ")).strip().title()
jogador['nome'] = nome

while True:
    try:
        partidas = int(input(f"Quantas partidas o jogador {jogador['nome']} jogou? "))
        if partidas < 0:
            print("A quantidade de jogos não pode ser negativa! Tente novamente.")
            continue
        else:
            jogador['partidas'] = partidas
            break
    except ValueError:
        print("A quantidade de partidas deve ser um número inteiro válido. Tente novamente.")
        continue

if jogador['partidas'] == 0:
    print("Finalizando o programa sem adicionar dados.")
else:
    while contador < jogador['partidas']:
        try:
            gols = int(input((f"Quantos gols o jogador {jogador['nome']}"
                                f" fez na partida {contador + 1}: ")))
            if gols < 0:
                print("A quantidade de gols não pode ser negativa! Tente novamente.")
                continue
            if gols >= 0:
                gols_marcados.append(gols)
                total_gols += gols

            jogador['gols_marcados'] = gols_marcados
            jogador['total_gols'] = total_gols
            contador += 1
        except ValueError:
            print("O número de gols deve ser um número inteiro! Tente novamente.")
            continue

    print()
    print("-*-" * 20)
    print()
    print("Processando dados", end='')
    sleep(1)
    for i in range(0, 2):
        print(".", end='')
        sleep(1)
        if i == 1:
            print('.')
            sleep(1)

    print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
    sleep(1)
    for indice, valor in enumerate(jogador['gols_marcados']):
        if valor == 1:
            plural = "gol"
        elif valor == 0 or valor > 1:
            plural = "gols"
        print(f"No {indice + 1}º jogo, {jogador['nome']} fez {valor} {plural}.")
        sleep(1)
    if jogador['total_gols'] == 0:
        print(f"O jogador {jogador['nome']} não fez gols em nehuma partida.")
        sleep(1)
    elif jogador['total_gols'] == 1:
        print(f"O jogador {jogador['nome']} fez apenas um gol.")
        sleep(1)
    else:
        print(f"O jogador {jogador['nome']} fez um total de {jogador['total_gols']} gols.")
        sleep(1)

despedida = "VOLTE SEMPRE"
print("-*-" * 20)
print(f"{despedida:^60}")
print("-*-" * 20)