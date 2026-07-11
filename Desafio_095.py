from time import sleep

jogadores = list()
jogador = dict()
gols_marcados = list()
contador = total_gols = escolha_jogador = 0
plural = escolha_cadastro = escolha_continuar = ''


while True:
    saudação = "Python Futebol Clube"
    print("\033[35m-*-\033[m" * 20)
    print(f"\033[35m{saudação:^60}\033[m")
    print("\033[35m-*-\033[m" * 20)

    nome = str(input("\033[36mDigite o nome do jogador: \033[m")).strip().title()
    jogador['nome'] = nome

    while True:
        try:
            partidas = int(input(f"\033[36mQuantas partidas o jogador {jogador['nome']} jogou? \033[m"))
            if partidas < 0:
                print("\033[31mA quantidade de jogos não pode ser negativa! Tente novamente.\033[m")
                continue
            else:
                jogador['partidas'] = partidas
                break
        except ValueError:
            print("\033[31mA quantidade de partidas deve ser um número inteiro válido. Tente novamente.\033[m")
            continue

    if jogador['partidas'] == 0:
        print("\033[32mFinalizando o programa sem adicionar dados.\033[m")
    else:
        while contador < jogador['partidas']:
            try:
                gols = int(input((f"\033[36mQuantos gols o jogador {jogador['nome']}"
                                    f" fez na partida {contador + 1}: \033[m")))
                if gols < 0:
                    print("\033[31mA quantidade de gols não pode ser negativa! Tente novamente.\033[m")
                    continue
                if gols >= 0:
                    gols_marcados.append(gols)
                    total_gols += gols

                jogador['gols_marcados'] = gols_marcados[:]
                jogador['total_gols'] = total_gols
                contador += 1
            except ValueError:
                print("\033[31mO número de gols deve ser um número inteiro! Tente novamente.\033[m")
                continue
    while True:
        try:
            escolha_cadastro = str(input("\033[36mQuer cadastrar outro jogador? [S/N]: \033[m")).strip().upper()[0]
            if escolha_cadastro not in "SN":
                print("\033[31mOpção inválida! Digite apenas S ou N.\033[m")
                continue
            if escolha_cadastro in "SN":
                break
        except IndexError:
            print("\033[31mSua escolha não pode estar vazia. Digite S ou N.\033[m")
            continue
    jogadores.append(jogador.copy())
    jogador.clear()
    gols_marcados.clear()
    partidas = 0
    contador = 0
    total_gols = 0
    if escolha_cadastro == "N":
        break
    else:
        continue

while True:
    for indice, jogador in enumerate(jogadores):
        print(f"\033[35mJogador nº {indice + 1} = {jogadores[indice]['nome']}\033[m")
    while True:
        try:
            escolha_jogador = int(input("\033[35mDe qual jogador você quer ver os dados? \033[m"))
            if escolha_jogador < 0 or escolha_jogador > len(jogadores):
                print("\033[31mOpção inválida! Escolha um jogador dentro da lista.\033[m")
                continue
            else:
                break
        except ValueError:
            print("\033[31mOpção inválida! Digite apenas um número inteiro.\033[m")
            continue
    print()
    print("\033[35m-*-\033[m" * 20)
    print()
    print("\033[35mProcessando dados", end='')
    sleep(1)
    for i in range(0, 2):
        print(".", end='')
        sleep(1)
        if i == 1:
            print('.\033[m')
            sleep(1)

    print(f"\033[33mO jogador {jogadores[escolha_jogador - 1]['nome']} jogou "
          f"{jogadores[escolha_jogador - 1]['partidas']} partidas.\033[m")
    sleep(1)
    for indice, valor in enumerate(jogadores[escolha_jogador - 1]['gols_marcados']):
        if valor == 1:
            plural = "gol"
        elif valor == 0 or valor > 1:
            plural = "gols"
        print(f"\033[33mNo {indice + 1}º jogo, {jogadores[escolha_jogador - 1]['nome']} fez {valor} {plural}.\033[m")
        sleep(1)
    if jogador['total_gols'] == 0:
        print(f"\033[33mO jogador {jogadores[escolha_jogador - 1]['nome']} não fez gols em nenhuma partida.\033[m")
        sleep(1)
    elif jogador['total_gols'] == 1:
        print(f"\033[33mO jogador {jogadores[escolha_jogador - 1]['nome']} fez apenas um gol.\033[m")
        sleep(1)
    else:
        print(f"\033[33mO jogador {jogadores[escolha_jogador - 1]['nome']} fez um total de "
              f"{jogadores[escolha_jogador - 1]['total_gols']} gols.\033[m")
        sleep(1)
    while True:
        try:
            escolha_continuar = str(input("\033[35mQuer escolher outro jogador? [S/N]: \033[m")).strip().upper()[0]
            if escolha_continuar not in "SN":
                print("\033[31mEscolha inválida! Digite S ou N.\033[m")
                continue
            if escolha_continuar in "SN":
                break
        except IndexError:
            print("\033[31mSua escolha não pode ficar vazia. Tente novamente.\033[m")
            continue
    if escolha_continuar == "N":
        break
    elif escolha_continuar == "S":
        continue
despedida = "VOLTE SEMPRE"
print("\033[35m-*-\033[m" * 20)
print(f"\033[35m{despedida:^60}\033[m")
print("\033[35m-*-\033[m" * 20)