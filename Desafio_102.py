from time import sleep

escolha = ""

def cumprimento(mensagem):
    print("\033[35m-*-\033[m" * 20)
    print(f"\033[35m{mensagem:^60}\033[m")
    print("\033[35m-*-\033[m" * 20)


def fatorial(número, show=False):
    fator = 1
    for valor in range(número, 1, -1):
        fator *= valor
        if show:
            print(f"\033[36m{valor} x {valor - 1} = {fator}\033[m")
            sleep(1)
    print(f"\033[34mfatorial de {número} = {fator}\033[m")

def show_fatorial():
    while True:
        try:
            show = str(input("\033[32mVocê deseja ver o SHOW? [S/N]: \033[m")).strip().upper()[0]
            if show not in "SN":
                print("\033[31mOpção inválida! Digite apenas S ou N.\033[m")
                continue
            if show == "S":
                return True
            else:
                return False
        except IndexError:
            print("\033[31mOpção inválida! Digite apenas S ou N.\033[m")
            continue



while True:
    try:
        cumprimento("CÁLCULO DE FATORIAL")
        valor = int(input("\033[32mDigite um número inteiro para ver seu fatorial: \033[m"))
        show = show_fatorial()
        if valor <= 0:
            print("\033[31mO valor precisar ser um número natural maior que zero.\033[m")
            continue
        else:
            fatorial(valor, show)
            while True:
                try:
                    escolha = str(input("\033[33mDeseja ver o fatorial de "
                                        "outro número? [S/N]: \033[m")).strip().upper()[0]
                    if escolha not in "SN":
                        print("\033[31mOpção inválida! Digite apenas S ou N.\033[m")
                        continue
                    if escolha in "SN":
                        break
                except IndexError:
                    print("\033[31mSua opção não pode estar vazia. Digite S ou N.\033[m")
                    continue
        if escolha == "N":
            break
    except ValueError:
        print("\033[31mOpção inválida! Digite apenas números naturais maiores que zero.\033[m")
        continue

cumprimento("VOLTE SEMPRE!!!")