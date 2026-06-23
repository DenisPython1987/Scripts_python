from random import randint
computador_escolha = ''
jogador_escolha = ''
condição = 0
vitória = 0
plural = ''
while True:
    while True:
        saudação = "JOGO DE PAR OU ÍMPAR"
        print("-*-" * 20)
        print(f'{saudação:^60}')
        print("-*-" * 20)
        computador_inteiro = randint(1, 10)
    
        try:
            jogador = int(input("""
            Qual é a sua escolha?
            [ 1 ] PAR
            [ 2 ] ÍMPAR
            Responda aqui: """))
            if jogador == 1:
                jogador_escolha = "par"
                computador_escolha = "ímpar"
                condição = 1
                break
            elif jogador == 2:
                jogador_escolha = "ímpar"
                computador_escolha = "par"
                condição = 2
                break
        except ValueError:
            print("Opção inválida! escolha entre [ 1 ]     PAR ou [ 2 ] ÍMPAR")
            continue
    while True:
        try:
            jogada = int(input("Qual número você     vai jogar (de 1 a 10)?"))
            if 0 > jogada > 11:
                print("Opção inválida! escolha um número entre 1 e 10.")
                continue
            elif 0 < jogada < 11:
                break
        except ValueError:
            print("Opção inválida! Escolha um número entre 1 e 10.")
            continue
    if condição == 1 and (computador_inteiro + jogada) % 2 == 0:
        print(f"Eu joguei {computador_inteiro} e você jogou {jogada}, o total deu {computador_inteiro + jogada}")
        print("Deu PAR!!! Você ganhou!")
        vitória += 1
        continue
    elif condição == 1 and (computador_inteiro + jogada) % 2 == 1:
        print(f"Eu joguei {computador_inteiro} e você jogou {jogada}, deu {computador_inteiro + jogada}")
        print("Deu ÍMPAR!!! Você perdeu!")
        if vitória == 1:
            plural = "partida"
        elif vitória > 1 or vitória == 0:
            plural = "partidas"
        print(f"Ao todo, você venceu um total de {vitória} {plural}")
        break
    if condição == 2 and (computador_inteiro + jogada) % 2 == 1:
        print(f"Eu joguei {computador_inteiro} e você jogou {jogada}, deu {computador_inteiro + jogada}")
        print("Deu ÍMPAR!!! Você ganhou!")
        vitória += 1
        continue
    elif condição == 2 and (computador_inteiro + jogada) % 2 == 0:
        print(f"Eu joguei {computador_inteiro} e você jogou {jogada}, deu {computador_inteiro + jogada}")
        print("Deu PAR!!! Você perdeu!")
        if vitória == 1:
            plural = "vitória"
        elif vitória > 1 or vitória == 0:
            plural = "vitórias"
        print(f"Ao todo, você venceu um total de {vitória} {plural}")
        break