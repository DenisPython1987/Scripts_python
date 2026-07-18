def cumprimento(mensagem):
    print("\033[35m-*-\033[m" * 20)
    print(f"\033[35m{mensagem:^60}\033[m")
    print("\033[35m-*-\033[m" * 20)


def ficha(nome='', gols=0):
    dicionário = dict()
    if nome == '' or gols == 0:
        dicionário['nome'] = '\033[31m<DESCONHECIDO>\033[m'
        dicionário['gols'] = gols
        return dicionário
    else:
        dicionário['nome'] = f'\033[31m{nome}\033[m'
        dicionário['gols'] = gols
        return dicionário

def verifica_int():
    while True:
        try:
            gols_função = int(input("\033[36mQuantos gols foram marcados pelo jogador? \033[m"))
            if gols_função < 0:
                print(f"\033[31mA quantidade não pode ser negativa.\033[m")
                continue
            else:
                return gols_função
        except ValueError:
            return 0

def continuar():
    while True:
        try:
            escolha = str(input("\033[36mDeseja continuar? [S/N]: \033[m")).strip().upper()[0]
            if escolha not in "SN":
                print("\033[31mEscolha inválida! Digite apenas S ou N.\033[m")
                continue
            if escolha in "SN":
                return escolha
        except IndexError:
            print("\033[31mEscolha inválida! Digite apenas S ou N.\033[m")
            continue


while True:
    cumprimento("CADASTRO DE JOGADOR")
    nome = str(input("\033[36mDigite o nome do jogador: \033[m")).strip().title()
    gols_marcados = verifica_int()
    dicionário_ficha = ficha(nome, gols_marcados)
    if gols_marcados == 0 or gols_marcados > 1:
        plural = "gols."
    else:
        plural = "gol."
    cumprimento("RESULTADOS")
    print(f"\033[36mO jogador \033[m{dicionário_ficha['nome']}\033[36m"
          f" fez \033[m\033[31m{gols_marcados}\033[m \033[36m{plural}\033[m")
    print("\033[35m-\033[m" * 60)
    escolha_principal = continuar()
    if escolha_principal == "N":
        break
cumprimento("VOLTE SEMPRE!")